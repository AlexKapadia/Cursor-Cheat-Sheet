# Jump-Diffusion Models MDC

## What It Is

This MDC (Model-Driven Code) document provides a comprehensive extraction of the paper "Jump-Diffusion Models" by Wolfgang J. Runggaldier. It serves as a complete reference for implementing jump-diffusion models in quantitative finance applications.

**Source Paper:** Jump-Diffusion Models by Wolfgang J. Runggaldier (Università di Padova)

**Purpose:** This MDC extracts all technical content, mathematical formulations, algorithms, and implementation guidance from the paper so that developers can implement jump-diffusion models without needing to read the original paper.

## How It Works

This MDC was created following a rigorous 4-pass extraction protocol:

1. **Pass 1:** Complete structure scan and mapping of all sections, figures, tables, and algorithms
2. **Pass 2:** Section-by-section detailed extraction of all technical content
3. **Pass 3:** Cross-reference validation to ensure completeness
4. **Pass 4:** Deep technical understanding and context building

**Content Included:**
- Complete mathematical foundations (stochastic analysis for jump-diffusions)
- All model specifications (Merton model, term structure models, stochastic volatility models)
- Pricing theory and methods (risk-neutral pricing, PDE methods, Fourier methods)
- Hedging strategies (complete and incomplete markets)
- Computational algorithms and implementation guidance
- All formulas in LaTeX format
- Variable definitions and notation
- Best practices and common pitfalls

## How to Use When Building

### Method 1: Reference in Cursor Chat

Simply mention the MDC in your chat:

```
@jump-diffusion-models.mdc How do I implement a Merton jump-diffusion model for option pricing?
```

or

```
Using the jump-diffusion models MDC, help me calibrate jump parameters from market data.
```

### Method 2: Open in Cursor

1. Navigate to `quant-finance-engine/jump-diffusion-models/jump-diffusion-models.mdc`
2. Open the file in Cursor
3. Use Cursor's AI features to ask questions about specific sections
4. Copy relevant formulas, algorithms, or code patterns directly

### Method 3: Add to Cursor Rules

Add this to your `.cursorrules` or project configuration:

```markdown
When working on quantitative finance models involving jumps:
- Reference: quant-finance-engine/jump-diffusion-models/jump-diffusion-models.mdc
- Use Merton jump-diffusion model for asset pricing
- Implement risk-neutral pricing using characteristic functions
- Consider market incompleteness when hedging
```

### Method 4: Use Specific Sections

The MDC is organized into clear sections. You can reference specific parts:

- **Mathematical Foundations:** For stochastic calculus and measure theory
- **Market Models:** For model specifications (Merton, term structure, etc.)
- **Pricing Methods:** For option pricing algorithms
- **Hedging Strategies:** For risk management implementations
- **Implementation Checklist:** For step-by-step development guidance

**Example:**
```
I need to implement the generalized Itô formula for jump-diffusions. 
See the "Preliminaries: Stochastic Analysis" section in jump-diffusion-models.mdc
```

## Key Concepts

This MDC covers the following key concepts:

1. **Jump-Diffusion Processes:** Mathematical models combining continuous diffusion with discrete jumps
2. **Poisson Point Processes:** Stochastic processes modeling jump arrival times
3. **Marked Point Processes:** Point processes with associated jump sizes
4. **Martingale Measures:** Equivalent probability measures for risk-neutral pricing
5. **Market Price of Risk:** Risk premiums for diffusion and jump components
6. **Market Completion:** Methods to make incomplete markets complete
7. **Risk Minimization:** Hedging strategies for incomplete markets
8. **Merton Jump-Diffusion Model:** Specific model with normally distributed jumps
9. **Generalized Itô Formula:** Extension of Itô's lemma for jump-diffusions
10. **Girsanov Transformation:** Measure changes for jump-diffusion processes

## Quick Start

1. **For Option Pricing:**
   - Start with the Merton Jump-Diffusion Model section
   - Use the Risk-Neutral Pricing formula
   - Implement Monte Carlo or Fourier methods from Computational Aspects

2. **For Model Calibration:**
   - Review the Experimental Setup section
   - Use maximum likelihood or moment matching methods
   - Validate with out-of-sample data

3. **For Hedging:**
   - Check if market is complete (unique martingale measure)
   - Use delta hedging if complete
   - Use risk-minimizing strategies if incomplete

4. **For Implementation:**
   - Follow the Implementation Checklist
   - Start with basic Poisson process simulation
   - Build up to full jump-diffusion paths
   - Add pricing and hedging methods

## Contents

The MDC includes:

- **Paper Metadata:** Title, author, keywords, abstract
- **Problem Statement:** Motivation, challenges, scope
- **Key Concepts:** All major concepts and techniques
- **Related Work:** Previous approaches and how this differs
- **Preliminaries:** Complete stochastic analysis foundation
- **Market Models:** Merton model, term structure models, stochastic volatility
- **Martingale Measures:** Existence, uniqueness, market price of risk
- **Hedging:** Complete and incomplete market strategies
- **Pricing:** General theory and computational methods
- **Mathematical Foundations:** All formulas, notation, variable definitions
- **Implementation Guidance:** Checklists, best practices, pitfalls
- **References:** Key papers for further reading

## Related Resources

### Related MDCs

- **quant-finance-engine/quant-finance-engine.mdc:** Contains implementation of Merton jump-diffusion in the quantitative finance engine
- **science-maths/statistical-analysis-engine/:** For statistical methods and calibration techniques

### Original Paper

The original paper is a comprehensive survey/tutorial on jump-diffusion models in financial mathematics. This MDC extracts all actionable content for implementation.

### Additional Resources

- **Merton (1976):** Original jump-diffusion option pricing paper
- **Ball and Torous (1985):** Empirical evidence of jumps in stock prices
- **Bakshi, Cao, Chen (1997):** Empirical performance of jump-diffusion models

## Implementation Notes

### When to Use Jump-Diffusion Models

- Modeling assets with occasional large price movements
- Pricing options with volatility smiles/skews
- High-frequency trading applications
- Risk management for tail events
- Interest rate modeling with jumps

### Key Implementation Considerations

1. **Market Incompleteness:** Be aware that markets with jumps are typically incomplete
2. **Parameter Estimation:** More parameters than pure diffusion models
3. **Computational Cost:** More complex than Black-Scholes
4. **Calibration:** Requires sufficient market data (option prices, historical data)

### Common Use Cases

- **Option Pricing:** European and American options, exotic derivatives
- **Risk Management:** VaR calculations, stress testing
- **Portfolio Optimization:** Asset allocation with jump risk
- **Interest Rate Modeling:** Bond pricing, interest rate derivatives

## Success Criteria

This MDC is successful if:

- ✅ You can implement a Merton jump-diffusion model without reading the original paper
- ✅ You understand when and how to use jump-diffusion models
- ✅ You can price options using risk-neutral methods
- ✅ You can implement hedging strategies for complete and incomplete markets
- ✅ You understand the mathematical foundations (stochastic calculus, measure theory)
- ✅ You can calibrate model parameters from market data
- ✅ You know the computational methods (Monte Carlo, PDE, Fourier)

## Questions?

If you need clarification on any aspect of jump-diffusion models:

1. Check the relevant section in the MDC
2. Review the Mathematical Foundations for notation and formulas
3. Consult the Implementation Checklist for step-by-step guidance
4. Reference the Best Practices section for common issues
5. Look at the Related Techniques section for alternative approaches

---

**Last Updated:** Based on comprehensive extraction of Runggaldier's "Jump-Diffusion Models" paper

**Maintained By:** This MDC serves as a complete reference extracted from the academic paper following rigorous extraction protocols.






