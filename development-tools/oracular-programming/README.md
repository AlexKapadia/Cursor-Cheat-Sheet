# Oracular Programming: A Modular Foundation for Building LLM-Enabled Software

## What It Is

This MDC (Markdown Cursor) document is a comprehensive extraction and organization of the paper **"Oracular Programming: A Modular Foundation for Building LLM-Enabled Software"** by Jonathan Laurent and André Platzer.

This MDC provides:
- **Complete paradigm description** of oracular programming for integrating LLMs with traditional programs
- **Three-component architecture** (strategy, policy, demonstrations) with complete separation of concerns
- **Programming language design** for writing nondeterministic programs with LLM choice points
- **Implementation patterns** and code examples using the Delphyne framework
- **Mathematical foundations** and formal treatment
- **Best practices** for building reliable LLM-enabled software
- **Practical applications** including theorem proving and symbolic mathematics
- **Complete code examples** with Python/Delphyne implementations

The MDC is designed to serve as a complete reference for understanding and implementing oracular programming, enabling developers to build reliable, maintainable, and scalable software systems that integrate Large Language Models as computational components.

## How It Works

This MDC was created following a comprehensive extraction protocol that ensures:
- **Complete coverage** of all concepts, techniques, and architectural components
- **Accurate representation** of the original paper's content
- **Actionable information** that developers can use to implement oracular programs
- **Organized structure** for easy navigation and reference

The content is organized into logical sections:
- Problem statement and motivation for oracular programming
- Key concepts: strategies, policies, and demonstrations
- Methodology: how the three components work together
- Implementation patterns and architecture
- Code examples with Delphyne framework
- Mathematical foundations and formal treatment
- Best practices and common pitfalls
- Practical applications and use cases

**Note:** This MDC was created from available content. The original paper contains more formal language specifications and complete evaluation results. For complete implementation details, refer to the Delphyne framework documentation if available.

## How to Use When Building

### Method 1: Reference in Cursor Chat

When working on an LLM-integration project, reference this MDC in your Cursor chat:

```
@oracular-programming I'm building a system that uses LLMs to make decisions in a 
problem-solving pipeline. How should I structure it to separate core logic from 
search logic?
```

The AI will use the comprehensive content from this MDC to provide informed guidance on the oracular programming paradigm.

### Method 2: Open in Cursor

1. Open the MDC file directly in Cursor
2. Use Cursor's AI features to ask questions about specific sections
3. Copy relevant code examples or patterns
4. Reference architectural patterns and design principles

### Method 3: Add to Cursor Rules

Add this MDC to your Cursor Rules for automatic context:

1. Copy the MDC file path: `development-tools/oracular-programming/oracular-programming.mdc`
2. Add it to your `.cursorrules` file or Cursor settings
3. The AI will automatically have access to this knowledge when working on LLM-integration tasks

### Method 4: Use Specific Sections

Navigate directly to relevant sections:
- **Architecture Design:** See "Implementation Patterns" for component structure
- **Code Examples:** See "Code Examples and Snippets" for Delphyne implementations
- **Best Practices:** See "Best Practices and Recommendations" for guidelines
- **Mathematical Details:** See "Mathematical Foundations" for formal treatment

## Key Concepts

This MDC covers the core concepts of oracular programming:

1. **Strategy:** Nondeterministic programs with choice points that can be reified into search trees
2. **Policy:** Functions that navigate search trees using LLM oracles, with resource awareness
3. **Demonstrations:** Grounded, evolvable program components describing successful and unsuccessful navigation scenarios
4. **Choice Points:** Unresolved decision points in strategies resolved at runtime by LLMs
5. **Search Tree Reification:** Converting nondeterministic programs into explicit tree structures
6. **Opaque Space:** Abstraction that unifies strategies and queries from a policy's perspective
7. **Search Stream Protocol:** Resource-aware communication protocol for search algorithms
8. **Modular Composition:** Composing heterogeneous strategies while keeping policies independent
9. **Local Refinement:** Refining LLM queries into sub-strategies without global impact
10. **Resource Management:** Tracking and enforcing limits on LLM inference budgets

## Quick Start

1. **Understand the Paradigm:**
   - Read "Problem Statement" to understand why oracular programming is needed
   - Review "Key Concepts" to understand the three-component architecture
   - Study "Methodology and Approach" to see how components work together

2. **Design Your Strategy:**
   - Identify choice points where LLM decisions are needed
   - Define validation contracts for each critical step
   - Express problem decomposition as a nondeterministic program
   - See "Code Examples" for implementation patterns

3. **Design Your Policy:**
   - Choose or implement a search algorithm (depth-first, MCTS, etc.)
   - Define how to construct LLM prompts
   - Set up resource budgets and tracking
   - Review "Implementation Patterns" for policy design

4. **Collect Demonstrations:**
   - Gather examples of successful problem-solving scenarios
   - Include examples of failures with reasons
   - Organize by problem type and strategy
   - Use search reflection to generate new examples

5. **Implement and Test:**
   - Use Delphyne framework or implement your own
   - Start with simple examples
   - Test each component independently
   - Follow the "Implementation Checklist"

6. **Iterate and Improve:**
   - Update demonstrations based on search traces
   - Refine strategies based on results
   - Tune policies for better performance
   - Monitor resource usage

## Contents

The MDC includes:

- **Paper Metadata:** Title, authors, publication details
- **Abstract/Summary:** Complete abstract from the paper
- **Problem Statement:** Motivation, challenges, scope, assumptions
- **Key Concepts:** Comprehensive list of techniques and concepts
- **Related Work:** Previous approaches and how this differs
- **Methodology:** Three-component architecture and design principles
- **Algorithms:** Strategy reification, policy navigation, prompt construction
- **Implementation Patterns:** Architecture patterns and design patterns
- **Code Examples:** Complete Delphyne code examples with explanations
- **Mathematical Foundations:** Formulas, notation, variable definitions
- **Experimental Setup:** Delphyne implementation details and use cases
- **Results and Evaluation:** Key findings and performance characteristics
- **Best Practices:** Implementation guidelines and optimization tips
- **Limitations:** Stated limitations and assumptions
- **Related Techniques:** Cross-references to related approaches
- **Practical Applications:** Use cases including theorem proving and symbolic math
- **Implementation Checklist:** Step-by-step guidance
- **Appendices:** Additional code examples and learned advice
- **References:** Related work and techniques

## Related Resources

### Original Paper
- **Title:** Oracular Programming: A Modular Foundation for Building LLM-Enabled Software
- **Authors:** Jonathan Laurent (Carnegie Mellon University, USA and Karlsruhe Institute of Technology, Germany), André Platzer (Karlsruhe Institute of Technology, Germany)

### Implementation Framework
- **Delphyne:** The framework described in the paper for implementing oracular programs
- **VSCode Extension:** Development tool mentioned in the paper
- **Python-based:** Implementation uses Python with Delphyne library

### Related MDCs in This Repository

- **AI Integration Patterns** (`ai/`): General patterns for integrating AI in software
- **Development Methodologies** (`development-tools/`): Other software development approaches
- **Programming Paradigms:** Other programming language designs and paradigms

### Key Technologies Referenced

- **Lean 4:** Theorem prover used in examples
- **Mathlib:** Mathematical library for Lean
- **SymPy:** Python library for symbolic mathematics
- **Loogle:** Theorem search tool for Lean
- **LLM APIs:** Various LLM providers (OpenAI, Anthropic, etc.)

## Important Notes

1. **Content Completeness:** This MDC was created from available content. The full paper contains more formal language specifications and complete evaluation results. For complete implementation, refer to:
   - The original paper for complete language specifications
   - Delphyne framework documentation if available
   - The full reference list for related work

2. **Framework Availability:** Delphyne is described as a research prototype. Production use may require:
   - Additional features not covered in the paper
   - Framework maturity improvements
   - Integration with specific LLM providers
   - Performance optimizations

3. **Implementation Guidance:** While this MDC provides patterns and examples, specific implementations may require:
   - Access to Delphyne framework or implementing your own
   - Understanding of nondeterministic programming
   - Familiarity with LLM APIs and prompting
   - Domain-specific adaptations

4. **Use as Reference:** This MDC serves as a comprehensive reference and starting point. Combine with:
   - Domain knowledge for your specific problem
   - LLM provider documentation
   - Search algorithm expertise
   - Software engineering best practices

5. **Paradigm Adoption:** Oracular programming is a new paradigm. Consider:
   - Starting with simple examples
   - Understanding the separation of concerns
   - Iterating on demonstrations
   - Managing resources carefully

## Getting Help

If you need help using this MDC:
1. Reference specific sections in Cursor chat (e.g., "@oracular-programming How do I design a strategy?")
2. Ask about particular concepts (strategies, policies, demonstrations)
3. Request implementation guidance for your specific use case
4. Cross-reference with related MDCs in the repository
5. Review code examples for implementation patterns

## Example Use Cases

### Use Case 1: Automated Theorem Proving
- **Strategy:** Generate proof sketches, break into subgoals
- **Policy:** Depth-first search with backtracking
- **Demonstrations:** Examples of successful proof strategies
- **Result:** Automated proof generation in Lean

### Use Case 2: Symbolic Mathematics
- **Strategy:** Guess parameter values, validate constraints
- **Policy:** Simple depth-first search
- **Demonstrations:** Examples of correct parameter choices
- **Result:** Finding values that make expressions nonnegative

### Use Case 3: Code Generation
- **Strategy:** Identify refactoring opportunities
- **Policy:** Select transformations based on examples
- **Demonstrations:** Good and bad refactoring examples
- **Result:** Safe code refactoring with validation

---

**Last Updated:** Based on available paper content  
**Status:** Comprehensive extraction from available content  
**Recommended Use:** Reference guide for building LLM-enabled software using oracular programming paradigm  
**Framework:** Delphyne (research prototype)




