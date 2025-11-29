"""Extract a specific chapter from the book and prepare it for MDC conversion."""
import re
from pathlib import Path
from pdf_extractor import PDFExtractor

def extract_chapter(pdf_path, chapter_num, chapter_title):
    """Extract content for a specific chapter."""
    print(f"Extracting Chapter {chapter_num}: {chapter_title}")
    
    extractor = PDFExtractor(pdf_path)
    content = extractor.extract()
    
    # Find chapter boundaries
    lines = content.full_text.split('\n')
    chapter_start = None
    chapter_end = None
    
    # Find chapter start - look for actual chapter content, not TOC
    # Pattern 1: "CHAPTER" followed by title in all caps
    chapter_title_upper = chapter_title.upper()
    for i, line in enumerate(lines):
        if "CHAPTER" in line.upper() and chapter_title_upper in line.upper():
            # Check if next few lines contain chapter content (not TOC)
            if i + 5 < len(lines):
                next_lines = '\n'.join(lines[i:i+5]).lower()
                if 'introduction' in next_lines or 'what is' in next_lines or 'this chapter' in next_lines:
                    chapter_start = i
                    break
    
    if chapter_start is None:
        # Pattern 2: Look for chapter number followed by title
        for i, line in enumerate(lines):
            if re.match(rf'^Chapter\s+{chapter_num}[:]\s+{re.escape(chapter_title)}', line, re.IGNORECASE):
                # Check if this is actual content (has more text after) or TOC
                if i + 10 < len(lines):
                    # TOC entries are usually short, actual chapters have more content
                    next_text = '\n'.join(lines[i:i+10])
                    if len(next_text) > 200:  # Actual chapter has substantial content
                        chapter_start = i
                        break
    
    if chapter_start is None:
        # Pattern 3: Search for first section heading of the chapter
        first_section = None
        if chapter_num == 1:
            first_section = "What Is Artificial Intelligence"
        elif chapter_num == 2:
            first_section = "What is Machine Learning"
        elif chapter_num == 3:
            first_section = "What Is Classification"
        elif chapter_num == 4:
            first_section = "What Is Deep Learning"
        elif chapter_num == 5:
            first_section = "What Is an RNN"
        elif chapter_num == 6:
            first_section = "Working with NLP"
        
        if first_section:
            for i, line in enumerate(lines):
                if first_section.lower() in line.lower() and len(line) > 20:
                    # Go back a few lines to get chapter header
                    chapter_start = max(0, i - 10)
                    break
    
    if chapter_start is None:
        print(f"ERROR: Could not find start of Chapter {chapter_num}")
        return None
    
    # Find chapter end (next chapter or appendix)
    for i in range(chapter_start + 1, len(lines)):
        line = lines[i].strip()
        # Check if this is the next chapter
        if re.match(r'^Chapter\s+\d+[:]', line, re.IGNORECASE):
            chapter_end = i
            break
        # Check if this is an appendix
        if re.match(r'^Appendix\s+[A-Z]', line, re.IGNORECASE):
            chapter_end = i
            break
    
    if chapter_end is None:
        chapter_end = len(lines)
    
    # Extract chapter content
    chapter_lines = lines[chapter_start:chapter_end]
    chapter_text = '\n'.join(chapter_lines)
    
    print(f"Chapter {chapter_num} extracted: lines {chapter_start} to {chapter_end}")
    print(f"Content length: {len(chapter_text)} characters")
    
    # Save chapter content
    output_file = Path(pdf_path).parent / f"chapter_{chapter_num}_extracted.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(chapter_text)
    
    print(f"Chapter {chapter_num} saved to: {output_file}")
    
    return {
        'number': chapter_num,
        'title': chapter_title,
        'content': chapter_text,
        'start_line': chapter_start,
        'end_line': chapter_end
    }

if __name__ == "__main__":
    import sys
    
    pdf_path = "papers/Artificial Intelligence, Machine Learning, and Deep Learning.pdf"
    
    chapters = [
        (1, "Introduction to AI"),
        (2, "Introduction to Machine Learning"),
        (3, "Classifiers in Machine Learning"),
        (4, "Deep Learning Introduction"),
        (5, "Deep Learning: RNNs and LSTMs"),
        (6, "NLP and Reinforcement Learning"),
    ]
    
    if len(sys.argv) > 1:
        chapter_num = int(sys.argv[1])
        chapter_title = next((t for n, t in chapters if n == chapter_num), None)
        if chapter_title:
            extract_chapter(pdf_path, chapter_num, chapter_title)
        else:
            print(f"Unknown chapter number: {chapter_num}")
    else:
        # Extract all chapters
        for chapter_num, chapter_title in chapters:
            extract_chapter(pdf_path, chapter_num, chapter_title)
            print()

