# Mathematical Functions for Deep Data Analysis Rules

## Overview

This document provides comprehensive rules for creating mathematical functions that enable genius-level data analysis while avoiding overengineering and ensuring all assumptions are thoroughly tested. The goal is to build sophisticated, reliable analytical functions that reveal deep insights without unnecessary complexity.

---

## Core Principles

### Simplicity Before Complexity
- **Start with the simplest function that solves the problem.** Only add complexity when simpler approaches fail.
- **Question every parameter.** If you can't explain why a parameter exists, remove it.
- **Avoid premature optimisation.** Build correctly first, optimise only when profiling shows it's needed.
- **Prefer well-understood methods** over novel approaches unless the novel approach is demonstrably superior.
- **One function, one purpose.** Each function should have a single, clear responsibility.

### Rigorous Testing of Assumptions
- **All assumptions must be explicitly stated** before implementation.
- **Every assumption must be testable** with concrete validation criteria.
- **Test assumptions on real data**, not just synthetic examples.
- **Document assumption failures** and their impact on results.
- **Never assume data properties** (normality, independence, stationarity) without verification.

### Mathematical Rigour
- **Verify mathematical correctness** before implementation.
- **Check boundary conditions** and edge cases mathematically.
- **Validate against known analytical solutions** when available.
- **Ensure numerical stability** for all input ranges.
- **Document mathematical foundations** and references.

---

## Function Design Principles

### 1. Input Validation and Preconditions

- **Validate all inputs explicitly.** Never trust that inputs are in the expected format or range.
- **Check data types** before processing (numeric, categorical, datetime, etc.).
- **Verify data dimensions** match function expectations (vector length, matrix shape, etc.).
- **Test for missing values** and handle them explicitly (don't silently fail).
- **Validate data ranges** (e.g., probabilities must be [0,1], counts must be non-negative).
- **Check for degenerate cases** (empty arrays, single values, constant sequences).
- **Verify required dependencies** (e.g., sufficient data points for statistical tests).
- **Document all preconditions** in function docstrings.

### 2. Mathematical Correctness

- **Derive formulas from first principles** or cite authoritative sources.
- **Verify against known test cases** with analytical solutions.
- **Check dimensional consistency** (units, scales, etc.).
- **Validate against mathematical identities** (e.g., probability axioms, conservation laws).
- **Test special cases** where results are known (e.g., identity matrices, zero vectors).
- **Verify symmetry properties** when applicable (e.g., distance functions should be symmetric).
- **Check limiting behaviour** (as parameters approach 0, infinity, or boundaries).

### 3. Numerical Stability

- **Avoid catastrophic cancellation** in floating-point arithmetic.
- **Use numerically stable algorithms** (e.g., log-sum-exp trick, QR decomposition).
- **Check for overflow and underflow** conditions.
- **Use appropriate data types** (float32 vs float64) based on precision needs.
- **Implement safe division** (check for division by zero).
- **Handle very large or very small numbers** appropriately.
- **Test with extreme values** (very large, very small, near-zero).
- **Use relative error tolerances** when comparing floating-point results.

### 4. Statistical Validity

- **Verify statistical assumptions** before applying methods (normality, independence, homoscedasticity).
- **Check sample size requirements** for statistical tests.
- **Validate distribution assumptions** with goodness-of-fit tests.
- **Test for independence** when required (autocorrelation tests, chi-square tests).
- **Verify stationarity** for time series methods.
- **Check for confounding variables** in causal analysis.
- **Validate model assumptions** (linearity, additivity, etc.) with diagnostic tests.

---

## Testing and Validation Framework

### 1. Unit Testing Requirements

- **Test with known analytical solutions** first.
- **Test edge cases**: empty inputs, single values, identical values, extreme values.
- **Test boundary conditions**: minimum/maximum valid inputs, transition points.
- **Test invalid inputs**: wrong types, out-of-range values, missing data.
- **Test degenerate cases**: constant sequences, perfectly correlated variables, singular matrices.
- **Verify mathematical properties**: symmetry, transitivity, idempotency where applicable.
- **Test numerical precision**: compare against high-precision reference implementations.
- **Test performance**: ensure functions complete in reasonable time for expected inputs.

### 2. Property-Based Testing

- **Test invariants**: properties that should always hold regardless of input.
- **Test mathematical identities**: verify functions satisfy known mathematical relationships.
- **Test monotonicity**: where applicable, verify functions are monotonic.
- **Test continuity**: verify functions behave continuously (no sudden jumps).
- **Test differentiability**: where applicable, verify derivatives exist and are correct.
- **Test scale invariance**: verify functions behave correctly under scaling transformations.
- **Test translation invariance**: where applicable, verify functions are translation-invariant.

### 3. Empirical Validation

- **Test on real-world datasets** with known ground truth when available.
- **Compare against established implementations** (e.g., scipy, R packages).
- **Validate against published results** from academic papers or benchmarks.
- **Test on diverse datasets**: different domains, sizes, and characteristics.
- **Verify results make domain sense**: check against expert knowledge and expectations.
- **Test sensitivity analysis**: verify small input changes produce small output changes (when appropriate).
- **Test robustness**: verify functions handle noisy or imperfect data gracefully.

### 4. Assumption Testing Protocol

For each assumption, create a test that:

- **Explicitly states the assumption** in code comments and documentation.
- **Implements a statistical or mathematical test** to verify the assumption.
- **Reports test results** (p-values, test statistics, confidence intervals).
- **Provides clear pass/fail criteria** based on significance levels.
- **Suggests alternatives** if the assumption fails.
- **Documents assumption violations** and their impact on results.

Example assumption tests:
- Normality: Shapiro-Wilk, Kolmogorov-Smirnov, or Q-Q plots
- Independence: autocorrelation tests, chi-square tests of independence
- Stationarity: Augmented Dickey-Fuller test, KPSS test
- Linearity: residual plots, Ramsey RESET test
- Homoscedasticity: Breusch-Pagan test, White test

---

## Common Mathematical Functions and Their Requirements

### 1. Distance and Similarity Functions

**Requirements:**
- **Non-negativity**: distance(x, y) ≥ 0
- **Identity**: distance(x, x) = 0
- **Symmetry**: distance(x, y) = distance(y, x)
- **Triangle inequality**: distance(x, z) ≤ distance(x, y) + distance(y, z) (for metrics)

**Testing:**
- Verify all metric properties with diverse inputs.
- Test with zero vectors, identical vectors, orthogonal vectors.
- Test with vectors of different magnitudes.
- Verify numerical stability with very small or very large values.

### 2. Statistical Aggregation Functions

**Requirements:**
- **Handle missing values** explicitly (don't silently ignore).
- **Return appropriate types** (NaN for undefined operations, not errors).
- **Preserve data types** when possible (integers remain integers).
- **Handle empty inputs** gracefully.

**Testing:**
- Test with all missing values.
- Test with mixed missing and present values.
- Test with single values.
- Test with constant sequences.
- Verify against known formulas (e.g., sample variance formula).

### 3. Transformation Functions

**Requirements:**
- **Invertibility**: document when functions are invertible and provide inverse.
- **Domain restrictions**: clearly document valid input ranges.
- **Range documentation**: document output ranges.
- **Monotonicity**: document when functions are monotonic.

**Testing:**
- Test with values at domain boundaries.
- Test inverse functions (if applicable): f(f_inv(x)) ≈ x.
- Test monotonicity where applicable.
- Test with extreme values (very large, very small, near boundaries).

### 4. Optimisation Functions

**Requirements:**
- **Convergence criteria**: clearly defined stopping conditions.
- **Initialisation sensitivity**: document sensitivity to starting values.
- **Local vs global**: clearly state if finding local or global optima.
- **Constraint handling**: document how constraints are handled.

**Testing:**
- Test with known optimal solutions.
- Test with multiple starting points.
- Test convergence on well-conditioned and ill-conditioned problems.
- Test with boundary constraints.
- Verify optimality conditions (gradient near zero, KKT conditions).

### 5. Decomposition Functions (PCA, SVD, etc.)

**Requirements:**
- **Reconstruction error**: verify X ≈ UΣV^T (or equivalent).
- **Orthogonality**: verify orthonormal properties of components.
- **Ordering**: verify components are ordered by explained variance.
- **Dimensionality**: verify output dimensions match expectations.

**Testing:**
- Test reconstruction: verify original data can be reconstructed.
- Test orthogonality: verify U^T U = I, V^T V = I.
- Test with known low-rank matrices.
- Test with singular matrices.
- Compare against reference implementations.

### 6. Time Series Functions

**Requirements:**
- **Stationarity**: verify or test for stationarity assumptions.
- **Temporal ordering**: preserve and respect temporal order.
- **Missing time points**: handle irregularly spaced data explicitly.
- **Seasonality**: document seasonal patterns and how they're handled.

**Testing:**
- Test with stationary and non-stationary series.
- Test with missing values and irregular spacing.
- Test with known periodic patterns.
- Test with trend components.
- Verify against analytical solutions for simple cases.

---

## Avoiding Overengineering

### Red Flags of Overengineering

- **Too many parameters**: if a function has more than 5-7 parameters, consider refactoring.
- **Unused features**: if code paths are never executed, remove them.
- **Premature abstraction**: don't create abstractions until you have at least 3 concrete use cases.
- **Complexity without benefit**: if a simple solution works, don't replace it with a complex one.
- **Optimisation without profiling**: don't optimise code that isn't a bottleneck.
- **Theoretical elegance over practicality**: prefer solutions that work well in practice.

### When to Add Complexity

Add complexity only when:
- **Simple solutions fail** on real data or edge cases.
- **Performance is proven to be a bottleneck** through profiling.
- **Accuracy requirements demand it** (e.g., high-precision scientific computing).
- **The problem domain requires it** (e.g., handling non-standard distributions).
- **You have evidence** that complexity improves results.

### Simplification Strategies

- **Remove optional parameters** that are rarely used differently from defaults.
- **Split complex functions** into smaller, composable functions.
- **Use standard libraries** instead of custom implementations when possible.
- **Eliminate redundant calculations** and cache results when appropriate.
- **Simplify formulas** using mathematical identities when possible.
- **Use established algorithms** instead of inventing new ones.

---

## Error Handling and Edge Cases

### Error Types to Handle

- **Input errors**: wrong type, wrong shape, out of range.
- **Mathematical errors**: division by zero, log of negative, invalid operations.
- **Numerical errors**: overflow, underflow, NaN propagation.
- **Convergence failures**: optimisation not converging, iterative methods diverging.
- **Data quality issues**: insufficient data, too many missing values, degenerate cases.

### Error Handling Strategy

- **Fail fast with clear messages**: don't silently return wrong results.
- **Provide actionable error messages**: tell users what went wrong and how to fix it.
- **Use appropriate exception types**: ValueError, TypeError, etc.
- **Return NaN or None** for undefined operations, not exceptions (when appropriate).
- **Log warnings** for recoverable issues (e.g., "assuming normality, but data may not be normal").
- **Document all possible error conditions** in docstrings.

### Edge Case Handling

For each function, explicitly handle:
- **Empty inputs**: empty arrays, empty lists, zero-length vectors.
- **Single values**: arrays with one element.
- **Constant sequences**: all values identical.
- **Extreme values**: very large, very small, near-zero.
- **Boundary values**: at the edges of valid ranges.
- **Degenerate cases**: singular matrices, perfectly correlated variables, zero variance.
- **Missing data**: NaN, None, or sentinel values depending on context.

---

## Documentation Requirements

### Function Documentation Must Include

- **Purpose**: what the function does in one clear sentence.
- **Mathematical formulation**: the core formula or algorithm.
- **Parameters**: type, range, meaning, and default values for each parameter.
- **Returns**: type, meaning, and range of return values.
- **Assumptions**: all mathematical and statistical assumptions.
- **Preconditions**: requirements on inputs (e.g., "input must be non-negative").
- **Postconditions**: guarantees about outputs (e.g., "output is in [0,1]").
- **Edge cases**: how the function handles edge cases.
- **References**: citations to papers, books, or algorithms used.
- **Examples**: at least 2-3 usage examples with expected outputs.
- **See also**: related functions or alternatives.

### Code Comments

- **Explain why, not what**: comments should explain reasoning, not restate code.
- **Document non-obvious choices**: why this algorithm, why this parameter value.
- **Note assumptions**: inline comments for assumptions that aren't obvious.
- **Mark TODOs**: if something needs improvement, mark it clearly.
- **Reference formulas**: cite equation numbers or sources for complex formulas.

---

## Performance Considerations

### When Performance Matters

- **Profile first**: identify actual bottlenecks before optimising.
- **Measure improvements**: verify optimisations actually improve performance.
- **Consider trade-offs**: sometimes accuracy or clarity is more important than speed.
- **Document performance characteristics**: O(n) complexity, expected runtime.

### Performance Optimisation Guidelines

- **Use vectorised operations** instead of loops when possible.
- **Cache expensive computations** when inputs repeat.
- **Use appropriate data structures** (sparse matrices for sparse data).
- **Leverage compiled code** (NumPy, SciPy) instead of pure Python loops.
- **Consider parallelisation** for independent computations.
- **Avoid premature optimisation**: correctness and clarity come first.

---

## Validation Checklist

Before considering a mathematical function complete, verify:

### Mathematical Correctness
- [ ] Formula is mathematically correct and derived from first principles or cited.
- [ ] Function satisfies all required mathematical properties (symmetry, transitivity, etc.).
- [ ] Boundary conditions are handled correctly.
- [ ] Limiting behaviour is correct (as parameters approach boundaries).
- [ ] Numerical stability is verified (no catastrophic cancellation, overflow, underflow).

### Statistical Validity
- [ ] All statistical assumptions are explicitly stated.
- [ ] Assumption tests are implemented and documented.
- [ ] Function works correctly when assumptions are met.
- [ ] Function behaviour when assumptions fail is documented.
- [ ] Sample size requirements are documented and checked.

### Testing Coverage
- [ ] Unit tests cover all edge cases.
- [ ] Property-based tests verify mathematical properties.
- [ ] Empirical tests validate on real data.
- [ ] Tests compare against reference implementations or analytical solutions.
- [ ] Tests cover invalid inputs and error conditions.

### Code Quality
- [ ] Input validation is comprehensive.
- [ ] Error handling is appropriate and informative.
- [ ] Documentation is complete and accurate.
- [ ] Code is readable and well-commented.
- [ ] No overengineering (complexity is justified).

### Practical Validation
- [ ] Function produces sensible results on real-world data.
- [ ] Results match domain expert expectations.
- [ ] Function performs acceptably (speed, memory).
- [ ] Function integrates well with existing codebase.

---

## Common Mistakes to Avoid

### Mathematical Mistakes

- **Assuming normality** without testing.
- **Ignoring correlation** when independence is assumed.
- **Using wrong formulas** (e.g., population vs sample variance).
- **Mixing up parameters** (e.g., standard deviation vs variance).
- **Incorrect degrees of freedom** in statistical tests.
- **Wrong matrix dimensions** in linear algebra operations.
- **Sign errors** in formulas (especially in gradients or derivatives).

### Implementation Mistakes

- **Silent failures**: returning NaN or wrong values instead of errors.
- **Off-by-one errors**: incorrect indexing in loops or array operations.
- **Type mismatches**: not handling integer vs float correctly.
- **Missing validation**: not checking inputs before processing.
- **Incorrect default values**: defaults that don't make sense for the use case.
- **Memory issues**: not handling large datasets efficiently.

### Testing Mistakes

- **Testing only happy paths**: not testing edge cases and errors.
- **Using same data for training and testing**: data leakage in validation.
- **Not testing assumptions**: assuming data properties without verification.
- **Insufficient test coverage**: missing important code paths.
- **Tests that don't fail**: tests that always pass regardless of implementation.

### Overengineering Mistakes

- **Adding features that aren't needed**: solving problems that don't exist.
- **Premature optimisation**: optimising code that isn't a bottleneck.
- **Unnecessary abstraction**: creating abstractions before they're needed.
- **Complex solutions for simple problems**: using advanced methods when simple ones work.
- **Ignoring simple solutions**: dismissing simple approaches without trying them.

---

## Example: Building a Robust Correlation Function

### Step 1: Define Requirements

- Calculate Pearson correlation coefficient.
- Handle missing values explicitly.
- Return NaN for invalid inputs (insufficient data, zero variance).
- Support both population and sample correlation.

### Step 2: State Assumptions

- Variables are continuous (or at least interval-scaled).
- Relationship is linear (Pearson correlation measures linear relationships).
- Data are paired (same length, corresponding observations).
- No assumption of normality required (correlation doesn't require normality).

### Step 3: Mathematical Formulation

```
r = Σ(x_i - x̄)(y_i - ȳ) / √[Σ(x_i - x̄)² × Σ(y_i - ȳ)²]
```

### Step 4: Implement with Validation

```python
def pearson_correlation(x, y, handle_missing='pairwise'):
    """
    Calculate Pearson correlation coefficient.
    
    Assumptions:
    - Linear relationship between variables
    - Paired observations (same length)
    
    Preconditions:
    - x and y are numeric arrays of same length
    - At least 2 valid pairs after handling missing values
    
    Returns:
    - Correlation coefficient in [-1, 1] or NaN if invalid
    """
    # Input validation
    x = np.asarray(x)
    y = np.asarray(y)
    
    if x.shape != y.shape:
        raise ValueError("x and y must have same shape")
    
    if len(x) < 2:
        return np.nan
    
    # Handle missing values
    if handle_missing == 'pairwise':
        mask = ~(np.isnan(x) | np.isnan(y))
        x_clean = x[mask]
        y_clean = y[mask]
    elif handle_missing == 'complete':
        mask = ~(np.isnan(x) | np.isnan(y))
        if not mask.all():
            return np.nan
        x_clean = x
        y_clean = y
    else:
        raise ValueError("handle_missing must be 'pairwise' or 'complete'")
    
    # Check sufficient data
    if len(x_clean) < 2:
        return np.nan
    
    # Check for constant variables (zero variance)
    x_std = np.std(x_clean, ddof=1)
    y_std = np.std(y_clean, ddof=1)
    
    if x_std == 0 or y_std == 0:
        return np.nan  # Correlation undefined for constant variables
    
    # Calculate correlation
    x_centered = x_clean - np.mean(x_clean)
    y_centered = y_clean - np.mean(y_clean)
    
    numerator = np.sum(x_centered * y_centered)
    denominator = np.sqrt(np.sum(x_centered**2) * np.sum(y_centered**2))
    
    if denominator == 0:
        return np.nan
    
    correlation = numerator / denominator
    
    # Verify result is in valid range (numerical stability check)
    correlation = np.clip(correlation, -1.0, 1.0)
    
    return correlation
```

### Step 5: Comprehensive Testing

```python
def test_pearson_correlation():
    # Test 1: Perfect positive correlation
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    assert abs(pearson_correlation(x, y) - 1.0) < 1e-10
    
    # Test 2: Perfect negative correlation
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([10, 8, 6, 4, 2])
    assert abs(pearson_correlation(x, y) - (-1.0)) < 1e-10
    
    # Test 3: No correlation
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 1, 4, 3, 5])
    # Should be close to 0 (exact value depends on data)
    
    # Test 4: Missing values
    x = np.array([1, 2, np.nan, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    result = pearson_correlation(x, y, handle_missing='pairwise')
    # Should calculate on 4 valid pairs
    
    # Test 5: Insufficient data
    x = np.array([1])
    y = np.array([2])
    assert np.isnan(pearson_correlation(x, y))
    
    # Test 6: Constant variable
    x = np.array([1, 1, 1, 1, 1])
    y = np.array([1, 2, 3, 4, 5])
    assert np.isnan(pearson_correlation(x, y))
    
    # Test 7: Compare with reference implementation
    from scipy.stats import pearsonr
    x = np.random.randn(100)
    y = np.random.randn(100)
    our_result = pearson_correlation(x, y)
    scipy_result, _ = pearsonr(x, y)
    assert abs(our_result - scipy_result) < 1e-10
```

---

## Final Reminders

- **Simplicity wins**: the simplest correct solution is usually the best.
- **Test assumptions**: never assume, always verify.
- **Document everything**: future you (and others) will thank you.
- **Fail clearly**: better to fail with a clear error than return wrong results silently.
- **Validate thoroughly**: test edge cases, boundary conditions, and real-world data.
- **Avoid overengineering**: add complexity only when it's necessary and proven beneficial.
- **Mathematical rigour**: verify correctness before optimising.
- **Practical validation**: ensure functions work on real data, not just test cases.

---

**Remember**: Genius-level analysis comes from deep understanding, rigorous validation, and careful implementation—not from complexity. Build functions that are mathematically sound, thoroughly tested, and appropriately simple for the problem at hand.

