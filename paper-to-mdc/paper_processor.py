"""
Main Paper Processing Pipeline

This module orchestrates the complete pipeline from PDF extraction
to MDC file generation, including file placement and related MDC updates.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from pdf_extractor import extract_pdf, ExtractedContent
from content_organizer import organize_content, OrganizedContent


class PaperProcessor:
    """Main processor for converting papers to MDCs."""
    
    # Folder mapping keywords
    FOLDER_KEYWORDS = {
        'ai/': [
            'machine learning', 'neural network', 'deep learning', 'ai', 'artificial intelligence',
            'nlp', 'natural language', 'computer vision', 'transformer', 'attention',
            'reinforcement learning', 'classification', 'regression', 'model training'
        ],
        'engines/': [
            'engine', 'architecture', 'framework', 'system design', 'platform',
            'rendering', 'game engine', 'core system', 'component architecture'
        ],
        'backend/': [
            'backend', 'server', 'database', 'api', 'rest', 'graphql', 'authentication',
            'authorization', 'data processing', 'pipeline', 'etl', 'storage',
            'microservice', 'distributed system'
        ],
        'development-tools/': [
            'development', 'testing', 'debugging', 'build', 'deployment', 'ci/cd',
            'code organization', 'refactoring', 'code review', 'version control',
            'workflow', 'methodology', 'best practices'
        ],
        'science-maths/': [
            'mathematical', 'algorithm', 'computation', 'numerical', 'statistical',
            'analysis', 'optimization', 'linear algebra', 'calculus', 'geometry',
            'scientific computing', 'data analysis', 'simulation'
        ],
        'apis-integration/': [
            'api', 'integration', 'service', 'third-party', 'external', 'webhook',
            'sdk', 'client library', 'service communication', 'rpc'
        ],
        'web-design/': [
            'frontend', 'ui', 'ux', 'user interface', 'user experience', 'design',
            'react', 'vue', 'angular', 'javascript', 'typescript', 'css', 'html',
            'client-side', 'browser', 'web application'
        ]
    }
    
    def __init__(self, workspace_root: str = "."):
        """
        Initialize paper processor.
        
        Args:
            workspace_root: Root directory of the workspace (where MDC folders are)
        """
        self.workspace_root = Path(workspace_root)
        self.base_folders = [
            'ai', 'engines', 'backend', 'development-tools',
            'science-maths', 'apis-integration', 'web-design'
        ]
    
    def process_paper(self, pdf_path: str, output_folder: Optional[str] = None) -> Dict[str, any]:
        """
        Process a paper and generate MDC file.
        
        Args:
            pdf_path: Path to the PDF file
            output_folder: Optional specific folder to place MDC (auto-detected if None)
            
        Returns:
            Dictionary with processing results and file paths
        """
        print(f"Processing paper: {pdf_path}")
        
        # Step 1: Extract content from PDF
        print("Step 1: Extracting content from PDF...")
        extracted = extract_pdf(pdf_path)
        print(f"  - Extracted {len(extracted.pages)} pages")
        print(f"  - Found {len(extracted.sections)} sections")
        print(f"  - Found {len(extracted.code_blocks)} code blocks")
        
        # Step 2: Organize content
        print("Step 2: Organizing content...")
        organized = organize_content(extracted)
        print(f"  - Identified {len(organized.key_concepts)} key concepts")
        print(f"  - Found {len(organized.code_examples)} code examples")
        print(f"  - Found {len(organized.formulas)} formulas")
        
        # Step 3: Determine output folder
        print("Step 3: Determining output location...")
        if output_folder:
            target_folder = self.workspace_root / output_folder
        else:
            target_folder = self._determine_folder(organized)
        print(f"  - Target folder: {target_folder}")
        
        # Step 4: Generate folder name and filename based on key technique
        folder_name = self._generate_folder_name(organized)
        paper_folder = target_folder / folder_name
        filename = self._generate_filename(organized)
        mdc_path = paper_folder / filename
        print(f"  - Paper folder: {paper_folder}")
        print(f"  - Output file: {mdc_path}")
        
        # Step 5: Generate MDC content
        print("Step 4: Generating MDC content...")
        mdc_content = self._generate_mdc_content(organized)
        
        # Step 6: Create folder and write MDC file
        print("Step 5: Creating folder and writing MDC file...")
        paper_folder.mkdir(parents=True, exist_ok=True)
        with open(mdc_path, 'w', encoding='utf-8') as f:
            f.write(mdc_content)
        print(f"  - MDC file created: {mdc_path}")
        
        # Step 7: Generate and write README
        print("Step 6: Generating README...")
        readme_content = self._generate_readme(organized, folder_name, filename)
        readme_path = paper_folder / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"  - README created: {readme_path}")
        
        # Step 8: Identify related MDCs
        print("Step 7: Identifying related MDCs...")
        related_mdcs = self._find_related_mdcs(organized)
        print(f"  - Found {len(related_mdcs)} related MDCs")
        
        return {
            'success': True,
            'mdc_path': str(mdc_path),
            'readme_path': str(readme_path),
            'paper_folder': str(paper_folder),
            'target_folder': str(target_folder),
            'related_mdcs': related_mdcs,
            'metadata': {
                'title': organized.metadata.title,
                'authors': organized.metadata.authors,
                'year': organized.metadata.year
            },
            'stats': {
                'sections': len(organized.sections),
                'code_examples': len(organized.code_examples),
                'formulas': len(organized.formulas),
                'key_concepts': len(organized.key_concepts)
            }
        }
    
    def _determine_folder(self, organized: OrganizedContent) -> Path:
        """Determine the appropriate folder for the MDC based on content."""
        # Analyze key concepts and content
        text_to_analyze = " ".join([
            organized.abstract,
            " ".join(organized.key_concepts),
            organized.methodology.content
        ]).lower()
        
        # Score each folder based on keyword matches
        folder_scores = {}
        for folder, keywords in self.FOLDER_KEYWORDS.items():
            score = sum(1 for keyword in keywords if keyword.lower() in text_to_analyze)
            folder_scores[folder] = score
        
        # Get folder with highest score
        if folder_scores:
            best_folder = max(folder_scores, key=folder_scores.get)
            if folder_scores[best_folder] > 0:
                return self.workspace_root / best_folder.rstrip('/')
        
        # Default to 'ai/' if no clear match
        return self.workspace_root / 'ai'
    
    def _extract_key_technique_name(self, organized: OrganizedContent) -> str:
        """Extract the key technique/concept name from paper content for filename."""
        # Try to identify the main technique from various sources
        technique_candidates = []
        
        # 1. Extract from key concepts (prioritize technical terms)
        if organized.key_concepts:
            for concept in organized.key_concepts[:5]:  # Top 5 concepts
                # Look for technical terms (capitalized, acronyms, compound terms)
                if len(concept) > 3 and len(concept) < 30:
                    # Prefer acronyms or technical compound terms
                    if concept.isupper() or '-' in concept or any(c.isupper() for c in concept):
                        technique_candidates.append(concept)
                    else:
                        technique_candidates.append(concept)
        
        # 2. Extract from title (look for key terms after common words)
        title = organized.metadata.title or ""
        if title:
            # Remove common paper title words
            title_lower = title.lower()
            # Look for patterns like "A [Technique] Approach", "[Technique]: [Description]", etc.
            patterns = [
                r'(?:^|:\s)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',  # Capitalized terms
                r'([A-Z]{2,})',  # Acronyms
                r'([a-z]+(?:-[a-z]+)+)',  # Hyphenated terms
            ]
            for pattern in patterns:
                matches = re.findall(pattern, title)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[0] if match else ""
                    if match and len(match) > 3 and len(match) < 30:
                        technique_candidates.append(match)
        
        # 3. Extract from abstract (look for technique mentions)
        if organized.abstract:
            abstract_lower = organized.abstract.lower()
            # Look for phrases like "we propose", "we introduce", "we present"
            intro_patterns = [
                r'(?:propose|introduce|present|develop|design)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
                r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:method|approach|technique|algorithm|framework|system)',
            ]
            for pattern in intro_patterns:
                matches = re.findall(pattern, organized.abstract)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[0] if match else ""
                    if match and len(match) > 3 and len(match) < 30:
                        technique_candidates.append(match)
        
        # 4. Extract from methodology section
        if organized.methodology.content:
            # Look for algorithm names, method names
            method_patterns = [
                r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:algorithm|method|technique)',
                r'(?:Algorithm|Method|Technique)\s+(\d+):\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            ]
            for pattern in method_patterns:
                matches = re.findall(pattern, organized.methodology.content)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[-1] if match else ""
                    if match and len(match) > 3 and len(match) < 30:
                        technique_candidates.append(match)
        
        # Select best candidate
        if technique_candidates:
            # Prefer shorter, more technical-sounding names
            # Remove duplicates while preserving order
            seen = set()
            unique_candidates = []
            for candidate in technique_candidates:
                candidate_lower = candidate.lower()
                if candidate_lower not in seen and candidate_lower not in ['the', 'and', 'for', 'with', 'using']:
                    seen.add(candidate_lower)
                    unique_candidates.append(candidate)
            
            if unique_candidates:
                # Return the first good candidate (prioritize acronyms and technical terms)
                for candidate in unique_candidates:
                    if candidate.isupper() or len(candidate.split()) <= 3:
                        return candidate
                return unique_candidates[0]
        
        # Fallback: use a cleaned version of the title
        return None
    
    def _generate_folder_name(self, organized: OrganizedContent) -> str:
        """Generate a valid folder name based on key technique from paper content."""
        # Try to extract key technique name
        technique_name = self._extract_key_technique_name(organized)
        
        if technique_name:
            base_name = technique_name
        else:
            # Fallback to paper title
            title = organized.metadata.title or "paper-technique"
            base_name = title
        
        # Clean the name
        folder_name = base_name.lower()
        
        # Remove special characters
        folder_name = re.sub(r'[^\w\s-]', '', folder_name)
        
        # Replace spaces with hyphens
        folder_name = re.sub(r'\s+', '-', folder_name)
        
        # Remove multiple hyphens
        folder_name = re.sub(r'-+', '-', folder_name)
        
        # Limit length
        if len(folder_name) > 50:
            folder_name = folder_name[:50]
        
        # Remove trailing hyphens
        folder_name = folder_name.rstrip('-')
        
        # Ensure it's not empty
        if not folder_name:
            folder_name = "paper-technique"
        
        return folder_name
    
    def _generate_filename(self, organized: OrganizedContent) -> str:
        """Generate a valid filename based on key technique from paper content."""
        # Use same logic as folder name but add extension
        filename = self._generate_folder_name(organized)
        
        # Add extension
        if not filename.endswith('.mdc'):
            filename += '.mdc'
        
        return filename
    
    def _generate_mdc_content(self, organized: OrganizedContent) -> str:
        """Generate MDC content from organized content."""
        lines = []
        
        # Frontmatter
        lines.append("---")
        lines.append("alwaysApply: false")
        lines.append("---")
        lines.append("")
        
        # Title
        title = organized.metadata.title or "Scientific Paper Technique"
        lines.append(f"# {title}")
        lines.append("")
        
        # Paper Metadata
        lines.append("## Paper Metadata")
        if organized.metadata.title:
            lines.append(f"- **Title:** {organized.metadata.title}")
        if organized.metadata.authors:
            lines.append(f"- **Authors:** {', '.join(organized.metadata.authors)}")
        if organized.metadata.year:
            lines.append(f"- **Year:** {organized.metadata.year}")
        if organized.metadata.doi:
            lines.append(f"- **DOI/URL:** {organized.metadata.doi}")
        lines.append("")
        
        # Abstract / Summary
        if organized.abstract:
            lines.append("## Abstract / Summary")
            lines.append("")
            lines.append(organized.abstract)
            lines.append("")
        
        # Key Concepts and Techniques
        if organized.key_concepts:
            lines.append("## Key Concepts and Techniques")
            lines.append("")
            for concept in organized.key_concepts:
                lines.append(f"- {concept}")
            lines.append("")
        
        # Methodology and Algorithms
        if organized.methodology.content:
            lines.append("## Methodology and Algorithms")
            lines.append("")
            lines.append(organized.methodology.content)
            lines.append("")
            
            # Add formulas from methodology
            if organized.methodology.formulas:
                lines.append("### Mathematical Foundations")
                lines.append("")
                for formula in organized.methodology.formulas:
                    # Ensure LaTeX format
                    if not formula.startswith('$'):
                        formula = f"${formula}$"
                    lines.append(f"$${formula}$$")
                    lines.append("")
        
        # Implementation Patterns
        if organized.implementation_patterns:
            lines.append("## Implementation Patterns")
            lines.append("")
            for pattern in organized.implementation_patterns:
                lines.append(f"- {pattern}")
            lines.append("")
        
        # Code Examples and Snippets
        if organized.code_examples:
            lines.append("## Code Examples and Snippets")
            lines.append("")
            for i, code_block in enumerate(organized.code_examples, 1):
                language = code_block.get('language', 'unknown')
                code = code_block.get('code', '')
                if code:
                    lines.append(f"### Code Example {i}")
                    lines.append("")
                    lines.append(f"```{language}")
                    lines.append(code)
                    lines.append("```")
                    lines.append("")
        
        # Mathematical Foundations (all formulas)
        if organized.formulas:
            lines.append("## Mathematical Foundations")
            lines.append("")
            for formula in organized.formulas:
                # Ensure LaTeX format
                if not formula.startswith('$'):
                    formula = f"${formula}$"
                lines.append(f"$${formula}$$")
                lines.append("")
        
        # Best Practices and Recommendations
        if organized.best_practices:
            lines.append("## Best Practices and Recommendations")
            lines.append("")
            for practice in organized.best_practices:
                lines.append(f"- {practice}")
            lines.append("")
        
        # Performance Metrics and Benchmarks
        if organized.performance_metrics:
            lines.append("## Performance Metrics and Benchmarks")
            lines.append("")
            for metric in organized.performance_metrics:
                lines.append(f"- {metric}")
            lines.append("")
        
        # Limitations and Assumptions
        if organized.limitations:
            lines.append("## Limitations and Assumptions")
            lines.append("")
            for limitation in organized.limitations:
                lines.append(f"- {limitation}")
            lines.append("")
        
        # Related Techniques and References
        if organized.related_techniques:
            lines.append("## Related Techniques and References")
            lines.append("")
            for technique in organized.related_techniques:
                lines.append(f"- {technique}")
            lines.append("")
        
        # Practical Applications
        if organized.practical_applications:
            lines.append("## Practical Applications")
            lines.append("")
            for application in organized.practical_applications:
                lines.append(f"- {application}")
            lines.append("")
        
        # Additional Sections
        for section in organized.sections:
            if section.title.lower() not in ['abstract', 'introduction', 'methodology']:
                lines.append(f"## {section.title}")
                lines.append("")
                lines.append(section.content)
                lines.append("")
        
        return "\n".join(lines)
    
    def _generate_readme(self, organized: OrganizedContent, folder_name: str, mdc_filename: str) -> str:
        """Generate README.md for the paper folder."""
        title = organized.metadata.title or "Scientific Paper Technique"
        authors = ", ".join(organized.metadata.authors) if organized.metadata.authors else "Unknown"
        year = organized.metadata.year or "Unknown"
        
        lines = []
        lines.append(f"# {title}")
        lines.append("")
        lines.append(f"**Authors:** {authors}  ")
        lines.append(f"**Year:** {year}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## What is This?")
        lines.append("")
        lines.append(f"This folder contains an MDC (Markdown Cursor) cheat sheet derived from the scientific paper: **{title}**.")
        lines.append("")
        lines.append("An MDC file is a comprehensive reference document that Cursor AI can use to understand and implement the techniques, patterns, and methodologies described in the original paper. Think of it as a condensed, actionable version of the paper optimized for code generation and implementation.")
        lines.append("")
        lines.append("## Contents")
        lines.append("")
        lines.append(f"- **`{mdc_filename}`** - The main MDC cheat sheet containing:")
        lines.append("  - Paper metadata and abstract")
        lines.append("  - Key concepts and techniques")
        lines.append("  - Methodology and algorithms")
        lines.append("  - Implementation patterns")
        lines.append("  - Code examples and snippets")
        lines.append("  - Mathematical foundations (formulas)")
        lines.append("  - Best practices and recommendations")
        lines.append("  - Performance metrics and benchmarks")
        lines.append("  - Limitations and assumptions")
        lines.append("  - Related techniques and references")
        lines.append("  - Practical applications")
        lines.append("")
        lines.append("- **`README.md`** - This file, explaining how to use the MDC")
        lines.append("")
        lines.append("## How It Works")
        lines.append("")
        lines.append("The MDC file was automatically generated from the scientific paper using a comprehensive extraction process that:")
        lines.append("")
        lines.append("1. **Reads the entire paper** - Performs multiple passes to ensure complete coverage")
        lines.append("2. **Extracts all technical content** - Code examples, algorithms, formulas, and patterns")
        lines.append("3. **Organizes information** - Structures content into logical sections")
        lines.append("4. **Preserves technical details** - Maintains accuracy of code, formulas, and implementation details")
        lines.append("5. **Creates actionable reference** - Formats content for easy use in development")
        lines.append("")
        lines.append("The extraction process follows strict protocols to ensure nothing is missed, making the MDC a reliable \"Source of Truth\" for the paper's content.")
        lines.append("")
        lines.append("## How to Use This When Building")
        lines.append("")
        lines.append("### Method 1: Reference in Cursor Chat")
        lines.append("")
        lines.append("Explicitly mention the MDC file in your Cursor conversation:")
        lines.append("")
        lines.append("```")
        lines.append(f"\"Use the techniques from {folder_name}/{mdc_filename} to implement [feature]\"")
        lines.append(f"\"Follow the patterns in {folder_name}/{mdc_filename} for [use case]\"")
        lines.append(f"\"Apply the methodology from {folder_name}/{mdc_filename}\"")
        lines.append("```")
        lines.append("")
        lines.append("### Method 2: Open in Cursor")
        lines.append("")
        lines.append("1. **Open the MDC file** in Cursor's editor")
        lines.append("2. Cursor will automatically include it in the context for that conversation")
        lines.append("3. The AI will reference the file's patterns and rules when generating code")
        lines.append("")
        lines.append("### Method 3: Add to Cursor Rules")
        lines.append("")
        lines.append("1. **Copy the file path** (e.g., `{folder_name}/{mdc_filename}`)")
        lines.append("2. **Add to `.cursorrules`** file in your project:")
        lines.append("")
        lines.append("```")
        lines.append(f"@{folder_name}/{mdc_filename}")
        lines.append("```")
        lines.append("")
        lines.append("### Method 4: Use Specific Sections")
        lines.append("")
        lines.append("You can reference specific sections of the MDC:")
        lines.append("")
        lines.append("- **Code Examples** - \"Use the code examples from the MDC to implement [feature]\"")
        lines.append("- **Implementation Patterns** - \"Follow the implementation patterns section\"")
        lines.append("- **Best Practices** - \"Apply the best practices from the MDC\"")
        lines.append("- **Mathematical Foundations** - \"Use the formulas from the MDC for calculations\"")
        lines.append("")
        lines.append("## Key Concepts")
        lines.append("")
        if organized.key_concepts:
            for concept in organized.key_concepts[:10]:  # Top 10
                lines.append(f"- {concept}")
        else:
            lines.append("- (Key concepts will be listed here)")
        lines.append("")
        lines.append("## Quick Start")
        lines.append("")
        lines.append("1. **Read the MDC file** to understand the technique")
        lines.append("2. **Review the code examples** to see implementations")
        lines.append("3. **Check best practices** before starting implementation")
        lines.append("4. **Reference the MDC** in Cursor when building features")
        lines.append("5. **Follow the methodology** described in the MDC")
        lines.append("")
        lines.append("## Related Resources")
        lines.append("")
        if organized.metadata.doi:
            lines.append(f"- **Original Paper DOI:** {organized.metadata.doi}")
        lines.append(f"- **Paper Title:** {title}")
        lines.append("")
        lines.append("## Notes")
        lines.append("")
        lines.append("- This MDC is automatically generated and should be verified against the original paper for critical implementations")
        lines.append("- The MDC focuses on practical implementation details and may not include all theoretical background")
        lines.append("- Code examples are extracted from the paper and may need adaptation for your specific use case")
        lines.append("- Always review best practices and limitations before implementation")
        lines.append("")
        
        return "\n".join(lines)
    
    def _find_related_mdcs(self, organized: OrganizedContent) -> List[str]:
        """Find existing MDCs that might be related to this paper."""
        related = []
        
        # Search for MDCs with similar keywords
        keywords = organized.key_concepts[:10]  # Top 10 concepts
        
        for folder_name in self.base_folders:
            folder_path = self.workspace_root / folder_name
            if folder_path.exists():
                # Search in subdirectories too
                for mdc_file in folder_path.rglob("*.mdc"):
                    # Read first few lines to check for keyword matches
                    try:
                        with open(mdc_file, 'r', encoding='utf-8') as f:
                            content = f.read(2000).lower()  # First 2000 chars
                            for keyword in keywords:
                                if keyword.lower() in content:
                                    related.append(str(mdc_file))
                                    break
                    except Exception:
                        continue
        
        return related


def process_paper(pdf_path: str, workspace_root: str = ".", output_folder: Optional[str] = None) -> Dict[str, any]:
    """
    Convenience function to process a paper.
    
    Args:
        pdf_path: Path to the PDF file
        workspace_root: Root directory of the workspace
        output_folder: Optional specific folder to place MDC
        
    Returns:
        Dictionary with processing results
    """
    processor = PaperProcessor(workspace_root)
    return processor.process_paper(pdf_path, output_folder)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python paper_processor.py <path_to_pdf> [workspace_root] [output_folder]")
        print("Example: python paper_processor.py papers/attention-is-all-you-need.pdf . ai/")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    workspace_root = sys.argv[2] if len(sys.argv) > 2 else "."
    output_folder = sys.argv[3] if len(sys.argv) > 3 else None
    
    try:
        result = process_paper(pdf_path, workspace_root, output_folder)
        
        print("\n" + "="*60)
        print("Processing Complete!")
        print("="*60)
        print(f"MDC created: {result['mdc_path']}")
        print(f"Title: {result['metadata']['title']}")
        print(f"Related MDCs found: {len(result['related_mdcs'])}")
        if result['related_mdcs']:
            print("\nConsider updating these related MDCs:")
            for mdc in result['related_mdcs']:
                print(f"  - {mdc}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

