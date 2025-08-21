"""
Pytest configuration and shared fixtures
"""
import pytest


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for the API"""
    return "http://localhost:8082"


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment before each test"""
    # Add any setup code here if needed
    yield
    # Add any cleanup code here if needed
