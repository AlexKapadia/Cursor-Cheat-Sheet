"""Extract and analyze the structure of the AI/ML/DL textbook."""
import sys
from pathlib import Path
from pdf_extractor import PDFExtractor

def extract_book_structure(pdf_path):
    """Extract content and identify chapters."""
    print(f"Extracting content from: {pdf_path}")
    extractor = PDFExtractor(pdf_path)
    content = extractor.extract()
    
    print(f"\nExtraction Summary:")
    print(f"- Pages: {len(content.pages)}")
    print(f"- Sections identified: {len(content.sections)}")
    print(f"- Code blocks: {len(content.code_blocks)}")
    print(f"- Formulas: {len(content.formulas)}")
    print(f"\nTitle: {content.metadata.title}")
    print(f"Authors: {content.metadata.authors}")
    print(f"Year: {content.metadata.year}")
    
    # Identify chapters
    print(f"\n=== Identifying Chapters ===")
    chapter_patterns = [
        r'^Chapter\s+(\d+)[:\s]+(.+)$',
        r'^CHAPTER\s+(\d+)[:\s]+(.+)$',
        r'^\s*(\d+)\.\s*([A-Z][^\n]+)$',  # Numbered sections that might be chapters
    ]
    
    import re
    lines = content.full_text.split('\n')
    chapters = []
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        for pattern in chapter_patterns:
            match = re.match(pattern, line_stripped, re.IGNORECASE)
            if match:
                chapter_num = match.group(1)
                chapter_title = match.group(2).strip()
                # Filter out false positives (too short, common words)
                if len(chapter_title) > 5 and chapter_title.lower() not in ['introduction', 'abstract', 'preface']:
                    chapters.append({
                        'number': chapter_num,
                        'title': chapter_title,
                        'line': i,
                        'page': _find_page_for_line(content, i)
                    })
                    break
    
    # Remove duplicates and sort
    seen = set()
    unique_chapters = []
    for ch in chapters:
        key = (ch['number'], ch['title'].lower())
        if key not in seen:
            seen.add(key)
            unique_chapters.append(ch)
    
    unique_chapters.sort(key=lambda x: (int(x['number']) if x['number'].isdigit() else 999, x['line']))
    
    print(f"\nFound {len(unique_chapters)} chapters:")
    for ch in unique_chapters[:20]:  # Show first 20
        print(f"  Chapter {ch['number']}: {ch['title']} (page ~{ch['page']})")
    
    # Save full text for analysis
    output_file = Path(pdf_path).parent / "extracted_book_text.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content.full_text)
    print(f"\nFull text saved to: {output_file}")
    
    # Save chapter structure
    structure_file = Path(pdf_path).parent / "book_structure.txt"
    with open(structure_file, 'w', encoding='utf-8') as f:
        f.write("CHAPTER STRUCTURE\n")
        f.write("=" * 50 + "\n\n")
        for ch in unique_chapters:
            f.write(f"Chapter {ch['number']}: {ch['title']}\n")
            f.write(f"  Page: ~{ch['page']}\n")
            f.write(f"  Line: {ch['line']}\n\n")
    print(f"Chapter structure saved to: {structure_file}")
    
    return content, unique_chapters

def _find_page_for_line(content, line_num):
    """Find which page a line number corresponds to."""
    current_line = 0
    for page_info in content.pages:
        page_lines = len(page_info['text'].split('\n'))
        if current_line + page_lines > line_num:
            return page_info['page_number']
        current_line += page_lines
    return 1

if __name__ == "__main__":
    pdf_path = "papers/Artificial Intelligence, Machine Learning, and Deep Learning.pdf"
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    
    extract_book_structure(pdf_path)

