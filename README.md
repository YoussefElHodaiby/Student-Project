# Student Management System with API Testing

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://img.shields.io/badge/pytest-7.4.3-green.svg)](https://pytest.org/)
[![Java](https://img.shields.io/badge/java-11+-orange.svg)](https://openjdk.java.net/)
[![React](https://img.shields.io/badge/react-18+-blue.svg)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack Student Management System with comprehensive API testing capabilities. This project includes a Java Spring Boot backend, React frontend, and Python-based API testing suite.

## 🚀 Getting Started

### Prerequisites
- **Python 3.13+** 
- **Java 17+** (for backend API)
- **Maven** (for Java build)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YoussefElHodaiby/Student-Project.git
   cd Student-Project
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend API** (Java Spring Boot)
   ```bash
   cd restassurd
   mvn spring-boot:run
   ```
   API will be available at `http://localhost:8082`

4. **Run the tests**
   ```bash
   # Run all tests
   pytest

   # Run specific test files
   pytest test_student.py
   pytest test_books.py  
   pytest test_scenrios.py

   # Run with verbose output
   pytest -v
   ```

## 📁 Project Structure

```
Student-Project/
├── 📂 Python API Testing Suite
│   ├── test_student.py         # Student API tests (GET, POST, validation)
│   ├── test_books.py          # Book API tests (CRUD operations)
│   ├── test_scenrios.py       # End-to-end scenario tests (create student → assign book)
│   ├── pyproject.toml         # Project configuration
│   ├── requirements.txt       # Python dependencies
│   └── reports/               # Test reports directory
│
├── 📂 Backend (Java Spring Boot)
│   ├── restassurd/
│   │   ├── src/main/java/callapi/
│   │   │   ├── StudentController.java
│   │   │   ├── BookController.java
│   │   │   ├── StudentService.java
│   │   │   └── BookService.java
│   │   └── pom.xml
│   └── data/                  # JSON data files
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
    ├── setup_github.sh       # GitHub setup script
    └── README.md             # This file
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

## 🧪 Testing Approach

This project uses **pytest** with direct HTTP requests for API testing:

- **Direct API Calls**: Uses `requests` library for straightforward HTTP requests
- **Simple Assertions**: Clear, readable test validation without complex frameworks
- **Scenario-Based Testing**: End-to-end workflows testing complete user journeys
- **Random Test Data**: Dynamic test data generation for robust testing

### Test Categories
1. **Unit Tests**: Individual API endpoint validation
2. **Integration Tests**: Cross-service functionality testing  
3. **End-to-End Tests**: Complete user workflow scenarios

## ✨ Test Features

- **Simple pytest structure** with direct HTTP requests
- **API operations testing** (Create, Read, Update, Assignment)
- **HTTP status code validation** and response verification
- **Random test data generation** for realistic testing
- **End-to-end scenario testing** with student-book assignment workflows
- **Clean test isolation** with proper setup/teardown
- **Parallel test execution** support

## 🎯 API Endpoints Tested

### Student Management (`test_student.py`)
- `GET /students` - Get all students
- `POST /students` - Create new student
- `GET /students/{id}` - Get student by ID

### Book Management (`test_books.py`)
- `GET /api/books` - Get all books
- `GET /api/books/{id}` - Get book by ID
- `POST /api/books` - Create new book
- `PUT /api/books/{id}` - Update book

### End-to-End Scenarios (`test_scenrios.py`)
- `POST /students` - Create new student
- `GET /students/{id}` - Retrieve created student
- `POST /api/books/{bookId}/assign/{studentId}` - Assign book to student

## ⚙️ Configuration

### API Testing Configuration
The API base URL is set to `http://localhost:8082` by default. You can modify this in the test files:
- `test_student.py` - `base_url` variable
- `test_books.py` - `base_url` variable  
- `test_scenrios.py` - endpoint URLs

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
