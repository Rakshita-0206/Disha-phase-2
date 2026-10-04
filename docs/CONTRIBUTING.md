# Contributing Guidelines

Thank you for contributing to Disha Phase 2!

## 1. Branching Strategy
* `main`: Stable production-ready branch deployed to Render.
* `crawler`: Development branch for web crawlers, institute scrapers, and data ingestion pipelines.
* `feature/*`: Short-lived feature branches for scoped enhancements.

## 2. Commit Message Standards
We follow the [Conventional Commits](https://www.conventionalcommits.org/) convention:
* `feat`: A new user-facing capability or API endpoint.
* `fix`: A bug fix or patch.
* `docs`: Documentation, architecture guides, and API specs.
* `style`: Code style, formatting, docstring alignment without logic changes.
* `refactor`: Internal code reorganization preserving existing behavior.
* `perf`: Performance improvements and algorithmic speedups.
* `test`: Adding or updating test suites.
* `chore`: Maintenance tasks, dependencies, and changelog updates.

## 3. Pull Request Requirements
1. Ensure all Python code conforms to PEP 8 standards.
2. Verify that FastAPI application boots successfully without dependency warnings.
3. Update relevant sections in `docs/` and `CHANGELOG.md`.
