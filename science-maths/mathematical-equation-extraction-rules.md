# Mathematical Equation Extraction Rules for Cursor AI

## Overview
This document provides comprehensive rules and guidelines that Cursor AI must follow when extracting mathematical equations from written papers, research documents, or academic texts. The primary goal is to ensure 100% accuracy in equation extraction, preservation, and representation.

---

## 1. PRE-EXTRACTION VERIFICATION

### 1.1 Source Document Analysis
- **Identify document type**: Determine if the source is a PDF, scanned image, LaTeX source, Word document, or handwritten notes
- **Check image quality**: For scanned documents, verify resolution is sufficient to read subscripts, superscripts, and special symbols
- **Detect equation numbering**: Identify if equations are numbered (e.g., "(1)", "Equation 2.3", etc.) and preserve numbering
- **Locate equation context**: Note the section, chapter, or page where each equation appears
- **Identify equation type**: Classify as inline, displayed, multi-line, matrix, system of equations, etc.

### 1.2 Symbol Recognition Requirements
- **Greek letters**: Verify correct case (α vs Α, β vs Β, etc.)
- **Subscripts and superscripts**: Distinguish between x_i, x^i, x_{i+1}, x^{i+1}
- **Mathematical operators**: Confirm correct symbols (× vs · vs *, ÷ vs /, etc.)
- **Special functions**: Identify sin, cos, log, ln, exp, max, min, sup, inf, etc.
- **Set notation**: Verify ∈, ∉, ⊂, ⊆, ∪, ∩, ∅, etc.
- **Logic symbols**: Confirm ∀, ∃, ∧, ∨, ¬, ⇒, ⇔, etc.
- **Comparison operators**: Distinguish ≤, ≥, <, >, ≠, ≈, ≪, ≫, etc.
- **Vector/matrix notation**: Identify boldface, overbars, arrows (→, ←, ↔), etc.

---

## 2. EXTRACTION PROCESS

### 2.1 Character-by-Character Verification
- **Read left-to-right, top-to-bottom**: Process equations in natural reading order
- **Verify each character**: Do not assume or guess characters; if uncertain, flag for review
- **Preserve spacing**: Maintain original spacing between terms, operators, and expressions
- **Check alignment**: For multi-line equations, preserve alignment of equals signs, operators, etc.
- **Verify parentheses matching**: Ensure all opening parentheses/brackets have matching closing ones
- **Check nested structures**: Verify proper nesting of parentheses, brackets, braces, and absolute values

### 2.2 Subscript and Superscript Handling
- **Explicit identification**: Clearly distinguish between:
  - Subscripts: x_i, a_{ij}, f_{n+1}
  - Superscripts: x^2, a^{ij}, f^{n+1}
  - Both: x_i^j, a_{ij}^{kl}
- **Multi-character sub/superscripts**: Use braces for multi-character indices: x_{i+1}, not x_i+1
- **Nested sub/superscripts**: Preserve nested structures: x_{i_{j}}, a^{b^{c}}

### 2.3 Fraction and Division Handling
- **Horizontal fractions**: Convert to LaTeX format: (a+b)/(c+d) or \frac{a+b}{c+d}
- **Vertical fractions**: Preserve visual structure in LaTeX: \frac{numerator}{denominator}
- **Complex fractions**: Handle nested fractions carefully: \frac{\frac{a}{b}}{\frac{c}{d}}
- **Division operators**: Distinguish between ÷, /, and fraction notation

### 2.4 Matrix and Vector Extraction
- **Matrix dimensions**: Count and verify rows and columns
- **Matrix elements**: Extract each element individually, preserving position
- **Matrix notation**: Use appropriate notation: [a_{ij}], (a_{ij}), or \begin{pmatrix}...\end{pmatrix}
- **Vector notation**: Distinguish between row vectors, column vectors, and general vectors
- **Boldface/overbar**: Preserve notation indicating vectors: \mathbf{x}, \vec{x}, \bar{x}, \underline{x}

### 2.5 Summation, Product, and Integral Notation
- **Summation (Σ)**: Extract limits correctly:
  - Lower limit: \sum_{i=1}^{n}
  - Upper limit: Verify if it's n, ∞, or another expression
  - Index variable: Confirm i, j, k, etc.
- **Product (Π)**: Same verification as summation
- **Integral (∫)**: Extract:
  - Integration variable: dx, dy, dt, etc.
  - Limits: \int_{a}^{b} or \int_{-\infty}^{\infty}
  - Multiple integrals: \iint, \iiint, \oint
- **Differential operators**: Verify d, ∂, ∇, Δ, etc.

---

## 3. ACCURACY VERIFICATION CHECKLIST

### 3.1 Symbol-by-Symbol Verification
- [ ] Every Greek letter is correctly identified and cased
- [ ] All subscripts are properly placed and enclosed in braces when needed
- [ ] All superscripts are properly placed and enclosed in braces when needed
- [ ] All operators are correctly identified (+, -, ×, ·, /, ÷, etc.)
- [ ] All comparison operators are correct (≤, ≥, <, >, ≠, ≈, etc.)
- [ ] All parentheses, brackets, and braces are matched
- [ ] All function names are correctly identified (sin, cos, log, etc.)
- [ ] All special constants are preserved (π, e, i, ∞, etc.)

### 3.2 Structural Verification
- [ ] Equation numbering is preserved (if present)
- [ ] Multi-line equations maintain proper alignment
- [ ] Fractions are correctly structured
- [ ] Matrices maintain correct dimensions and element positions
- [ ] Summations/products/integrals have correct limits
- [ ] Subscripts and superscripts are on the correct base characters
- [ ] Nested structures are properly formatted

### 3.3 Context Verification
- [ ] Equation label/number matches reference in text
- [ ] Variable names match those used in surrounding text
- [ ] Units (if present) are preserved
- [ ] Conditions or constraints associated with the equation are noted
- [ ] Equation type is correctly identified (definition, theorem, constraint, etc.)

---

## 4. OUTPUT FORMAT REQUIREMENTS

### 4.1 LaTeX Format (Primary)
- **Use standard LaTeX syntax**: All equations must be valid LaTeX
- **Display equations**: Use \[ ... \] or \begin{equation}...\end{equation}
- **Inline equations**: Use \( ... \) or $ ... $
- **Numbered equations**: Use \begin{equation}...\end{equation} with \label{} and \tag{}
- **Multi-line equations**: Use \begin{align}...\end{align} or \begin{split}...\end{split}
- **Matrices**: Use appropriate environment: \begin{pmatrix}, \begin{bmatrix}, \begin{matrix}, etc.

### 4.2 Alternative Formats (When Requested)
- **MathML**: Provide valid MathML representation
- **Unicode**: Use Unicode mathematical symbols when appropriate
- **Plain text**: Use ASCII approximations only when explicitly requested
- **Image preservation**: If original is an image, note this and provide both LaTeX and reference to original

### 4.3 Documentation Requirements
- **Source citation**: Include page number, section, or equation number from source
- **Uncertainty flags**: Mark any characters or symbols that were unclear in the source
- **Format notes**: Document any assumptions made (e.g., "assumed boldface for vector")
- **Context notes**: Include brief context about the equation's purpose if available

---

## 5. COMMON ERRORS TO AVOID

### 5.1 Character Confusion
- **O vs 0**: Verify if character is letter O or number zero
- **l vs 1 vs I**: Distinguish lowercase L, number 1, and uppercase I
- **Greek vs Latin**: Distinguish α vs a, β vs B, γ vs y, etc.
- **Minus vs hyphen**: Use correct minus sign (−) not hyphen (-) in equations
- **Prime vs apostrophe**: Use ′ for derivatives, not '

### 5.2 Spacing Errors
- **Function spacing**: sin x vs sin(x) - preserve original
- **Operator spacing**: a+b vs a + b - preserve original spacing
- **Multiplication**: ab vs a·b vs a×b vs a*b - preserve original notation

### 5.3 Structural Errors
- **Missing parentheses**: Verify all opening parentheses have closing ones
- **Incorrect nesting**: Check that nested structures are properly formatted
- **Misaligned fractions**: Ensure fraction bars align correctly
- **Wrong matrix dimensions**: Verify row and column counts

### 5.4 Notation Errors
- **Vector notation**: Don't confuse boldface, overbar, arrow, or underline notation
- **Set notation**: Verify correct use of { }, [ ], ( ) for sets, intervals, tuples
- **Function notation**: Distinguish f(x), f_x, f^x, f^{(x)}

---

## 6. VERIFICATION PROTOCOL

### 6.1 First Pass: Character Extraction
1. Extract equation character by character
2. Flag any unclear characters with [UNCLEAR: ?]
3. Preserve original formatting and spacing
4. Note equation number and location

### 6.2 Second Pass: Symbol Verification
1. Verify each Greek letter is correct
2. Check all subscripts and superscripts
3. Verify all operators and special symbols
4. Confirm function names are correct

### 6.3 Third Pass: Structural Verification
1. Check parentheses/brackets matching
2. Verify fraction structures
3. Check matrix dimensions and elements
4. Verify summation/product/integral limits
5. Check alignment in multi-line equations

### 6.4 Fourth Pass: Context Verification
1. Compare variable names with surrounding text
2. Verify equation numbering matches references
3. Check if units or conditions are associated
4. Confirm equation type makes sense in context

### 6.5 Final Pass: Output Verification
1. Verify LaTeX compiles correctly (if possible)
2. Check output format matches requirements
3. Ensure all uncertainty flags are documented
4. Verify source citation is included

---

## 7. SPECIAL CASES

### 7.1 Handwritten Equations
- **Be extra cautious**: Handwriting can be ambiguous
- **Flag all uncertain characters**: Use [UNCLEAR: ?] liberally
- **Note style variations**: Document unusual notation
- **Request clarification**: If multiple interpretations are possible, note all options

### 7.2 Poor Quality Scans
- **Enhancement attempts**: Note if image enhancement was attempted
- **Flag low-confidence extractions**: Mark characters with low confidence
- **Provide alternatives**: If uncertain, provide multiple possible interpretations

### 7.3 Non-Standard Notation
- **Document deviations**: Note any non-standard notation used
- **Preserve original**: Don't "correct" non-standard notation unless explicitly requested
- **Provide explanation**: Explain what the notation likely means

### 7.4 Multi-Page Equations
- **Track continuation**: Note if equation continues across pages
- **Preserve structure**: Maintain alignment and formatting across pages
- **Verify completeness**: Ensure entire equation is captured

### 7.5 Annotated Equations
- **Preserve annotations**: Include any notes, arrows, or annotations near the equation
- **Separate annotations**: Distinguish between equation and annotations
- **Document annotations**: Explain what annotations refer to

---

## 8. QUALITY ASSURANCE

### 8.1 Confidence Levels
Assign confidence levels to each extraction:
- **High (95-100%)**: Clear source, standard notation, unambiguous
- **Medium (80-94%)**: Mostly clear, minor ambiguities resolved
- **Low (50-79%)**: Significant ambiguities, multiple possible interpretations
- **Very Low (<50%)**: Source unclear, cannot reliably extract

### 8.2 Required Actions by Confidence Level
- **High**: Proceed with extraction, minimal verification needed
- **Medium**: Double-check ambiguous elements, flag for review
- **Low**: Extract with extensive flags, provide alternatives, request human verification
- **Very Low**: Do not extract, request better source or human assistance

### 8.3 Error Reporting
For any extraction:
- **List all flagged characters**: Document every [UNCLEAR: ?] marker
- **Provide alternatives**: For ambiguous characters, list all possible interpretations
- **Note assumptions**: Document any assumptions made during extraction
- **Suggest verification**: Recommend how to verify uncertain elements

---

## 9. OUTPUT TEMPLATE

For each extracted equation, provide:

```markdown
## Equation [NUMBER]

**Source**: [Page X, Section Y, or Equation Z]
**Type**: [Inline/Display/Multi-line/Matrix/System/etc.]
**Confidence**: [High/Medium/Low/Very Low]

**LaTeX**:
```latex
[LaTeX code here]
```

**Rendered**: [Visual representation if possible]

**Context**: [Brief description of equation's purpose]

**Notes**:
- [Any uncertainty flags]
- [Any assumptions made]
- [Any non-standard notation]
- [Any verification recommendations]
```

---

## 10. MANDATORY WORKFLOW

When extracting mathematical equations, Cursor AI MUST:

1. **Never guess**: If a character is unclear, flag it rather than guessing
2. **Always verify**: Perform all four verification passes before finalizing
3. **Document everything**: Include source, confidence, and all notes
4. **Preserve original**: Don't "improve" or "correct" the original equation
5. **Flag uncertainties**: Be transparent about any ambiguities
6. **Request clarification**: When confidence is low, ask for better source or human verification
7. **Verify LaTeX**: Ensure output LaTeX is syntactically correct
8. **Check context**: Verify equation makes sense in its context
9. **Preserve formatting**: Maintain original spacing, alignment, and structure
10. **Double-check**: Review extraction at least twice before finalizing

---

## 11. EXAMPLES OF CORRECT EXTRACTION

### Example 1: Simple Equation
**Source**: Page 5, Section 2.1
**Original**: E = mc²
**Extracted**: `E = mc^2` or `E = mc^{2}`
**Note**: Preserve superscript notation

### Example 2: Fraction
**Source**: Page 10, Equation 3.2
**Original**: (a+b)/(c+d)
**Extracted**: `\frac{a+b}{c+d}` or `(a+b)/(c+d)` depending on context
**Note**: Use \frac for displayed equations, preserve original for inline

### Example 3: Summation
**Source**: Page 15, Equation 4.5
**Original**: Σ(i=1 to n) x_i
**Extracted**: `\sum_{i=1}^{n} x_i`
**Note**: Verify limits are correct

### Example 4: Matrix
**Source**: Page 20, Equation 5.1
**Original**: 2x2 matrix with elements a_11, a_12, a_21, a_22
**Extracted**: 
```latex
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}
```
**Note**: Verify matrix dimensions and element positions

---

## 12. FINAL REMINDERS

- **Accuracy over speed**: Take time to verify rather than rushing
- **When in doubt, flag it**: Better to flag uncertainty than make incorrect assumptions
- **Preserve original intent**: Don't "modernize" or "improve" notation
- **Context matters**: Consider the equation's purpose and surrounding text
- **Multiple formats**: Be prepared to provide LaTeX, MathML, or other formats as needed
- **Continuous verification**: Verify at each step, not just at the end
- **Human review for low confidence**: Always recommend human review for low-confidence extractions

---

**Last Updated**: [Date]
**Version**: 1.0
**Status**: Active - Must be followed for all mathematical equation extractions

