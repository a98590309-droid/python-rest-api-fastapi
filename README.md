# REST API with Comprehensive Tests

A REST API built using FastAPI featuring Pydantic data modeling, automated Swagger documentation, and automated test suites.

## Features
- **4 Fully-Typed Endpoints:** GET `/items`, GET `/items/{id}`, POST `/items`, DELETE `/items/{id}`.
- **Pydantic Validation:** Type enforcement with sensible HTTP 422 error payloads for malformed requests.
- **Auto-Generated Documentation:** Interactive OpenAPI/Swagger docs at `/docs` and ReDoc at `/redoc`.
- **Test Suite:** Pytest coverage for successful flows, validation errors, and 404 edge cases.
-
