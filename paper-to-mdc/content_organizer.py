"""
Content Organizer for Scientific Papers

This module organizes extracted PDF content into structured sections
suitable for MDC generation. It identifies key concepts, techniques,
and organizes content by paper structure.
"""

import re
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from pdf_extractor import ExtractedContent, PaperMetadata


@dataclass
class OrganizedSection:
    """A section of organized content."""
    title: str
    content: str
    subsections: List['OrganizedSection'] = field(default_factory=list)
    code_blocks: List[Dict[str, any]] = field(default_factory=list)
    formulas: List[str] = field(default_factory=list)
    key_concepts: List[str] = field(default_factory=list)
    implementation_details: List[str] = field(default_factory=list)
    best_practices: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)


@dataclass
class OrganizedContent:
    """Fully organized content ready for MDC generation."""
    metadata: PaperMetadata
    abstract: str
    key_concepts: List[str]
    methodology: OrganizedSection
    implementation_patterns: List[str]
    code_examples: List[Dict[str, any]]
    formulas: List[str]
    best_practices: List[str]
    performance_metrics: List[str]
    limitations: List[str]
    related_techniques: List[str]
    practical_applications: List[str]
    sections: List[OrganizedSection] = field(default_factory=list)


class ContentOrganizer:
    """Organizes extracted PDF content into structured format."""
    
    def __init__(self, extracted_content: ExtractedContent):
        """
        Initialize content organizer.
        
        Args:
            extracted_content: ExtractedContent from PDF extractor
        """
        self.extracted = extracted_content
        self.organized = OrganizedContent(
            metadata=extracted_content.metadata,
            abstract="",
            key_concepts=[],
            methodology=OrganizedSection(title="Methodology", content=""),
            implementation_patterns=[],
            code_examples=[],
            formulas=[],
            best_practices=[],
            performance_metrics=[],
            limitations=[],
            related_techniques=[],
            practical_applications=[]
        )
    
    def organize(self) -> OrganizedContent:
        """
        Organize all extracted content.
        
        Returns:
            OrganizedContent ready for MDC generation
        """
        # Extract abstract
        self._extract_abstract()
        
        # Organize sections
        self._organize_sections()
        
        # Extract key concepts
        self._extract_key_concepts()
        
        # Organize methodology
        self._organize_methodology()
        
        # Extract implementation patterns
        self._extract_implementation_patterns()
        
        # Organize code examples
        self._organize_code_examples()
        
        # Organize formulas
        self._organize_formulas()
        
        # Extract best practices
        self._extract_best_practices()
        
        # Extract performance metrics
        self._extract_performance_metrics()
        
        # Extract limitations
        self._extract_limitations()
        
        # Extract related techniques
        self._extract_related_techniques()
        
        # Extract practical applications
        self._extract_practical_applications()
        
        return self.organized
    
    def _extract_abstract(self):
        """Extract and clean abstract."""
        if self.extracted.metadata.abstract:
            self.organized.abstract = self.extracted.metadata.abstract
        else:
            # Try to find abstract section
            for section in self.extracted.sections:
                if 'abstract' in section['title'].lower():
                    self.organized.abstract = section['content']
                    break
    
    def _organize_sections(self):
        """Organize paper sections."""
        for section in self.extracted.sections:
            organized_section = OrganizedSection(
                title=section['title'],
                content=section['content']
            )
            
            # Extract code blocks from this section
            organized_section.code_blocks = [
                cb for cb in self.extracted.code_blocks
                if self._is_code_in_section(cb, section['content'])
            ]
            
            # Extract formulas from this section
            organized_section.formulas = [
                f for f in self.extracted.formulas
                if f in section['content']
            ]
            
            # Extract key concepts
            organized_section.key_concepts = self._extract_concepts_from_text(
                section['content']
            )
            
            self.organized.sections.append(organized_section)
    
    def _is_code_in_section(self, code_block: Dict, section_content: str) -> bool:
        """Check if code block appears in section content."""
        code_snippet = code_block.get('code', '')[:100]  # First 100 chars
        return code_snippet in section_content
    
    def _extract_key_concepts(self):
        """Extract key concepts and techniques from the paper."""
        # Look for common concept indicators
        concept_patterns = [
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:is|are|refers to|denotes)',
            r'(?:technique|method|approach|algorithm|pattern|framework)\s+(?:called|named|termed)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'([A-Z][A-Z]+)',  # Acronyms
        ]
        
        concepts = set()
        full_text = self.extracted.full_text
        
        for pattern in concept_patterns:
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0] if match else ""
                if match and len(match) > 2 and len(match) < 50:
                    concepts.add(match.strip())
        
        # Also look in section titles
        for section in self.extracted.sections:
            title = section['title']
            # Extract significant words from titles
            words = re.findall(r'\b[A-Z][a-z]+\b', title)
            concepts.update(words)
        
        self.organized.key_concepts = sorted(list(concepts))[:20]  # Top 20
    
    def _organize_methodology(self):
        """Organize methodology section."""
        methodology_keywords = [
            'methodology', 'method', 'approach', 'algorithm',
            'technique', 'framework', 'architecture', 'design'
        ]
        
        methodology_content = []
        
        for section in self.extracted.sections:
            title_lower = section['title'].lower()
            if any(keyword in title_lower for keyword in methodology_keywords):
                methodology_content.append(section['content'])
                # Add code blocks and formulas
                self.organized.methodology.code_blocks.extend([
                    cb for cb in self.extracted.code_blocks
                    if self._is_code_in_section(cb, section['content'])
                ])
                self.organized.methodology.formulas.extend([
                    f for f in self.extracted.formulas
                    if f in section['content']
                ])
        
        self.organized.methodology.content = "\n\n".join(methodology_content)
    
    def _extract_implementation_patterns(self):
        """Extract implementation patterns and design patterns."""
        pattern_keywords = [
            'pattern', 'design pattern', 'architecture pattern',
            'implementation', 'structure', 'organization',
            'component', 'module', 'layer'
        ]
        
        patterns = []
        full_text = self.extracted.full_text
        
        # Look for pattern descriptions
        for keyword in pattern_keywords:
            pattern_regex = rf'{keyword}[:\s]+([^\.]+)'
            matches = re.findall(pattern_regex, full_text, re.IGNORECASE)
            patterns.extend([m.strip() for m in matches if len(m.strip()) > 10])
        
        self.organized.implementation_patterns = patterns[:15]  # Top 15
    
    def _organize_code_examples(self):
        """Organize all code examples."""
        self.organized.code_examples = self.extracted.code_blocks.copy()
        
        # Enhance with context if available
        for code_block in self.organized.code_examples:
            # Try to find context around the code
            code_text = code_block.get('code', '')
            if code_text:
                # Look for code in full text to get surrounding context
                idx = self.extracted.full_text.find(code_text[:50])
                if idx > 0:
                    context_start = max(0, idx - 200)
                    context_end = min(len(self.extracted.full_text), idx + len(code_text) + 200)
                    context = self.extracted.full_text[context_start:context_end]
                    code_block['context'] = context
    
    def _organize_formulas(self):
        """Organize all mathematical formulas."""
        # Remove duplicates while preserving order
        seen = set()
        unique_formulas = []
        for formula in self.extracted.formulas:
            formula_clean = formula.strip()
            if formula_clean and formula_clean not in seen:
                seen.add(formula_clean)
                unique_formulas.append(formula_clean)
        
        self.organized.formulas = unique_formulas
    
    def _extract_best_practices(self):
        """Extract best practices and recommendations."""
        practice_keywords = [
            'best practice', 'recommendation', 'should', 'must',
            'guideline', 'suggestion', 'advice', 'tip'
        ]
        
        practices = []
        full_text = self.extracted.full_text
        
        for keyword in practice_keywords:
            # Look for sentences containing practice keywords
            pattern = rf'[^\.]*{keyword}[^\.]*\.'
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            practices.extend([m.strip() for m in matches if len(m.strip()) > 20])
        
        self.organized.best_practices = practices[:20]  # Top 20
    
    def _extract_performance_metrics(self):
        """Extract performance metrics and benchmarks."""
        metric_patterns = [
            r'(\d+\.?\d*)\s*(?:ms|seconds?|milliseconds?)',  # Time metrics
            r'(\d+\.?\d*)\s*(?:%|percent)',  # Percentage metrics
            r'(\d+\.?\d*)\s*(?:x|times)\s+(?:faster|slower|better)',  # Comparison metrics
            r'(?:accuracy|precision|recall|F1|score)[:\s]+(\d+\.?\d*)',  # ML metrics
            r'(\d+\.?\d*)\s*(?:MB|GB|KB)',  # Size metrics
        ]
        
        metrics = []
        full_text = self.extracted.full_text
        
        for pattern in metric_patterns:
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0] if match else ""
                # Get context around the metric
                match_str = str(match)
                idx = full_text.find(match_str)
                if idx > 0:
                    context_start = max(0, idx - 50)
                    context_end = min(len(full_text), idx + len(match_str) + 50)
                    context = full_text[context_start:context_end].strip()
                    if context not in metrics:
                        metrics.append(context)
        
        self.organized.performance_metrics = metrics[:15]  # Top 15
    
    def _extract_limitations(self):
        """Extract limitations and assumptions."""
        limitation_keywords = [
            'limitation', 'assumption', 'constraint', 'restriction',
            'drawback', 'weakness', 'challenge', 'issue',
            'assumes', 'requires', 'depends on'
        ]
        
        limitations = []
        full_text = self.extracted.full_text
        
        for keyword in limitation_keywords:
            # Look for sentences containing limitation keywords
            pattern = rf'[^\.]*{keyword}[^\.]*\.'
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            limitations.extend([m.strip() for m in matches if len(m.strip()) > 20])
        
        self.organized.limitations = limitations[:15]  # Top 15
    
    def _extract_related_techniques(self):
        """Extract references to related techniques and methods."""
        related_keywords = [
            'similar to', 'compared to', 'based on', 'extends',
            'improves upon', 'alternative to', 'related work'
        ]
        
        related = []
        full_text = self.extracted.full_text
        
        for keyword in related_keywords:
            # Look for sentences mentioning related techniques
            pattern = rf'[^\.]*{keyword}[^\.]*\.'
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            related.extend([m.strip() for m in matches if len(m.strip()) > 20])
        
        self.organized.related_techniques = related[:15]  # Top 15
    
    def _extract_practical_applications(self):
        """Extract practical applications and use cases."""
        application_keywords = [
            'application', 'use case', 'scenario', 'example',
            'case study', 'real-world', 'practical', 'deployment'
        ]
        
        applications = []
        full_text = self.extracted.full_text
        
        for keyword in application_keywords:
            # Look for sentences containing application keywords
            pattern = rf'[^\.]*{keyword}[^\.]*\.'
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            applications.extend([m.strip() for m in matches if len(m.strip()) > 20])
        
        self.organized.practical_applications = applications[:15]  # Top 15
    
    def _extract_concepts_from_text(self, text: str) -> List[str]:
        """Extract key concepts from a text block."""
        # Look for capitalized terms and technical terms
        concepts = set()
        
        # Capitalized terms (likely proper nouns or technical terms)
        capitalized = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
        concepts.update([c for c in capitalized if len(c) > 3 and len(c) < 30])
        
        # Acronyms
        acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
        concepts.update(acronyms)
        
        return sorted(list(concepts))[:10]  # Top 10 per section


def organize_content(extracted_content: ExtractedContent) -> OrganizedContent:
    """
    Convenience function to organize extracted content.
    
    Args:
        extracted_content: ExtractedContent from PDF extractor
        
    Returns:
        OrganizedContent ready for MDC generation
    """
    organizer = ContentOrganizer(extracted_content)
    return organizer.organize()


if __name__ == "__main__":
    import sys
    from pdf_extractor import extract_pdf
    
    if len(sys.argv) < 2:
        print("Usage: python content_organizer.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    try:
        extracted = extract_pdf(pdf_path)
        organized = organize_content(extracted)
        
        print(f"Organized content from: {organized.metadata.title}")
        print(f"Key concepts: {len(organized.key_concepts)}")
        print(f"Code examples: {len(organized.code_examples)}")
        print(f"Formulas: {len(organized.formulas)}")
        print(f"Best practices: {len(organized.best_practices)}")
        print(f"Sections: {len(organized.sections)}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

