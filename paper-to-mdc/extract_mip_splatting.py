#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pdf_extractor import extract_pdf

content = extract_pdf('papers/Mip Splatting Alias free 3D Gaussian Splatting.pdf')

print("="*80)
print("PAPER METADATA")
print("="*80)
print(f"Title: {content.metadata.title}")
print(f"Authors: {content.metadata.authors}")
print(f"Year: {content.metadata.year}")
print(f"DOI: {content.metadata.doi}")
print(f"\nPages: {len(content.pages)}")
print(f"Sections: {len(content.sections)}")
print(f"Formulas: {len(content.formulas)}")
print(f"Code blocks: {len(content.code_blocks)}")

print("\n" + "="*80)
print("ABSTRACT")
print("="*80)
print(content.metadata.abstract or "Not found in metadata")

print("\n" + "="*80)
print("SECTION TITLES")
print("="*80)
for i, section in enumerate(content.sections[:15], 1):
    print(f"{i}. {section['title'][:80]}")

print("\n" + "="*80)
print("FIRST 3000 CHARACTERS OF FULL TEXT")
print("="*80)
print(content.full_text[:3000])

print("\n" + "="*80)
print("FORMULAS FOUND")
print("="*80)
for i, formula in enumerate(content.formulas[:10], 1):
    print(f"{i}. {formula[:100]}")






