"""
PDF Text Extraction Utility for Scientific Papers

This module provides functionality to extract text, metadata, and structure
from PDF scientific papers. It preserves section hierarchy and identifies
code blocks, mathematical formulas, and tables.
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path

try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False
    try:
        import PyPDF2
        PYPDF2_AVAILABLE = True
    except ImportError:
        PYPDF2_AVAILABLE = False


@dataclass
class PaperMetadata:
    """Metadata extracted from a PDF paper."""
    title: Optional[str] = None
    authors: List[str] = None
    year: Optional[str] = None
    doi: Optional[str] = None
    abstract: Optional[str] = None
    
    def __post_init__(self):
        if self.authors is None:
            self.authors = []


@dataclass
class ExtractedContent:
    """Structured content extracted from a PDF."""
    metadata: PaperMetadata
    full_text: str
    pages: List[Dict[str, any]]
    sections: List[Dict[str, any]]
    code_blocks: List[Dict[str, any]]
    tables: List[Dict[str, any]]
    formulas: List[str]
    
    def __init__(self):
        self.metadata = PaperMetadata()
        self.full_text = ""
        self.pages = []
        self.sections = []
        self.code_blocks = []
        self.tables = []
        self.formulas = []


class PDFExtractor:
    """Extracts text and structure from PDF files."""
    
    def __init__(self, pdf_path: str):
        """
        Initialize PDF extractor.
        
        Args:
            pdf_path: Path to the PDF file
        """
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        self.extractor_method = self._determine_extractor()
    
    def _determine_extractor(self) -> str:
        """Determine which PDF extraction library is available."""
        if PDFPLUMBER_AVAILABLE:
            return "pdfplumber"
        elif PYPDF2_AVAILABLE:
            return "pypdf2"
        else:
            raise ImportError(
                "No PDF extraction library available. "
                "Please install pdfplumber (recommended) or PyPDF2: "
                "pip install pdfplumber"
            )
    
    def extract(self) -> ExtractedContent:
        """
        Extract all content from the PDF.
        
        Returns:
            ExtractedContent object with all extracted information
        """
        content = ExtractedContent()
        
        if self.extractor_method == "pdfplumber":
            content = self._extract_with_pdfplumber()
        elif self.extractor_method == "pypdf2":
            content = self._extract_with_pypdf2()
        
        # Post-process to extract metadata and structure
        self._extract_metadata(content)
        self._identify_sections(content)
        self._identify_code_blocks(content)
        self._identify_formulas(content)
        
        return content
    
    def _extract_with_pdfplumber(self) -> ExtractedContent:
        """Extract using pdfplumber (better quality)."""
        content = ExtractedContent()
        full_text_parts = []
        
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    full_text_parts.append(text)
                    content.pages.append({
                        "page_number": page_num,
                        "text": text,
                        "width": page.width,
                        "height": page.height
                    })
                
                # Extract tables
                tables = page.extract_tables()
                for table in tables:
                    content.tables.append({
                        "page_number": page_num,
                        "table": table
                    })
        
        content.full_text = "\n\n".join(full_text_parts)
        return content
    
    def _extract_with_pypdf2(self) -> ExtractedContent:
        """Extract using PyPDF2 (fallback)."""
        import PyPDF2
        
        content = ExtractedContent()
        full_text_parts = []
        
        with open(self.pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extract_text()
                if text:
                    full_text_parts.append(text)
                    content.pages.append({
                        "page_number": page_num,
                        "text": text
                    })
        
        content.full_text = "\n\n".join(full_text_parts)
        return content
    
    def _extract_metadata(self, content: ExtractedContent):
        """Extract paper metadata from the first few pages."""
        # Try to extract title (usually first line or in first page)
        first_page_text = content.pages[0]["text"] if content.pages else ""
        lines = first_page_text.split('\n')[:20]  # First 20 lines
        
        # Look for title (usually the largest text or first significant line)
        if lines:
            # Title is often the first non-empty line that's not too short
            for line in lines[:10]:
                line = line.strip()
                if line and len(line) > 10 and not line.lower().startswith(('abstract', 'introduction')):
                    content.metadata.title = line
                    break
        
        # Try to extract authors (look for patterns like "Author1, Author2, and Author3")
        author_patterns = [
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+and\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)*)',
            r'([A-Z]\.[\s]*[A-Z][a-z]+(?:\s+and\s+[A-Z]\.[\s]*[A-Z][a-z]+)*)',
        ]
        
        for line in lines[:15]:
            for pattern in author_patterns:
                matches = re.findall(pattern, line)
                if matches and len(matches[0]) > 5:
                    # Split authors
                    authors_text = matches[0]
                    if ' and ' in authors_text:
                        parts = authors_text.split(' and ')
                        content.metadata.authors.extend([p.strip() for p in parts])
                    elif ',' in authors_text:
                        content.metadata.authors = [a.strip() for a in authors_text.split(',')]
                    else:
                        content.metadata.authors = [authors_text.strip()]
                    break
            if content.metadata.authors:
                break
        
        # Extract year (look for 4-digit year)
        year_pattern = r'\b(19|20)\d{2}\b'
        for line in lines:
            matches = re.findall(year_pattern, line)
            if matches:
                # Get full year
                full_year_match = re.search(r'\b(19|20)\d{2}\b', line)
                if full_year_match:
                    content.metadata.year = full_year_match.group()
                    break
        
        # Extract DOI
        doi_pattern = r'DOI[:\s]*([0-9]+\.[0-9]+/[^\s]+)'
        doi_match = re.search(doi_pattern, content.full_text, re.IGNORECASE)
        if doi_match:
            content.metadata.doi = doi_match.group(1)
        
        # Try to extract abstract
        abstract_pattern = r'(?i)abstract[:\s]*(.+?)(?=\n\s*(?:1\.|introduction|keywords|index terms))'
        abstract_match = re.search(abstract_pattern, content.full_text, re.DOTALL)
        if abstract_match:
            content.metadata.abstract = abstract_match.group(1).strip()
    
    def _identify_sections(self, content: ExtractedContent):
        """Identify major sections in the paper."""
        # Common section headers
        section_patterns = [
            r'^\s*\d+\.\s*([A-Z][^\n]+)',  # Numbered sections: "1. Introduction"
            r'^\s*([A-Z][A-Z\s]+)\s*$',     # ALL CAPS headers
            r'^\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*$',  # Title Case headers
        ]
        
        lines = content.full_text.split('\n')
        current_section = None
        section_text = []
        
        for line in lines:
            line_stripped = line.strip()
            
            # Check if this line is a section header
            is_header = False
            for pattern in section_patterns:
                match = re.match(pattern, line_stripped)
                if match and len(line_stripped) < 100:  # Headers are usually short
                    # Save previous section
                    if current_section:
                        content.sections.append({
                            "title": current_section,
                            "content": "\n".join(section_text)
                        })
                    
                    # Start new section
                    current_section = line_stripped
                    section_text = []
                    is_header = True
                    break
            
            if not is_header and current_section:
                section_text.append(line)
        
        # Save last section
        if current_section:
            content.sections.append({
                "title": current_section,
                "content": "\n".join(section_text)
            })
    
    def _identify_code_blocks(self, content: ExtractedContent):
        """Identify potential code blocks in the text."""
        # Patterns that suggest code blocks
        code_indicators = [
            r'```(\w+)?\n(.*?)```',  # Markdown code blocks
            r'function\s+\w+\s*\(',   # Function definitions
            r'def\s+\w+\s*\(',        # Python functions
            r'class\s+\w+',            # Class definitions
            r'import\s+\w+',           # Import statements
            r'#include\s*<',           # C/C++ includes
            r'public\s+class',         # Java classes
        ]
        
        # Look for code-like patterns
        lines = content.full_text.split('\n')
        current_block = []
        in_code_block = False
        
        for i, line in enumerate(lines):
            # Check if line looks like code
            looks_like_code = any(re.search(pattern, line) for pattern in code_indicators)
            
            if looks_like_code:
                if not in_code_block:
                    in_code_block = True
                    current_block = [line]
                else:
                    current_block.append(line)
            else:
                if in_code_block and len(current_block) > 2:
                    # Save code block
                    code_text = "\n".join(current_block)
                    # Try to detect language
                    language = self._detect_language(code_text)
                    content.code_blocks.append({
                        "language": language,
                        "code": code_text,
                        "line_number": i - len(current_block)
                    })
                in_code_block = False
                current_block = []
    
    def _detect_language(self, code: str) -> str:
        """Detect programming language from code snippet."""
        language_indicators = {
            "python": ["def ", "import ", "print(", "if __name__"],
            "javascript": ["function ", "const ", "let ", "=>", "console.log"],
            "java": ["public class", "public static void", "System.out.println"],
            "cpp": ["#include", "using namespace", "std::"],
            "c": ["#include", "int main(", "printf("],
        }
        
        code_lower = code.lower()
        for lang, indicators in language_indicators.items():
            if any(indicator.lower() in code_lower for indicator in indicators):
                return lang
        
        return "unknown"
    
    def _identify_formulas(self, content: ExtractedContent):
        """Identify mathematical formulas in the text."""
        # Patterns for mathematical formulas
        formula_patterns = [
            r'\$[^$]+\$',              # Inline LaTeX: $formula$
            r'\$\$[^$]+\$\$',          # Block LaTeX: $$formula$$
            r'\\begin\{equation\}.*?\\end\{equation\}',  # LaTeX equation environment
            r'[A-Za-z]\s*=\s*[^=]+',   # Simple equations: x = ...
            r'\\[a-z]+\s*\([^)]+\)',   # LaTeX functions: \sin(x)
        ]
        
        for pattern in formula_patterns:
            matches = re.findall(pattern, content.full_text, re.DOTALL)
            content.formulas.extend(matches)


def extract_pdf(pdf_path: str) -> ExtractedContent:
    """
    Convenience function to extract content from a PDF.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        ExtractedContent object
    """
    extractor = PDFExtractor(pdf_path)
    return extractor.extract()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python pdf_extractor.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    try:
        content = extract_pdf(pdf_path)
        print(f"Extracted {len(content.pages)} pages")
        print(f"Found {len(content.sections)} sections")
        print(f"Found {len(content.code_blocks)} code blocks")
        print(f"Found {len(content.formulas)} formulas")
        print(f"\nTitle: {content.metadata.title}")
        print(f"Authors: {', '.join(content.metadata.authors)}")
        print(f"Year: {content.metadata.year}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

