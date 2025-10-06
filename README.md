Welcome to the Auto-Test project, built using the Playwright testing framework(Async mode).

This repository includes full E2E test for opensource-demo.orangehrmlive.com, featuring:

Allure Reports for detailed and visually appealing test result summaries.

A Dockerfile and docker-compose.yml to easily set up and run tests in isolated, consistent environments.

Fully configured CI/CD pipelines that automatically execute tests to ensure continuous quality and reliability.


Installation and Setup

1. Clone the Repository
   
git clone https://github.com/OleksandrSava/Playwright_E2E_Test.git
cd Playwright_E2E_Test

2. Install Python Dependencies

pip install -r requirements.txt

4. Running Tests Locally
-Simply run:

pytest

-Running Tests Using Docker:

docker-compose up --build

