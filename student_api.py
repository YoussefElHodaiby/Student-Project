"""
Student and Book API Clients for testing API endpoints
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


class BookAPIClient:
    """Client for interacting with the Book API"""
    
    def __init__(self, base_url: str = "http://localhost:8082"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def create_book(self, title: str, author: str, isbn: str = None) -> Dict[str, Any]:
        """Create a new book"""
        payload = {"title": title, "author": author}
        if isbn:
            payload["isbn"] = isbn
        response = self.session.post(f"{self.base_url}/books", json=payload)
        response.raise_for_status()
        return response.json()
    
    def get_book(self, book_id: int) -> Dict[str, Any]:
        """Get a book by ID"""
        response = self.session.get(f"{self.base_url}/books/{book_id}")
        response.raise_for_status()
        return response.json()
    
    def update_book(self, book_id: int, title: str, author: str, isbn: str = None) -> Dict[str, Any]:
        """Update a book"""
        payload = {"title": title, "author": author}
        if isbn:
            payload["isbn"] = isbn
        response = self.session.put(f"{self.base_url}/books/{book_id}", json=payload)
        response.raise_for_status()
        return response.json()
    
    def delete_book(self, book_id: int) -> int:
        """Delete a book and return status code"""
        response = self.session.delete(f"{self.base_url}/books/{book_id}")
        return response.status_code
    
    def get_book_status_code(self, book_id: int) -> int:
        """Get status code for book request (for testing 404s)"""
        response = self.session.get(f"{self.base_url}/books/{book_id}")
        return response.status_code


class TestDataGenerator:
    """Generate test data for API testing"""
    
    # Student data
    NAMES = ["hady", "mahmoud", "omar", "zein", "mourad", "ismail", "ahmed", "aly", "yehia"]
    UPDATE_NAMES = ["ahmed", "aly", "yehia", "khaled", "ismail"]
    UPDATE_AGES = [25, 30, 35, 40, 45]
    
    # Book data
    BOOK_TITLES = [
        "The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice",
        "The Catcher in the Rye", "Lord of the Flies", "Animal Farm", "Brave New World",
        "Jane Eyre", "Wuthering Heights", "The Lord of the Rings", "Harry Potter"
    ]
    
    AUTHORS = [
        "F. Scott Fitzgerald", "Harper Lee", "George Orwell", "Jane Austen",
        "J.D. Salinger", "William Golding", "Aldous Huxley", "Charlotte Brontë",
        "Emily Brontë", "J.R.R. Tolkien", "J.K. Rowling", "Mark Twain"
    ]
    
    UPDATE_TITLES = [
        "Updated Book Title", "Revised Edition", "Second Edition", "New Version",
        "Updated Work", "Revised Work"
    ]
    
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
    
    @classmethod
    def get_random_book_title(cls) -> str:
        """Get a random book title"""
        return random.choice(cls.BOOK_TITLES)
    
    @classmethod
    def get_random_author(cls) -> str:
        """Get a random author name"""
        return random.choice(cls.AUTHORS)
    
    @classmethod
    def get_random_update_title(cls) -> str:
        """Get a random title for updating books"""
        return random.choice(cls.UPDATE_TITLES)
    
    @classmethod
    def generate_isbn(cls) -> str:
        """Generate a random ISBN-like string"""
        return f"978-{random.randint(1000000000, 9999999999)}"
