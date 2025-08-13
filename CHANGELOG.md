# CHANGELOG

<!-- version list -->

## v1.3.0 (2025-08-13)

### Features

- Enhance GitHub Actions workflow to include Docker Buildx setup and configuration validation
  ([`58aea99`](https://github.com/Armgd/fireflyiii-mcp/commit/58aea99e49f501ec954cbee7f22b8514b6b900e3))


## v1.2.0 (2025-08-07)

### Chores

- **build.yaml**: Refactor GitHub Actions workflow for better tagging conventions and organization
  ([`6b8a9e5`](https://github.com/Armgd/fireflyiii-mcp/commit/6b8a9e5539a77838d156bb5120223c0c56bd7ab8))

- **ci**: Update Docker image name in GitHub Actions workflow to reflect correct repository name for
  building process
  ([`a71e5ca`](https://github.com/Armgd/fireflyiii-mcp/commit/a71e5ca38e222b02b85afa12b6b08ea7416dd9f3))

### Continuous Integration

- **workflow**: Enhance Docker build workflow for better tag management and conditional DockerHub
  login
  ([`cf54f11`](https://github.com/Armgd/fireflyiii-mcp/commit/cf54f11eaa4359f14bf5081431ca7d9466289dcc))

### Features

- **gemini**: Add Gemini CLI and related workflows for automated issue triage and PR review
  processes to improve repository maintenance efficiency.
  ([`841e0d9`](https://github.com/Armgd/fireflyiii-mcp/commit/841e0d957512be99b672ed27e675481ebf28a882))


## v1.1.0 (2025-07-15)

### Bug Fixes

- **pyproject.toml**: Update uv dependency version from 0.7.12 to 0.7.21 to ensure compatibility and
  receive bug fixes
  ([`184f0af`](https://github.com/Armgd/fireflyiii-mcp/commit/184f0afda1d5b1dba2bd3c16a6f71b20bdeb8d8e))

### Features

- **github**: Add a GitHub Actions workflow for linting with Ruff
  ([`c3c166d`](https://github.com/Armgd/fireflyiii-mcp/commit/c3c166d7d33750caacefad5e8e6b4d2826ed4383))

- **pyproject.toml**: Add dev dependency group for ruff to improve linting process
  ([`92d8ba4`](https://github.com/Armgd/fireflyiii-mcp/commit/92d8ba4f9ea3f81baf076c96af9b4dd9d115b690))


## v1.0.0 (2025-07-15)

- Initial Release
