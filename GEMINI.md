## Project Overview

This project is a Python-based Model-Context-Protocol (MCP) server for Firefly III, a personal finance manager. It utilizes the `fastmcp` library to expose a selection of the Firefly III API endpoints as tools and resources that can be consumed by AI models and other MCP-compatible clients.

The server is designed to be run in a Docker container and comes with a `Dockerfile` and `compose.yaml` for easy setup. The main application logic is contained in `main.py`, which initializes the `fastmcp` server and defines the routes to be exposed from the Firefly III API.

## Building and Running

The project uses `uv` for dependency management.

**To set up the development environment:**

1.  Create a virtual environment and install dependencies:
    ```bash
    uv venv
    uv sync
    ```
2.  Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
3. Create a `.env` file in the root of the project with the following content:
    ```
    FIREFLY_III_URL="http://your-firefly-iii-instance.com"
    FIREFLY_III_ACCESS_TOKEN="your_personal_access_token"
    ```
4.  Run the development server:
    ```bash
    fastmcp dev main.py
    ```
The server will be available at `http://localhost:8000`.

**To run the application with Docker:**

1.  Create a `.env` file as described above.
2.  Run the following command:
    ```bash
    docker compose up -d
    ```


**To run tests (TODO):**

The project does not currently have a test suite.

## Development Conventions

*   **Linting and Formatting:** The project uses `ruff` for linting and formatting. You can run the linter with `ruff check .` and the formatter with `ruff format .`.
*   **Dependency Management:** The project uses `uv` for dependency management. To add a new dependency, add it to the `pyproject.toml` file and run `uv lock`.
*   **Versioning and Releases:** The project uses `python-semantic-release` for automated versioning and releases. Commits should follow the Conventional Commits specification.
