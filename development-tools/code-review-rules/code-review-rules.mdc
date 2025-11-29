# Code Review Rules and Guidelines

Review the changes on @branch:

## Data Flow and Architecture

- Think through how data flows in the app. Explain new patterns if they exist and why.
- Verify that data transformations maintain consistency and don't introduce unexpected side effects.
- Check for proper separation of concerns between layers (presentation, business logic, data access).
- Ensure that state management follows established patterns and doesn't create unnecessary complexity.

## Infrastructure and Deployment

- Were there any changes that could affect infrastructure?
- Check for hardcoded configuration values that should be environment variables.
- Verify that new services or dependencies are properly configured for all environments.
- Ensure that resource limits (memory, CPU, database connections) are considered.
- Check if new external API calls have proper rate limiting and retry logic.

## User Experience States

- Consider empty, loading, error, and offline states.
- Verify that error messages are user-friendly and actionable.
- Check that loading indicators don't block critical user interactions.
- Ensure that empty states provide helpful guidance to users.
- Verify that offline functionality degrades gracefully.

## Accessibility

- Review frontend changes for accessibility (keyboard navigation, focus management, ARIA roles, color contrast).
- Ensure all interactive elements are keyboard accessible.
- Verify that focus indicators are visible and logical.
- Check that form labels are properly associated with inputs.
- Ensure that color is not the only means of conveying information.
- Verify that images have appropriate alt text.
- Check that dynamic content changes are announced to screen readers.

## API Compatibility

- If public APIs have changed, ensure backwards compatibility (or increment API version).
- Verify that deprecated endpoints have proper migration paths.
- Check that API versioning follows established conventions.
- Ensure that breaking changes are documented and communicated.
- Verify that API responses maintain consistent structure.

## Dependencies

- Did we add any unnecessary dependencies? If there's a heavy dependency, could we inline a more minimal version?
- Check if new dependencies are actively maintained and secure.
- Verify that dependency versions are pinned appropriately.
- Ensure that peer dependencies are correctly specified.
- Check for duplicate dependencies that could be consolidated.

## Testing

- Did we add quality tests? Prefer fewer, high quality tests. Prefer integration tests for user flows.
- Verify that tests cover edge cases and error scenarios.
- Check that tests are deterministic and don't rely on timing or external state.
- Ensure that test setup and teardown are properly handled.
- Verify that tests follow the AAA pattern (Arrange, Act, Assert).
- Check that test names clearly describe what they're testing.

## Database and Schema Changes

- Were there schema changes which could require a database migration?
- Verify that migrations are reversible when possible.
- Check that migrations handle existing data appropriately.
- Ensure that indexes are added for frequently queried fields.
- Verify that foreign key constraints are properly defined.
- Check that schema changes don't break existing queries.

## Security

- Changes to auth flows or permissions? Run /security-review.
- Verify that sensitive data is not logged or exposed in error messages.
- Check that user input is properly validated and sanitised.
- Ensure that authentication tokens are handled securely.
- Verify that authorisation checks are performed at the appropriate level.
- Check for SQL injection, XSS, and CSRF vulnerabilities.
- Ensure that secrets and API keys are not committed to version control.

## Feature Flags

- If feature flags are set up, does this change require adding a new one?
- Verify that feature flags have appropriate default values.
- Check that feature flag logic is testable and doesn't create technical debt.
- Ensure that feature flags are documented and have removal plans.

## Internationalisation

- If i18n is set up, are the strings added localised and new routes internationalised?
- Verify that all user-facing text uses i18n functions.
- Check that date, time, and number formats respect locale settings.
- Ensure that RTL languages are supported if applicable.
- Verify that translated strings are complete and accurate.

## Performance and Caching

- Are there places we should use caching?
- Check for N+1 query problems in database access.
- Verify that expensive computations are memoised or cached appropriately.
- Ensure that pagination is implemented for large data sets.
- Check that images and assets are optimised and properly sized.
- Verify that API responses are appropriately sized and don't include unnecessary data.

## Observability

- Are we missing critical observability or logging on backend changes?
- Verify that errors are logged with sufficient context for debugging.
- Check that important business events are tracked appropriately.
- Ensure that performance metrics are captured for critical paths.
- Verify that log levels are appropriate (debug, info, warn, error).
- Check that sensitive information is not included in logs.

## Code Quality

- Verify that code follows established style guidelines and conventions.
- Check that functions and classes have appropriate names and responsibilities.
- Ensure that complex logic is well-commented and explained.
- Verify that code is DRY (Don't Repeat Yourself) without over-abstracting.
- Check that error handling is comprehensive and consistent.
- Ensure that code is readable and maintainable by other team members.

## Documentation

- Verify that new features or significant changes are documented.
- Check that README files are updated if setup or usage has changed.
- Ensure that API documentation is updated for new endpoints.
- Verify that complex algorithms or business logic have inline comments.

## Git and Version Control

- Check that commit messages are clear and descriptive.
- Verify that related changes are grouped logically in commits.
- Ensure that merge conflicts are resolved correctly.
- Check that the branch is up to date with the main branch.
- Verify that unnecessary files (logs, build artifacts) are not committed.

---

**Remember:** Code reviews are collaborative. Be constructive, specific, and kind. Focus on improving code quality while maintaining team morale.

