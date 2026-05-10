# test_automation_candymapper

Selenium-based UI automation testing project for the **candymapper.com** website.  
The project was created as part of a **university course assignment** and demonstrates practical automation testing using **Python**, **Selenium WebDriver**, and the **unittest** framework, following the **Page Object Model (POM)** design pattern.

This repository contains automated UI tests for selected user-facing functionalities of the Candymapper website.

---

## What Is Covered

- Page Object Model (POM) structure for Candymapper pages
- Automated tests for the contact form on the Home Page
- User account-related flows (account creation and authentication)
- Input validation scenarios (positive and negative cases)
- Handling of dynamic web elements
- Separation of test logic, page logic, and test data
- Dynamic test data generation using Faker

The scope of testing may be extended with additional scenarios as the project evolves.

---

## Tech Stack

- Python 3.10+
- Selenium WebDriver
- unittest
- Faker
- Google Chrome / ChromeDriver

---

## Project Structure

```
test_automation_candymapper/
├── pages/                  # Page Object classes
│   ├── base_page.py
│   ├── home_page.py
│   ├── create_account_page.py
│   └── sign_in_page.py
├── tests/                  # Test cases
│   ├── base_test.py
│   ├── test_contact_form.py
│   └── test_authentication.py
├── test_data/               # Test data helpers (Faker-based)
├── requirements.txt         # Project dependencies
├── README.md
└── .gitignore
```

---

## Setup

Clone the repository and install dependencies:

```
git clone <repository_url>
cd test_automation_candymapper
pip install -r requirements.txt
```

---

## Run Tests

Run all tests from the project root directory:

```
python -m unittest discover
```

Run a specific test file:

```
python -m unittest tests/test_contact_form.py
```

---

## Design Pattern

The project follows the **Page Object Model (POM)** pattern:

- Page classes contain element locators and page-specific actions only
- Test classes contain test logic and assertions
- Test data generation is separated from test implementation

This design improves test readability, maintainability, and scalability.

---

## Notes

- Dynamic web elements are handled using stable selectors (e.g. `data-*` attributes)
- Faker is used to generate realistic input data
- The project focuses on UI behavior validation rather than backend testing


