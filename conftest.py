"""
Pytest configuration and shared fixtures for Student and Book API testing
"""
import pytest
from student_api import StudentAPIClient, BookAPIClient, TestDataGenerator


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for the API"""
    return "http://localhost:8082"


@pytest.fixture(scope="session")
def student_api_client(api_base_url):
    """Session-scoped Student API client fixture"""
    return StudentAPIClient(api_base_url)


@pytest.fixture(scope="session")
def book_api_client(api_base_url):
    """Session-scoped Book API client fixture"""
    return BookAPIClient(api_base_url)


@pytest.fixture(scope="session")
def test_data_generator():
    """Session-scoped test data generator fixture"""
    return TestDataGenerator()


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment before each test"""
    # Add any setup code here if needed
    yield
    # Add any cleanup code here if needed
