# AI Usage Notes

## AI Tool Used

- ChatGPT

## 1. AI-Assisted Components

AI was used as a development assistant during this assignment to:

- Brainstorm the overall FastAPI project structure.
- Suggest REST API endpoint organization.
- Generate initial templates for Pydantic models.
- Suggest implementations for JSON file storage.
- Provide examples for API validation.
- Suggest automated test cases using Pytest.
- Improve project documentation (README).

## 2. My Contributions

I reviewed and modified all AI-generated suggestions before including them in the project.

My own work included:

- Integrating all modules into a complete FastAPI application.
- Implementing and debugging the storage layer.
- Connecting API routes with the storage functions.
- Configuring JSON file persistence.
- Fixing compatibility issues related to the installed Python and Pydantic versions.
- Running and validating all API endpoints using Swagger UI.
- Writing, running, and expanding the automated test suite.
- Running Ruff to improve code quality and fixing reported issues.
- Verifying that the installation, server startup, and test commands work correctly.

## 3. Validation Performed

Before submission I verified the project by:

- Testing every endpoint manually using Swagger UI.
- Running the complete Pytest suite successfully.
- Checking API validation for invalid inputs.
- Confirming JSON data persistence.
- Running Ruff to ensure code quality.
- Confirming the project starts successfully using the commands documented in the README.

## 4. AI Suggestions Not Used

AI suggested using a database (SQLite/PostgreSQL) for data persistence.

I intentionally chose JSON file storage because the assignment explicitly states that a database is not required. This keeps the solution simple while fully satisfying the assignment requirements.

I also avoided adding features outside the requested scope so the implementation remains focused and maintainable.
