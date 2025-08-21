"""
Student API Client for testing API endpoints
"""
import requests
import random
from typing import Dict, Any


class StudentAPIClient:
    """Client for interacting with the Student API"""
    
    def __init__(self, base_url: str = "http://localhost:8082"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def create_student(self, name: str, age: int) -> Dict[str, Any]:
        """Create a new student"""
        payload = {"name": name, "age": age}
        response = self.session.post(f"{self.base_url}/students", json=payload)
        response.raise_for_status()
        return response.json()
    
    def get_student(self, student_id: int) -> Dict[str, Any]:
        """Get a student by ID"""
        response = self.session.get(f"{self.base_url}/students/{student_id}")
        response.raise_for_status()
        return response.json()
    
    def update_student(self, student_id: int, name: str, age: int) -> Dict[str, Any]:
        """Update a student"""
        payload = {"name": name, "age": age}
        response = self.session.put(f"{self.base_url}/students/{student_id}", json=payload)
        response.raise_for_status()
        return response.json()
    
    def delete_student(self, student_id: int) -> int:
        """Delete a student and return status code"""
        response = self.session.delete(f"{self.base_url}/students/{student_id}")
        return response.status_code
    
    def get_student_status_code(self, student_id: int) -> int:
        """Get status code for student request (for testing 404s)"""
        response = self.session.get(f"{self.base_url}/students/{student_id}")
        return response.status_code


class TestDataGenerator:
    """Generate test data for API testing"""
    
    NAMES = ["hady", "mahmoud", "omar", "zein", "mourad", "ismail", "ahmed", "aly", "yehia"]
    UPDATE_NAMES = ["ahmed", "aly", "yehia", "khaled", "ismail"]
    UPDATE_AGES = [25, 30, 35, 40, 45]
    
    @classmethod
    def get_random_name(cls) -> str:
        """Get a random name for creating students"""
        return random.choice(cls.NAMES)
    
    @classmethod
    def get_random_update_name(cls) -> str:
        """Get a random name for updating students"""
        return random.choice(cls.UPDATE_NAMES)
    
    @classmethod
    def get_random_update_age(cls) -> int:
        """Get a random age for updating students"""
        return random.choice(cls.UPDATE_AGES)
