# Student Management System with API Testing

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://img.shields.io/badge/pytest-7.4.3-green.svg)](https://pytest.org/)
[![Java](https://img.shields.io/badge/java-11+-orange.svg)](https://openjdk.java.net/)
[![React](https://img.shields.io/badge/react-18+-blue.svg)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack Student Management System with comprehensive API testing capabilities. This project includes a Java Spring Boot backend, React frontend, and Python-based API testing suite.

## 🚀 Quick Start

### For API Testing (Python):
```bash
git clone https://github.com/YoussefElHodaiby/Student-Project.git
cd Student-Project
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v
```

### For Backend (Java Spring Boot):
```bash
cd restassurd
mvn spring-boot:run
```

### For Frontend (React):
```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure

```
Student-Project/
├── 📂 Python API Testing Suite
│   ├── student_api.py          # API client classes
│   ├── test_student_api.py     # Pytest test cases
│   ├── postcall.py            # Legacy testing script
│   ├── conftest.py            # Pytest configuration
│   ├── pyproject.toml         # Project configuration
│   ├── requirements.txt       # Python dependencies
│   ├── run_tests.py           # Test runner script
│   └── reports/              # Test reports directory
│
├── 📂 Backend (Java Spring Boot)
│   ├── restassurd/
│   │   ├── src/main/java/callapi/
│   │   │   ├── StudentController.java
│   │   │   ├── BookController.java
│   │   │   ├── StudentService.java
│   │   │   └── BookService.java
│   │   └── pom.xml
│   └── data/                 # JSON data files
│
├── 📂 Frontend (React)
│   ├── src/components/
│   │   ├── StudentList.js
│   │   ├── AddStudent.js
│   │   ├── EditStudent.js
│   │   ├── BookList.js
│   │   └── AddBook.js
│   └── package.json
│
└── 📂 Configuration & Setup
    ├── .github/workflows/    # CI/CD workflows
    ├── setup_github.sh      # GitHub setup script
    └── README.md           # This file
```

## 🛠️ Setup & Installation

### Python API Testing Environment

1. **Create Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Java Backend Setup

1. **Prerequisites**: Java 11+ and Maven
2. **Run Backend**:
   ```bash
   cd restassurd
   mvn clean install
   mvn spring-boot:run
   ```
3. **API will be available at**: `http://localhost:8082`

### React Frontend Setup

1. **Prerequisites**: Node.js 14+
2. **Install and Run**:
   ```bash
   cd frontend
   npm install
   npm start
   ```
3. **Frontend will be available at**: `http://localhost:3000`

## 🧪 Running API Tests

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

## ✨ Test Features

- **Comprehensive pytest structure** with fixtures and test classes
- **Full CRUD operations testing** (Create, Read, Update, Delete)
- **Error handling** and HTTP status code validation
- **Random test data generation** for realistic testing
- **HTML test reports** for better visibility and CI/CD integration
- **Clean test isolation** with proper setup/teardown
- **Parallel test execution** support

## 🎯 API Endpoints Tested

### Student Management
- `POST /students` - Create new student
- `GET /students/{id}` - Get student by ID  
- `PUT /students/{id}` - Update student information
- `DELETE /students/{id}` - Delete student

### Book Management
- `POST /books` - Create new book
- `GET /books/{id}` - Get book by ID
- `PUT /books/{id}` - Update book information
- `DELETE /books/{id}` - Delete book

## ⚙️ Configuration

### API Testing Configuration
The API base URL is set to `http://localhost:8082` by default. You can modify this in:
- `student_api.py` - `StudentAPIClient` class
- `conftest.py` - `api_base_url` fixture

### Backend Configuration
- **Port**: 8082
- **Database**: JSON file-based storage
- **CORS**: Enabled for frontend integration

## 📋 Prerequisites

1. **For API Testing**: Python 3.8+, pip
2. **For Backend**: Java 11+, Maven
3. **For Frontend**: Node.js 14+, npm
4. **Make sure the backend server is running** on `http://localhost:8082` before running tests

## 📊 Test Reports

HTML test reports are generated in the `reports/` directory after running tests with the `--html` option. These reports include:
- Test execution summary
- Individual test results
- Error details and stack traces
- Execution time metrics

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🛠️ Technology Stack

- **Backend**: Java Spring Boot, Maven
- **Frontend**: React, JavaScript, HTML/CSS
- **API Testing**: Python, pytest, requests
- **CI/CD**: GitHub Actions
- **Documentation**: Swagger/OpenAPI
