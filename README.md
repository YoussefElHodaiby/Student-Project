# Student API Testing Project

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://img.shields.io/badge/pytest-7.4.3-green.svg)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project contains automated tests for a Student API using Python and pytest.

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/student-api-testing.git
cd student-api-testing
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v
```

## Project Structure

```
apicourse/
├── student_api.py          # API client classes
├── test_student_api.py     # Pytest test cases
├── postcall.py            # Legacy testing script (updated)
├── conftest.py            # Pytest configuration
├── pyproject.toml         # Project configuration
├── requirements.txt       # Python dependencies
├── run_tests.py           # Test runner script
├── reports/              # Test reports directory
└── README.md             # This file
```

## Setup

1. **Virtual Environment** (should already be created):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Using pytest directly:
```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run with HTML report
python -m pytest -v --html=reports/report.html --self-contained-html

# Run specific test file
python -m pytest test_student_api.py -v

# Run specific test
python -m pytest test_student_api.py::TestStudentAPI::test_create_student -v
```

### Using the test runner script:
```bash
python run_tests.py
```

### Using the legacy script:
```bash
python postcall.py
```

## Test Features

- **Proper pytest structure** with fixtures and test classes
- **CRUD operations testing** (Create, Read, Update, Delete)
- **Error handling** and status code validation
- **Data generation** with random test data
- **HTML test reports** for better visibility
- **Clean test isolation** with proper setup/teardown

## API Endpoints Tested

- `POST /students` - Create student
- `GET /students/{id}` - Get student by ID
- `PUT /students/{id}` - Update student
- `DELETE /students/{id}` - Delete student

## Configuration

The API base URL is set to `http://localhost:8082` by default. You can modify this in:
- `student_api.py` - `StudentAPIClient` class
- `conftest.py` - `api_base_url` fixture

## Prerequisites

Make sure your Student API server is running on `http://localhost:8082` before running the tests.

## Test Reports

HTML test reports are generated in the `reports/` directory after running tests with the `--html` option.
