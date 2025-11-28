# Excel and Dataset Extraction Rules

When extracting and analysing data from Excel files and datasets, follow these rules to ensure accurate, reliable, and well-documented data extraction.

## Initial File Assessment

- **Examine the file structure first.** Check for multiple sheets, hidden rows/columns, merged cells, and header configurations before extracting data.
- **Identify the data range.** Determine where actual data begins and ends, accounting for headers, footers, and summary rows.
- **Document the file format and version.** Note whether it's .xlsx, .xls, .csv, or other formats, as this affects extraction methods.
- **Check for data quality indicators.** Look for notes, comments, or metadata sheets that explain data collection methods or known issues.
- **Identify the primary key or unique identifiers** in the dataset to ensure data integrity during extraction.
- **Examine cell formatting** for clues about data types (dates, numbers, text) that might not be immediately obvious from raw values.
- **Check for protected sheets or password protection** that might require special handling.

## Header and Structure Detection

- **Always identify header rows explicitly.** Don't assume row 1 contains headers; headers might be in row 2, 3, or later.
- **Handle multi-row headers gracefully.** Some Excel files use multiple header rows; extract and combine them appropriately.
- **Preserve header names exactly as they appear** unless explicitly asked to clean or standardise them.
- **Detect and handle merged header cells** by expanding merged values across appropriate columns.
- **Identify and skip summary rows** (totals, subtotals, averages) that appear within data ranges.
- **Check for column name consistency** across multiple sheets or files when combining data.
- **Document any header variations** or inconsistencies found across sheets or files.

## Data Type Handling

- **Preserve original data types when possible.** Don't convert numbers to strings or dates to text unless necessary.
- **Handle date formats carefully.** Excel stores dates as numbers; identify and convert them to proper date objects, preserving the original format information.
- **Detect and preserve number formats** including currency, percentages, and decimal precision.
- **Handle mixed data types in columns.** Some columns may contain both text and numbers; document these cases.
- **Preserve leading zeros** in identifiers (e.g., "00123" should remain as text, not become 123).
- **Handle boolean values consistently.** Convert Excel TRUE/FALSE to appropriate boolean types, not strings.
- **Detect and handle error values** (#N/A, #VALUE!, #REF!, etc.) explicitly rather than silently converting them.
- **Preserve null/empty cell distinctions.** Distinguish between empty cells, cells with spaces, and cells with actual null values.

## Missing and Incomplete Data

- **Document missing data patterns.** Identify whether missing values are random, systematic, or follow a pattern.
- **Preserve Excel's representation of missing data.** Don't automatically fill with zeros or empty strings; maintain null/NA values.
- **Check for placeholder values** that represent missing data (e.g., "N/A", "NULL", "-", "TBD") and standardise them appropriately.
- **Identify incomplete rows or columns** and document them separately from complete data.
- **Handle merged cells that span data ranges** by determining how to distribute the merged value.
- **Check for hidden rows or columns** that might contain important data or affect data interpretation.

## Data Extraction Best Practices

- **Extract data in chunks for large files** to avoid memory issues, but maintain data integrity across chunks.
- **Preserve row and column relationships** when extracting subsets of data.
- **Maintain referential integrity** when extracting related data from multiple sheets or files.
- **Extract formulas as formulas when needed**, or calculate and extract values based on requirements.
- **Preserve cell comments and notes** if they contain important context or metadata.
- **Handle named ranges appropriately** by expanding them to their actual cell references.
- **Extract data validation rules** if they provide important constraints or context.
- **Preserve conditional formatting information** if it indicates data quality or status.

## Multi-Sheet Handling

- **List all available sheets** before extraction to confirm which sheets contain relevant data.
- **Handle sheet naming conventions** consistently, including spaces, special characters, and long names.
- **Check for duplicate sheet names** or similar names that might cause confusion.
- **Extract sheet metadata** (sheet names, positions) along with data for traceability.
- **Combine data from multiple sheets** only when structure and column names are compatible.
- **Document relationships between sheets** (lookups, references, data flows) when extracting related data.
- **Handle sheet-specific formatting or structure differences** appropriately rather than forcing uniformity.

## Data Validation and Quality Checks

- **Validate data ranges** to ensure extracted data matches expected dimensions.
- **Check for duplicate rows** and document them rather than silently removing them.
- **Verify data consistency** across related columns (e.g., dates should be in chronological order if applicable).
- **Validate data against known constraints** (e.g., percentages should be 0-100, ages should be reasonable).
- **Check for data entry errors** such as typos in categorical fields or impossible values.
- **Verify calculated fields** by recalculating formulas when possible.
- **Cross-reference data** with source documentation or previous extractions when available.
- **Document any data quality issues** found during extraction.

## Error Handling

- **Handle file access errors gracefully.** Provide clear error messages if files are locked, missing, or corrupted.
- **Detect and report encoding issues** that might cause character corruption in extracted text.
- **Handle version compatibility issues** between different Excel formats (.xls vs .xlsx).
- **Manage memory errors** for very large files by implementing chunked reading or sampling strategies.
- **Report partial extraction failures** clearly, indicating which data was successfully extracted and which failed.
- **Preserve error context** including file paths, sheet names, and row/column positions when errors occur.

## Output and Documentation

- **Document the extraction process** including which sheets, rows, and columns were extracted.
- **Preserve source information** including file names, sheet names, and extraction timestamps.
- **Include data dictionaries** that describe column meanings, data types, and value ranges when available.
- **Document any transformations** applied during extraction (type conversions, cleaning, filtering).
- **Provide summary statistics** for extracted data (row counts, column counts, missing value counts).
- **Include extraction metadata** such as file size, last modified date, and Excel version if available.
- **Create reproducible extraction scripts** that can be rerun on updated files.
- **Output data in appropriate formats** (CSV, JSON, Parquet) based on downstream analysis needs.

## Performance Considerations

- **Use appropriate libraries** (pandas, openpyxl, xlrd) based on file size and format requirements.
- **Read only necessary sheets and ranges** for large files to improve performance.
- **Use efficient data types** in output formats to reduce memory usage and improve processing speed.
- **Consider file size limitations** and implement streaming or chunked reading for very large files.
- **Cache extraction results** when the same file will be processed multiple times.
- **Optimise for the specific use case** rather than using a one-size-fits-all approach.

## Security and Privacy

- **Handle sensitive data appropriately.** Don't log or expose personally identifiable information during extraction.
- **Respect file permissions** and don't attempt to extract from protected or restricted files without authorisation.
- **Validate file sources** before extraction to avoid processing malicious files.
- **Sanitise file paths and names** in logs and error messages to avoid exposing sensitive directory structures.
- **Handle password-protected files** securely, never storing passwords in code or logs.

## Common Excel-Specific Issues

- **Handle Excel's 1900 vs 1904 date system** correctly when converting dates.
- **Detect and handle Excel's maximum row/column limits** (1,048,576 rows, 16,384 columns for .xlsx).
- **Manage Excel's precision issues** with floating-point numbers (15-17 significant digits).
- **Handle Excel's text-to-columns scenarios** where data might be improperly delimited within cells.
- **Detect and handle Excel's automatic type conversion** (e.g., strings that look like numbers being converted).
- **Manage Excel's formula calculation dependencies** when extracting calculated values.
- **Handle Excel's array formulas** appropriately, preserving their structure or expanding as needed.

## Dataset Combination and Integration

- **Standardise column names** when combining data from multiple Excel files, but document the mapping.
- **Handle schema differences** between files gracefully, using union or join strategies as appropriate.
- **Preserve data lineage** by tracking which data came from which file and sheet.
- **Resolve conflicts** when the same identifier appears in multiple sources.
- **Maintain data integrity** when merging datasets with different structures or time periods.
- **Document combination logic** including how duplicates, missing values, and conflicts were handled.

## Code Quality for Data Extraction

- **Write modular extraction functions** that can handle different file structures and formats.
- **Use configuration files** for extraction parameters (sheet names, header rows, data ranges) rather than hardcoding.
- **Implement logging** to track extraction progress and issues.
- **Create unit tests** for extraction functions using sample Excel files.
- **Handle edge cases** explicitly (empty files, single-row files, files with only headers).
- **Use type hints** to document expected inputs and outputs of extraction functions.
- **Write clear error messages** that help users understand what went wrong and how to fix it.

## Reproducibility

- **Version control extraction scripts** along with sample data files for testing.
- **Document Excel file versions** and any manual preprocessing steps required.
- **Set random seeds** if any random sampling is used during extraction.
- **Preserve extraction parameters** in configuration files or code comments.
- **Create extraction logs** that record what was extracted, when, and from which files.
- **Document any manual interventions** required during the extraction process.

## Communication

- **Report extraction results clearly** including row counts, column counts, and any issues encountered.
- **Provide data quality summaries** highlighting missing values, duplicates, and anomalies.
- **Explain any data transformations** or cleaning steps applied during extraction.
- **Flag potential issues** that might affect downstream analysis (e.g., "Date column contains text values").
- **Suggest next steps** based on what was found during extraction (e.g., "Consider investigating missing values in column X").

---

**Remember:** The goal is accurate, reliable data extraction that preserves data integrity and provides clear documentation. When in doubt, preserve the original data structure and document any assumptions or transformations made during extraction. Always validate extracted data against the source file to ensure accuracy.

