#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io
import json

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pdf_extractor import extract_pdf

content = extract_pdf('papers/Mip Splatting Alias free 3D Gaussian Splatting.pdf')

# Save full extracted content to JSON for processing
output = {
    'metadata': {
        'title': content.metadata.title,
        'authors': content.metadata.authors,
        'year': content.metadata.year,
        'doi': content.metadata.doi,
        'abstract': content.metadata.abstract
    },
    'pages': len(content.pages),
    'sections': [{'title': s['title'], 'content': s['content'][:500]} for s in content.sections],
    'formulas': content.formulas,
    'code_blocks': content.code_blocks,
    'tables': len(content.tables),
    'full_text': content.full_text
}

# Write to file
with open('mip_splatting_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Extracted content saved. Full text length: {len(content.full_text)} characters")
print(f"Sections: {len(content.sections)}")
print(f"Formulas: {len(content.formulas)}")




