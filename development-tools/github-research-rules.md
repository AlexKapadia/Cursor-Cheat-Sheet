# GitHub Research and Solution Search Rules

When extracting data from GitHub and searching for solutions to problems, follow these comprehensive rules to ensure accurate, reliable, and ethical research practices.

## Search Strategy and Query Formulation

- **Use specific, targeted search queries** that include relevant keywords, error messages, and technology stack information.
- **Search for exact error messages** when troubleshooting, using quotes to find precise matches.
- **Combine multiple search approaches**: code search, issue search, and repository search to get comprehensive results.
- **Use GitHub's advanced search syntax** (language filters, date ranges, stars, forks) to narrow results to high-quality sources.
- **Search for both the problem and the solution** to find discussions, pull requests, and commits that address similar issues.
- **Look for closed issues** that were resolved, as they often contain the actual solution.
- **Search across multiple repositories** when a problem might be framework or library-specific.
- **Use alternative search terms** if initial searches don't yield results (synonyms, related technologies, or broader categories).

## Repository Evaluation and Quality Assessment

- **Prioritise repositories with active maintenance**: recent commits, open issues being addressed, and responsive maintainers.
- **Check repository statistics**: star count, fork count, and contributor activity as indicators of community trust and usage.
- **Review repository documentation** (README, CONTRIBUTING, documentation folders) to understand project structure and conventions.
- **Verify repository license** and ensure it's compatible with your intended use before extracting code.
- **Assess code quality** by examining code style, test coverage, and overall project organisation.
- **Check for security advisories** or known vulnerabilities in the repository or its dependencies.
- **Look for official or verified repositories** when possible, especially for popular libraries or frameworks.
- **Evaluate repository age and stability**: newer repositories might have breaking changes, while older ones might use outdated patterns.

## Code Extraction and Analysis

- **Extract complete, working examples** rather than partial code snippets that might be missing context.
- **Understand the full context** of extracted code: read surrounding code, comments, and related files.
- **Verify code compatibility** with your project's versions, dependencies, and architecture before using it.
- **Check for dependencies and requirements** that the extracted code relies on.
- **Look for tests or examples** that demonstrate how the code should be used.
- **Extract code from the correct branch or tag** that matches your needs (main, latest release, specific version).
- **Review commit history** to understand why code was written or changed, which provides valuable context.
- **Check for related pull requests** that might show alternative approaches or discussions about the implementation.
- **Verify that extracted code follows security best practices** and doesn't introduce vulnerabilities.

## Solution Verification and Validation

- **Cross-reference solutions** from multiple sources to verify their correctness and applicability.
- **Test solutions in a safe environment** before applying them to production code.
- **Check solution dates and versions** to ensure they're relevant to your current technology stack.
- **Look for solutions that have been accepted or merged** rather than just proposed.
- **Verify that solutions address the root cause** and not just symptoms of the problem.
- **Check for follow-up comments** that indicate whether a solution worked for others.
- **Look for official documentation** that confirms or contradicts the solution approach.
- **Validate solutions against your specific use case** rather than assuming they'll work universally.
- **Check for breaking changes or deprecations** that might affect the solution's viability.

## Issue and Discussion Analysis

- **Read entire issue threads** to understand the full context, not just the initial problem description.
- **Look for workarounds and temporary fixes** when permanent solutions aren't available.
- **Identify patterns in similar issues** that might indicate a broader problem or common pitfall.
- **Check for maintainer responses** or official guidance on the issue.
- **Review closed issues** to see how problems were ultimately resolved.
- **Look for related issues** that might provide additional context or alternative solutions.
- **Check issue labels** (bug, feature, documentation) to understand the nature of the problem.
- **Verify issue status**: open issues might not have solutions yet, while closed issues should have resolutions.

## Pull Request and Commit Analysis

- **Review pull request descriptions and discussions** to understand the reasoning behind code changes.
- **Check code reviews and feedback** in pull requests to identify potential issues or improvements.
- **Examine commit messages** for context about why changes were made.
- **Look for related commits** that might show the evolution of a solution.
- **Verify that pull requests were merged** and are part of the main codebase.
- **Check for revert commits** that might indicate a solution didn't work as expected.
- **Review file changes** in pull requests to understand the full scope of modifications.
- **Look for test files** in pull requests that demonstrate expected behaviour.

## Documentation and Examples

- **Prioritise official documentation** over third-party examples when available.
- **Check for code examples in documentation** that demonstrate proper usage patterns.
- **Look for migration guides** when dealing with version upgrades or breaking changes.
- **Review changelogs and release notes** for information about fixes, new features, or deprecations.
- **Check for tutorials or guides** in repository wikis or documentation folders.
- **Look for example projects or demos** that show complete implementations.
- **Verify documentation is up to date** by checking last update dates and comparing with code changes.

## Security and Safety Considerations

- **Never extract or use code that contains hardcoded secrets, API keys, or credentials.**
- **Verify that solutions don't introduce security vulnerabilities** (SQL injection, XSS, authentication bypasses).
- **Check for security advisories** related to the code or dependencies you're considering.
- **Review authentication and authorisation** patterns in extracted code to ensure they're secure.
- **Avoid using code from untrusted or unmaintained repositories** for security-critical functionality.
- **Verify dependency versions** for known security vulnerabilities.
- **Check for proper input validation and sanitisation** in extracted code.
- **Review error handling** to ensure sensitive information isn't exposed.

## Attribution and Licensing

- **Respect repository licenses** and ensure compliance with terms when using extracted code.
- **Provide attribution** when using code from other repositories, following the license requirements.
- **Document sources** of extracted code or solutions for future reference and compliance.
- **Understand license implications** (MIT, GPL, Apache, etc.) before incorporating code.
- **Check for license compatibility** between your project and the source repository.
- **Maintain license notices** when required by the source license.

## Best Practices for Solution Implementation

- **Adapt solutions to your codebase** rather than copying code verbatim without understanding.
- **Refactor extracted code** to match your project's coding standards and architecture.
- **Add appropriate error handling** and validation when implementing solutions.
- **Write tests** for solutions you implement to ensure they work correctly.
- **Document the source** of solutions in code comments for future reference.
- **Consider the long-term maintainability** of solutions, not just immediate fixes.
- **Evaluate performance implications** of solutions, especially for high-traffic or resource-intensive operations.
- **Check for alternative solutions** that might be more appropriate for your specific context.

## Version and Compatibility Checking

- **Verify version compatibility** between your project and the solution's target version.
- **Check for version-specific solutions** when dealing with breaking changes between versions.
- **Look for migration paths** when solutions are for different versions than your current setup.
- **Verify dependency versions** required by solutions are compatible with your project.
- **Check for deprecated features** that might affect solution viability.
- **Review version history** to understand when solutions were created and if they're still relevant.

## Context and Domain Understanding

- **Understand the problem domain** before searching for solutions to ensure you're looking in the right places.
- **Consider framework or library-specific solutions** when working within a particular ecosystem.
- **Look for solutions that match your architecture** (monolith vs microservices, server-side vs client-side, etc.).
- **Check for platform-specific considerations** (operating system, runtime environment, deployment target).
- **Understand the trade-offs** of different solutions, not just their immediate benefits.
- **Consider scalability and performance** implications of solutions for your use case.

## Quality Indicators

- **Favour solutions with high community engagement**: multiple upvotes, comments, or confirmations that they work.
- **Prioritise solutions from maintainers or core contributors** when available.
- **Look for solutions that are well-documented** with clear explanations and examples.
- **Prefer solutions that follow best practices** and established patterns in the community.
- **Check for solutions that have been tested** or have accompanying test code.
- **Look for solutions that are actively maintained** or have recent updates.

## Avoiding Common Pitfalls

- **Don't blindly copy code** without understanding how it works and why it solves the problem.
- **Avoid using outdated solutions** that might not work with current versions or might introduce security issues.
- **Don't ignore error messages or warnings** in extracted code; investigate and resolve them.
- **Avoid solutions that violate best practices** or introduce technical debt.
- **Don't use solutions without testing** them in your specific environment and use case.
- **Avoid solutions that are overly complex** when simpler alternatives exist.
- **Don't ignore license requirements** or attribution needs when using extracted code.
- **Avoid solutions that create dependencies** on unmaintained or problematic libraries.

## Documentation and Note-Taking

- **Document the source URLs** of solutions you find for future reference.
- **Note the context and assumptions** under which solutions were found to work.
- **Record version information** for solutions to help with future compatibility checks.
- **Keep notes on why solutions were chosen** over alternatives for future decision-making.
- **Document any modifications** made to extracted solutions to adapt them to your needs.
- **Maintain a record of solutions tried** that didn't work, to avoid repeating unsuccessful attempts.

## Multi-Source Verification

- **Cross-reference solutions** from GitHub with official documentation, Stack Overflow, and other sources.
- **Verify solutions work** by checking multiple implementations or examples.
- **Look for consensus** among multiple sources about the best approach to a problem.
- **Check for conflicting information** and investigate which source is more authoritative or up to date.
- **Validate solutions** against official documentation or maintainer guidance when available.

## Ethical and Legal Considerations

- **Respect intellectual property rights** and license terms when using code from GitHub.
- **Don't extract or use code** that appears to be proprietary or confidential.
- **Follow responsible disclosure practices** if you discover security vulnerabilities in code you're researching.
- **Respect repository owners' guidelines** for code usage and contribution.
- **Don't use code** that violates terms of service or ethical guidelines.

## Efficiency and Time Management

- **Start with the most likely sources** (official repos, popular libraries) before exploring niche solutions.
- **Use GitHub's search filters effectively** to narrow results quickly.
- **Bookmark useful repositories** and solutions for future reference.
- **Create a systematic approach** to searching and evaluating solutions to avoid redundant work.
- **Know when to stop searching** and start implementing; perfect solutions might not exist.

---

**Remember:** GitHub is a valuable resource, but solutions should always be verified, tested, and adapted to your specific context. Prioritise understanding over copying, quality over speed, and security over convenience. When in doubt, consult official documentation, test thoroughly, and seek additional verification from multiple sources.

