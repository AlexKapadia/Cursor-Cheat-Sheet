# Report Data Extraction Rules

## Overview
This document provides comprehensive guidelines for extracting data from reports with accuracy, consistency, and professionalism. Follow these rules to ensure data integrity and analytical reliability.

## Pre-Extraction Planning

### 1. Understand the Report Structure
- **Identify report type**: Financial, operational, sales, marketing, research, etc.
- **Map the layout**: Headers, sections, tables, charts, footnotes
- **Note data sources**: Primary sources, calculated fields, derived metrics
- **Document metadata**: Report date, period covered, version, author/organization

### 2. Define Extraction Objectives
- **Clarify purpose**: What questions need to be answered?
- **Identify key metrics**: Which data points are critical?
- **Set scope boundaries**: What time periods, categories, or segments?
- **Determine output format**: Database, spreadsheet, structured data format

### 3. Assess Data Quality
- **Check completeness**: Are all expected sections present?
- **Verify consistency**: Do formats match across sections?
- **Identify anomalies**: Missing values, outliers, formatting inconsistencies
- **Review data lineage**: Understand how data was calculated or aggregated

## Extraction Methodology

### 1. Systematic Approach

#### Step-by-Step Process
1. **Initial Scan**: Read entire report to understand context
2. **Section Identification**: Mark all data-containing sections
3. **Schema Design**: Create data structure before extraction
4. **Extraction**: Extract data systematically section by section
5. **Validation**: Cross-check extracted data against source
6. **Documentation**: Record assumptions, transformations, and issues

### 2. Data Identification Rules

#### Primary Data Elements
- **Quantitative metrics**: Numbers, percentages, ratios, counts
- **Categorical data**: Labels, classifications, segments
- **Temporal data**: Dates, time periods, timestamps
- **Dimensional data**: Hierarchies, groupings, breakdowns
- **Contextual data**: Notes, definitions, methodology

#### Secondary Data Elements
- **Calculated fields**: Derived metrics, formulas
- **Aggregations**: Sums, averages, totals
- **Comparisons**: Period-over-period, year-over-year
- **Benchmarks**: Targets, goals, industry standards

### 3. Extraction Techniques

#### For Tabular Data
- **Identify table boundaries**: Headers, footers, row/column delimiters
- **Map column headers**: Understand what each column represents
- **Handle merged cells**: Note when cells span multiple rows/columns
- **Extract row data**: Maintain relationships between dimensions and metrics
- **Preserve formatting**: Note units, currency, date formats

#### For Text-Based Data
- **Use pattern recognition**: Identify consistent patterns in text
- **Extract structured info**: Dates, names, numbers embedded in text
- **Parse narratives**: Extract key facts, findings, conclusions
- **Maintain context**: Link extracted data to surrounding text

#### For Chart/Graph Data
- **Read chart titles and labels**: Understand what is being visualized
- **Extract data points**: Series names, values, categories
- **Note chart type**: Bar, line, pie, scatter, etc.
- **Capture legends**: Understand what each element represents
- **Document scale**: Axis ranges, units, intervals

## Accuracy Standards

### 1. Data Validation

#### Cross-Reference Checks
- **Internal consistency**: Do numbers add up correctly?
- **Formula verification**: Recalculate derived metrics when possible
- **Period alignment**: Ensure time periods match across sections
- **Unit consistency**: Verify all metrics use same units/currency

#### Quality Checks
- **Completeness**: All expected data points extracted
- **Precision**: Correct number of decimal places maintained
- **Format consistency**: Dates, numbers, text formatted uniformly
- **No data loss**: Nothing skipped or omitted

### 2. Error Prevention

#### Common Pitfalls to Avoid
- **Misreading numbers**: 0 vs O, 1 vs l, decimal placement
- **Missing context**: Extracting numbers without units or labels
- **Incorrect aggregation**: Double-counting or missing subtotals
- **Format misinterpretation**: Date formats, number formats, currency
- **Section confusion**: Extracting from wrong section or period

#### Verification Methods
- **Spot checks**: Randomly verify 10-20% of extracted data
- **Range checks**: Ensure values are within expected ranges
- **Logic checks**: Verify relationships make sense (e.g., parts sum to whole)
- **Peer review**: Have another analyst review critical extractions

### 3. Handling Ambiguities

#### When Data is Unclear
- **Document assumptions**: Record what you assumed and why
- **Flag uncertainties**: Mark data points that need clarification
- **Seek clarification**: Contact report author when possible
- **Use conservative estimates**: When forced to estimate, be conservative
- **Note limitations**: Document what couldn't be extracted and why

## Technical Best Practices

### 1. Data Structure Design

#### Schema Considerations
- **Normalize data**: Avoid redundancy, maintain referential integrity
- **Use appropriate data types**: Numbers, text, dates, booleans
- **Create unique identifiers**: Primary keys for records
- **Maintain relationships**: Foreign keys, hierarchies, groupings
- **Preserve metadata**: Source, extraction date, version

#### Naming Conventions
- **Clear, descriptive names**: Column/field names should be self-explanatory
- **Consistent formatting**: Use same naming style throughout
- **Avoid abbreviations**: Unless universally understood
- **Include units**: When relevant (e.g., "Revenue_USD", "Temperature_Celsius")

### 2. Extraction Tools and Methods

#### Manual Extraction
- **Use templates**: Pre-designed forms for consistent extraction
- **Double-entry**: Enter critical data twice and compare
- **Checklists**: Ensure all required fields completed
- **Time stamps**: Record when each section was extracted

#### Automated Extraction
- **OCR for PDFs**: Use optical character recognition when needed
- **Parsing scripts**: Write code to extract structured data
- **API integration**: When reports are available via API
- **Validation rules**: Build checks into automated processes

### 3. Data Transformation

#### Standardization
- **Unit conversion**: Convert to standard units (e.g., all to USD)
- **Date normalization**: Use consistent date format (YYYY-MM-DD)
- **Text cleaning**: Remove extra spaces, standardize capitalization
- **Categorical mapping**: Map variations to standard categories

#### Enrichment
- **Add calculated fields**: Derived metrics, ratios, percentages
- **Create hierarchies**: Build dimensional hierarchies
- **Add context**: Include metadata, definitions, notes
- **Link related data**: Connect to other datasets when relevant

## Documentation Requirements

### 1. Extraction Log

#### Required Information
- **Report identification**: Title, date, version, source
- **Extraction date/time**: When extraction was performed
- **Extractor name**: Who performed the extraction
- **Method used**: Manual, automated, tool used
- **Time taken**: Duration of extraction process

### 2. Data Dictionary

#### For Each Extracted Field
- **Field name**: Exact name used in output
- **Description**: What the field represents
- **Source location**: Where in report it came from
- **Data type**: Number, text, date, etc.
- **Units/format**: Currency, percentage, date format
- **Validation rules**: Expected range, format, constraints
- **Notes**: Any special considerations or assumptions

### 3. Issues and Assumptions Log

#### Document
- **Data quality issues**: Missing data, inconsistencies found
- **Assumptions made**: What you assumed when data was unclear
- **Transformations applied**: Calculations, conversions, mappings
- **Limitations**: What couldn't be extracted or verified
- **Recommendations**: Suggestions for improving future reports

## Quality Assurance

### 1. Self-Review Checklist

#### Before Finalizing Extraction
- [ ] All required sections extracted
- [ ] Numbers verified against source (spot checks)
- [ ] Formulas recalculated where possible
- [ ] Units and formats consistent
- [ ] Dates and periods correct
- [ ] No obvious errors or outliers
- [ ] Documentation complete
- [ ] Metadata included

### 2. Peer Review Process

#### Review Criteria
- **Accuracy**: Data matches source report
- **Completeness**: Nothing missing that should be included
- **Consistency**: Formatting and structure uniform
- **Clarity**: Documentation is clear and understandable
- **Usability**: Data is ready for analysis

### 3. Continuous Improvement

#### Learn from Experience
- **Track common errors**: Identify patterns in mistakes
- **Refine processes**: Update procedures based on lessons learned
- **Build templates**: Create reusable extraction templates
- **Share knowledge**: Document solutions to unique challenges

## Special Considerations

### 1. Multi-Page Reports
- **Maintain page context**: Note which page data came from
- **Handle page breaks**: Ensure continuity across pages
- **Track section numbering**: Maintain section references
- **Link related data**: Connect data across pages

### 2. Multi-Period Reports
- **Clear period identification**: Label each period distinctly
- **Maintain time series**: Preserve chronological order
- **Handle period comparisons**: Extract comparative metrics carefully
- **Note period definitions**: Fiscal vs calendar, custom periods

### 3. Complex Reports
- **Break into sections**: Extract section by section
- **Maintain relationships**: Link related data across sections
- **Handle nested data**: Hierarchies, sub-totals, groupings
- **Document structure**: Map how sections relate to each other

### 4. Incomplete or Poor Quality Reports
- **Document gaps**: Clearly note what's missing
- **Flag quality issues**: Identify formatting or data problems
- **Estimate impact**: Assess how gaps affect analysis
- **Recommend improvements**: Suggest how report could be improved

## Output Standards

### 1. Data Format Requirements

#### Structured Output
- **Consistent structure**: Same format across all extractions
- **Proper data types**: Numbers as numbers, dates as dates
- **No formatting artifacts**: Clean data, no merged cells, no formulas
- **Ready for analysis**: Data can be immediately used

### 2. File Organization

#### Naming Conventions
- **Descriptive filenames**: Include report name, date, version
- **Version control**: Track different versions of extractions
- **Organized folders**: Logical folder structure
- **Backup files**: Keep original extractions

### 3. Deliverables Package

#### Complete Package Should Include
- **Extracted data file(s)**: Main data output
- **Data dictionary**: Field definitions and metadata
- **Extraction log**: Process documentation
- **Issues log**: Problems encountered and resolutions
- **Source report reference**: Link or copy of original report

## Professional Standards

### 1. Attention to Detail
- **Zero tolerance for errors**: Accuracy is paramount
- **Thoroughness**: Leave no stone unturned
- **Precision**: Correct number of decimal places, exact formatting
- **Consistency**: Same approach throughout entire extraction

### 2. Critical Thinking
- **Question anomalies**: Investigate unexpected values
- **Verify assumptions**: Don't assume, verify
- **Understand context**: Know what data means, not just what it is
- **Think ahead**: Consider how data will be used

### 3. Communication
- **Clear documentation**: Others should understand your work
- **Transparent about limitations**: Honest about what's uncertain
- **Proactive issue reporting**: Flag problems immediately
- **Collaborative approach**: Work with stakeholders effectively

## Tools and Resources

### Recommended Tools
- **Spreadsheet software**: Excel, Google Sheets for manual extraction
- **PDF tools**: Adobe Acrobat, PDF readers with extraction features
- **OCR software**: For scanned documents
- **Data extraction tools**: Power Query, Python (pandas), R
- **Database tools**: For storing and managing extracted data

### Useful Techniques
- **Regular expressions**: For pattern matching in text
- **Text-to-columns**: For parsing delimited data
- **Pivot tables**: For restructuring data
- **Data validation**: Built-in checks in spreadsheet software
- **Version control**: Git for tracking changes

## Conclusion

Professional data extraction requires:
1. **Systematic approach**: Methodical, organized process
2. **Attention to detail**: Zero tolerance for errors
3. **Thorough documentation**: Complete record of process and decisions
4. **Quality assurance**: Multiple validation steps
5. **Continuous improvement**: Learning and refining processes

Remember: The quality of your analysis depends on the quality of your data extraction. Take the time to do it right the first time.

