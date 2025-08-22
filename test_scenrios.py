# test_scenrios.py
import pytest
import requests
import random

base_url_books = "http://localhost:8082/api/books"
base_url_students = "http://localhost:8082/students"
base_url_assign = "http://localhost:8082/api/books/4/assign/4"



@pytest.fixture
def create_student():
    # generate a random name to avoid duplicates
    names = ["hady", "mahmoud", "omar", "zein", "mourad", "ismail", "ahmed", "aly", "yehia"]
    random_name = random.choice(names)
    request_payload = {
        "name": random_name,
        "age": 35
    }
    response = requests.post(base_url_students, json=request_payload)
    assert response.status_code == 201

    data = response.json()
    recieved_id = data["id"]
    recieved_name = data["name"]

    print("New ID is:", recieved_id)

    # return both ID and name so the GET test can use them
    return recieved_id, recieved_name


def test_create_student():
    """Test creating a new student"""
    names = ["hady", "mahmoud", "omar", "zein", "mourad", "ismail", "ahmed", "aly", "yehia"]
    random_name = random.choice(names)
    request_payload = {
        "name": random_name,
        "age": 35
    }
    
    response = requests.post(base_url_students, json=request_payload)
    print(f"Create student response: {response.text}")
    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == random_name
    assert data["age"] == 35
    assert "assignedBookIds" in data
    
    print(f"Successfully created student with ID: {data['id']}")


def test_get_student_by_id(create_student):

    student_id, random_name = create_student

    response = requests.get(base_url_students + "/" + str(student_id))
    print(response.text)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == random_name


def test_assign_book_to_student(create_student):
    """Test assigning book 4 to a student"""
    student_id, random_name = create_student
    
    # Use the assignment URL format with the received student ID
    assign_url = f"http://localhost:8082/api/books/4/assign/{student_id}"
    
    response = requests.post(assign_url)
    print(f"Assignment URL: {assign_url}")
    print(f"Response: {response.text}")
    assert response.status_code == 200 or response.status_code == 201
    
    data = response.json()
    assert "id" in data
    assert "bookName" in data
    assert "studentId" in data
    assert "studentName" in data
    assert "assignedDate" in data
    
    # Verify the assignment worked
    assert data["studentId"] == student_id
    assert data["studentName"] == random_name


def test_create_book():
    """Test creating a new book"""
    request_payload_newbook = {
        "bookName": "TEST"
    }
    response = requests.post(base_url_books, json=request_payload_newbook)
    print(f"Create book response: {response.text}")
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    assert data["bookName"] == "TEST"
    print(f"Successfully created book with ID: {data['id']}")