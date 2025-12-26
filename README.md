# Playwright E2E Test

Compact Playwright (Python, async) end-to-end test suite for opensource-demo.orangehrmlive.com with Allure reporting and Docker support.

Quick start
1. git clone https://github.com/OleksandrSava/Playwright_E2E_Test.git
2. cd Playwright_E2E_Test
3. python -m venv .venv && source .venv/bin/activate
4. pip install -r requirements.txt
5. Run tests: pytest -q

Run with Docker
- docker-compose up --build

Common commands
- Run all tests: pytest
- Run folder/file: pytest tests/
- Run single test: pytest tests/test_example.py::test_login
- Allure report: pytest --alluredir=reports/allure

Key env vars
- BASE_URL — application URL (default: opensource-demo.orangehrmlive.com)
- PLAYWRIGHT_HEADLESS — true|false
- BROWSER — chromium|firefox|webkit
- CI — set in CI environments

Project layout
- tests/ — test cases
- pages/ — Page Objects
- fixtures/, utils/, reports/, requirements.txt, conftest.py, docker-compose.yml

Notes
- Designed for local, Docker, or CI execution. Allure and JUnit artifacts supported.
- Add LICENSE and CONTRIBUTING.md if you want to present the repo for job applications.
