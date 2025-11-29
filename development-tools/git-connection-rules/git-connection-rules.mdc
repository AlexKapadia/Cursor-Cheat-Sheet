# Git Connection and Rules Guide

## Initial Git Setup

### Configure Your Identity

Before making your first commit, configure your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Verify Configuration

```bash
git config --list
```

## Connecting to Remote Repositories

### Clone an Existing Repository

```bash
git clone <repository-url>
```

### Add a Remote Repository

```bash
git remote add origin <repository-url>
```

### Verify Remote Connection

```bash
git remote -v
```

### Update Remote URL

```bash
git remote set-url origin <new-repository-url>
```

## Authentication Methods

### SSH Keys (Recommended)

1. **Generate SSH Key:**
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

2. **Add SSH Key to SSH Agent:**
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

3. **Copy Public Key:**
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

4. **Add to Git Provider:** Copy the public key and add it to your GitHub/GitLab/Bitbucket account settings.

### Personal Access Token (HTTPS)

1. Generate a personal access token from your Git provider.
2. Use the token as your password when prompted.
3. Store credentials securely:
   ```bash
   git config --global credential.helper store
   ```

## Git Workflow Rules

### Branch Naming Conventions

*   Use descriptive branch names that indicate the purpose.
*   Prefix with feature type: `feature/`, `bugfix/`, `hotfix/`, `refactor/`
*   Use kebab-case: `feature/user-authentication`
*   Include ticket numbers when applicable: `feature/PROJ-123-add-login`

### Commit Message Rules

#### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

*   `feat`: New feature
*   `fix`: Bug fix
*   `docs`: Documentation changes
*   `style`: Code style changes (formatting, no logic change)
*   `refactor`: Code refactoring
*   `test`: Adding or updating tests
*   `chore`: Maintenance tasks

#### Examples

```
feat(auth): add user login functionality

Implement email/password authentication with JWT tokens.
Add validation for email format and password strength.

Closes #123
```

```
fix(api): resolve null pointer exception in user service

The getUserById method was throwing NPE when user not found.
Added null check and proper error handling.

Fixes #456
```

#### Commit Message Best Practices

*   Write the subject line in imperative mood: "Add feature" not "Added feature" or "Adds feature"
*   Keep subject line under 50 characters
*   Capitalise the first letter of the subject
*   Don't end the subject with a period
*   Use the body to explain what and why, not how
*   Reference issues and pull requests in the footer
*   Write each commit message in present tense

### Branching Strategy

#### Main Branches

*   `main` or `master`: Production-ready code
*   `develop`: Integration branch for features

#### Feature Branches

*   Branch from `develop`
*   Merge back to `develop` when complete
*   Delete after merging

#### Hotfix Branches

*   Branch from `main`
*   Merge to both `main` and `develop`
*   Delete after merging

### Pull Request Rules

#### Before Creating a PR

*   Ensure all tests pass
*   Update documentation if needed
*   Rebase on the target branch
*   Write a clear PR description

#### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests pass
```

## Daily Git Workflow

### Starting Work

1. **Update local branches:**
   ```bash
   git fetch origin
   git checkout develop
   git pull origin develop
   ```

2. **Create feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### During Development

1. **Stage changes:**
   ```bash
   git add <file>
   # or
   git add .
   ```

2. **Commit changes:**
   ```bash
   git commit -m "feat(scope): descriptive message"
   ```

3. **Push to remote:**
   ```bash
   git push origin feature/your-feature-name
   ```

### Before Pushing

*   Review your changes: `git diff`
*   Check status: `git status`
*   Ensure commits are logical and atomic
*   Don't commit commented-out code
*   Don't commit temporary files or build artifacts

## File Management Rules

### .gitignore Best Practices

Always include:

*   IDE configuration files (`.idea/`, `.vscode/`)
*   Build outputs (`dist/`, `build/`, `*.class`)
*   Dependencies (`node_modules/`, `venv/`)
*   Environment files (`.env`, `.env.local`)
*   OS files (`.DS_Store`, `Thumbs.db`)
*   Log files (`*.log`)

### Never Commit

*   Secrets or API keys
*   Personal configuration files
*   Large binary files (use Git LFS if needed)
*   Generated files
*   Database files
*   Cache directories

## Merge and Rebase Rules

### When to Merge

*   Merging feature branches into main branches
*   Preserving complete history
*   Public branches shared with others

### When to Rebase

*   Cleaning up local commit history
*   Before creating a pull request
*   Updating feature branch with latest changes

### Rebase Workflow

```bash
git fetch origin
git rebase origin/develop
```

**Never rebase shared/public branches.**

## Conflict Resolution

### When Conflicts Occur

1. **Identify conflicted files:**
   ```bash
   git status
   ```

2. **Open and resolve conflicts** in your editor

3. **Mark as resolved:**
   ```bash
   git add <resolved-file>
   ```

4. **Complete the merge/rebase:**
   ```bash
   git commit  # for merge
   # or
   git rebase --continue  # for rebase
   ```

### Conflict Resolution Best Practices

*   Communicate with team members about conflicts
*   Understand both sides of the conflict
*   Test thoroughly after resolving
*   Don't just accept one side blindly

## Code Review Rules

### As a Reviewer

*   Review within 24 hours when possible
*   Be constructive and respectful
*   Ask questions rather than making demands
*   Approve when code meets standards
*   Request changes with clear explanations

### As an Author

*   Respond to all review comments
*   Make requested changes or explain why not
*   Don't take feedback personally
*   Keep PRs focused and reasonably sized
*   Update PR when changes are made

## Security Rules

### Authentication

*   Use SSH keys instead of passwords when possible
*   Rotate credentials regularly
*   Don't share credentials
*   Use personal access tokens with minimal required permissions

### Repository Access

*   Follow principle of least privilege
*   Review repository access regularly
*   Remove access when team members leave
*   Use branch protection rules for main branches

### Sensitive Data

*   Never commit secrets, passwords, or API keys
*   Use environment variables or secret management tools
*   If secrets are committed, rotate them immediately
*   Consider using tools like `git-secrets` or `truffleHog`

## Troubleshooting

### Common Issues

**Undo last commit (keep changes):**
```bash
git reset --soft HEAD~1
```

**Undo last commit (discard changes):**
```bash
git reset --hard HEAD~1
```

**Undo changes to a file:**
```bash
git checkout -- <file>
```

**View commit history:**
```bash
git log --oneline --graph --all
```

**Find when a bug was introduced:**
```bash
git bisect start
git bisect bad
git bisect good <commit-hash>
```

## Best Practices Summary

1. **Commit often, push regularly:** Small, frequent commits are easier to review and debug.
2. **Write clear commit messages:** Future you (and your team) will thank you.
3. **Keep branches focused:** One feature or fix per branch.
4. **Test before committing:** Don't commit broken code.
5. **Pull before pushing:** Stay up to date with remote changes.
6. **Use meaningful branch names:** Make it clear what each branch does.
7. **Review your own code:** Check `git diff` before committing.
8. **Keep main branch stable:** Only merge tested, reviewed code.
9. **Document complex changes:** Use commit body for explanations.
10. **Follow team conventions:** Consistency helps everyone.

---

**Remember:** Git is a tool for collaboration. Clear communication through commit messages, PR descriptions, and code reviews makes the entire team more productive.

