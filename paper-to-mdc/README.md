# Scientific Paper to MDC Conversion System

A comprehensive system for converting scientific papers (PDFs) about coding techniques and building methods into MDC (Markdown Cursor) cheat sheets. This system ensures complete paper coverage, accurate extraction, and proper file organization.

## Overview

This system provides:
- **Automated PDF extraction** - Extracts text, metadata, code blocks, and formulas from PDF papers
- **Content organization** - Structures extracted content into logical sections
- **MDC generation** - Creates comprehensive MDC cheat sheets from papers
- **Smart file placement** - Automatically determines the correct folder based on paper content
- **Folder structure** - Each MDC gets its own folder with a README for easy reference

## What is an MDC?

An MDC (Markdown Cursor) file is a comprehensive reference document that Cursor AI can use to understand and implement techniques, patterns, and methodologies. Think of it as a condensed, actionable version of a scientific paper optimized for code generation and implementation.

## System Components

### 1. Rule Book (`scientific-paper-to-mdc-rules.mdc`)
The main rule book that guides AI through the complete paper processing workflow. It enforces:
- **Mandatory multi-pass reading** - Ensures complete paper coverage
- **Structured extraction** - Systematic content extraction from all sections
- **Quality assurance** - Verification checklists before MDC creation
- **File organization** - Smart placement in appropriate folders

### 2. PDF Extractor (`pdf_extractor.py`)
Extracts content from PDF files:
- Text extraction with structure preservation
- Metadata extraction (title, authors, year, DOI)
- Section identification
- Code block detection
- Formula identification
- Table extraction

### 3. Content Organizer (`content_organizer.py`)
Organizes extracted content:
- Structures content by paper sections
- Identifies key concepts and techniques
- Organizes code examples by language
- Extracts best practices and limitations
- Identifies performance metrics
- Finds related techniques

### 4. Paper Processor (`paper_processor.py`)
Main orchestration script:
- Coordinates the entire pipeline
- Generates MDC content
- Creates folder structure
- Generates README files
- Identifies related MDCs

## Installation

### Prerequisites
- Python 3.8 or higher
- PDF extraction library (pdfplumber recommended)

### Install Dependencies

```bash
pip install pdfplumber
```

Or if you prefer PyPDF2 (fallback):

```bash
pip install PyPDF2
```

## Usage

### Basic Usage

```bash
python paper_processor.py <path_to_pdf> [workspace_root] [output_folder]
```

**Example:**
```bash
python paper_processor.py papers/attention-is-all-you-need.pdf . ai/
```

### Parameters

- `<path_to_pdf>` - Path to the PDF file to process (required)
- `[workspace_root]` - Root directory of your workspace (default: current directory)
- `[output_folder]` - Optional specific folder (e.g., `ai/`, `engines/`). If not specified, the system will auto-detect based on paper content.

### Processing Steps

The system performs the following steps:

1. **PDF Extraction** - Extracts all text, metadata, and structure from the PDF
2. **Content Organization** - Organizes content into logical sections
3. **Folder Determination** - Analyzes content to determine the appropriate folder
4. **MDC Generation** - Creates the MDC file with all extracted content
5. **Folder Creation** - Creates a dedicated folder for the paper
6. **README Generation** - Creates a README explaining how to use the MDC
7. **Related MDC Identification** - Finds existing MDCs that might be related

## Output Structure

Each processed paper creates a folder structure like this:

```
ai/
└── attention-mechanism-transformer/
    ├── attention-mechanism-transformer.mdc
    └── README.md
```

### MDC File Contents

The MDC file contains:
- Paper metadata (title, authors, year, DOI)
- Abstract/Summary
- Key concepts and techniques
- Methodology and algorithms
- Implementation patterns
- Code examples and snippets
- Mathematical foundations (formulas)
- Best practices and recommendations
- Performance metrics and benchmarks
- Limitations and assumptions
- Related techniques and references
- Practical applications

### README File Contents

Each README explains:
- **What it is** - Description of the MDC and its purpose
- **How it works** - Explanation of the extraction process
- **How to use it when building** - Instructions for using the MDC in Cursor
- Key concepts from the paper
- Quick start guide
- Related resources

## Using MDCs in Cursor

### Method 1: Reference in Cursor Chat

Explicitly mention the MDC file in your Cursor conversation:

```
"Use the techniques from ai/attention-mechanism-transformer/attention-mechanism-transformer.mdc to implement a transformer model"
"Follow the patterns in engines/rendering-engine/rendering-engine.mdc for the graphics system"
```

### Method 2: Open in Cursor

1. Open the MDC file in Cursor's editor
2. Cursor will automatically include it in the context
3. The AI will reference the file's patterns when generating code

### Method 3: Add to Cursor Rules

Add the MDC to your `.cursorrules` file:

```
@ai/attention-mechanism-transformer/attention-mechanism-transformer.mdc
```

### Method 4: Use Specific Sections

Reference specific sections:

- "Use the code examples from the MDC to implement [feature]"
- "Follow the implementation patterns section"
- "Apply the best practices from the MDC"

## Folder Mapping

The system automatically maps papers to folders based on content:

- **`ai/`** - Machine learning, AI algorithms, neural networks, NLP, computer vision
- **`engines/`** - System architectures, engine designs, frameworks
- **`backend/`** - Backend patterns, databases, APIs, server-side architectures
- **`development-tools/`** - Development methodologies, testing, debugging, workflows
- **`science-maths/`** - Mathematical algorithms, computational methods, statistics
- **`apis-integration/`** - API integration patterns, third-party services
- **`web-design/`** - Frontend techniques, UI/UX patterns, client-side architectures

## Manual Processing (AI-Assisted)

For best results, use the rule book (`scientific-paper-to-mdc-rules.mdc`) with Cursor AI:

1. **Reference the rule book** in Cursor:
   ```
   "Use paper-to-mdc/scientific-paper-to-mdc-rules.mdc to process this paper"
   ```

2. **Follow the multi-pass reading protocol**:
   - Pass 1: Full paper structure scan
   - Pass 2: Section-by-section detailed extraction
   - Pass 3: Cross-reference validation

3. **Create the MDC** following the template in the rule book

4. **Create the folder structure** with MDC and README

5. **Update related MDCs** if applicable

## Quality Assurance

The system includes multiple quality checks:

- **Completeness** - Verifies all sections are extracted
- **Accuracy** - Validates code examples and formulas
- **Organization** - Ensures proper folder structure
- **Formatting** - Checks markdown syntax and LaTeX formulas

## Best Practices

1. **Always use the rule book** - It ensures complete coverage
2. **Verify extraction** - Review the generated MDC against the original paper
3. **Update related MDCs** - Add cross-references to related techniques
4. **Keep READMEs updated** - Ensure they accurately describe the MDC
5. **Test the MDC** - Use it in Cursor to verify it works as expected

## Troubleshooting

### PDF Extraction Issues

If extraction fails:
- Ensure the PDF is not password-protected
- Check that pdfplumber or PyPDF2 is installed
- Try a different PDF if the format is unusual

### Content Organization Issues

If content is not well-organized:
- Review the paper structure
- Manually adjust the MDC if needed
- Check that all sections were extracted

### Folder Placement Issues

If the MDC is placed in the wrong folder:
- Manually move it to the correct location
- Update the README with the correct path
- Consider the paper's primary focus when deciding placement

## Contributing

When adding new papers:
1. Place PDFs in the `papers/` folder
2. Process using the system
3. Review and verify the generated MDC
4. Update related MDCs if needed

## License

This system is part of the Cursor Rules workspace and follows the same licensing terms.

## Support

For issues or questions:
1. Review the rule book (`scientific-paper-to-mdc-rules.mdc`)
2. Check the generated README in each paper folder
3. Verify the paper was processed completely

---

**Remember:** The goal is to create comprehensive, accurate MDCs that serve as "Source of Truth" documents for implementing techniques from scientific papers. Quality and completeness are more important than speed.

