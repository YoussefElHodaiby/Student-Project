"""
Test suite for Student API using pytest
"""
import pytest
from student_api import StudentAPIClient, TestDataGenerator


class TestStudentAPI:
    """Test class for Student API endpoints"""
    
    @pytest.fixture
    def api_client(self):
        """Fixture to provide API client instance"""
        return StudentAPIClient()
    
    @pytest.fixture
    def test_data(self):
        """Fixture to provide test data"""
        return TestDataGenerator()
    
    def test_create_student(self, api_client, test_data):
        """Test creating a new student"""
        name = test_data.get_random_name()
        age = 35
        
        # Create student
        response_data = api_client.create_student(name, age)
        
        # Assertions
        assert "id" in response_data
        assert "name" in response_data
        assert response_data["name"] == name
        assert response_data["age"] == age
        
        # Cleanup
        student_id = response_data["id"]
        api_client.delete_student(student_id)
    
    def test_get_student(self, api_client, test_data):
        """Test retrieving a student by ID"""
        name = test_data.get_random_name()
        age = 35
        
        # Create student first
        created_student = api_client.create_student(name, age)
        student_id = created_student["id"]
        
        # Get student
        retrieved_student = api_client.get_student(student_id)
        
        # Assertions
        assert retrieved_student["id"] == student_id
        assert retrieved_student["name"] == name
        assert retrieved_student["age"] == age
        
        # Cleanup
        api_client.delete_student(student_id)
    
    def test_update_student(self, api_client, test_data):
        """Test updating a student"""
        # Create initial student
        original_name = test_data.get_random_name()
        original_age = 35
        created_student = api_client.create_student(original_name, original_age)
        student_id = created_student["id"]
        
        # Update student
        new_name = test_data.get_random_update_name()
        new_age = test_data.get_random_update_age()
        updated_student = api_client.update_student(student_id, new_name, new_age)
        
        # Assertions
        assert updated_student["id"] == student_id
        assert updated_student["name"] == new_name
        assert updated_student["age"] == new_age
        
        # Verify the update persisted
        retrieved_student = api_client.get_student(student_id)
        assert retrieved_student["name"] == new_name
        assert retrieved_student["age"] == new_age
        
        # Cleanup
        api_client.delete_student(student_id)
    
    def test_delete_student(self, api_client, test_data):
        """Test deleting a student"""
        # Create student first
        name = test_data.get_random_name()
        age = 35
        created_student = api_client.create_student(name, age)
        student_id = created_student["id"]
        
        # Delete student
        status_code = api_client.delete_student(student_id)
        
        # Assertions
        assert status_code == 200 or status_code == 204  # Both are valid for successful deletion
        
        # Verify student is deleted (should return 404)
        status_code_after_delete = api_client.get_student_status_code(student_id)
        assert status_code_after_delete == 404
    
    def test_get_nonexistent_student(self, api_client):
        """Test getting a student that doesn't exist"""
        # Test with a student ID that likely doesn't exist
        nonexistent_id = 99999
        status_code = api_client.get_student_status_code(nonexistent_id)
        
        # Should return 404 for non-existent student
        assert status_code == 404
    
    def test_complete_crud_workflow(self, api_client, test_data):
        """Test complete CRUD workflow in sequence"""
        # CREATE
        name = test_data.get_random_name()
        age = 35
        created_student = api_client.create_student(name, age)
        student_id = created_student["id"]
        
        assert created_student["name"] == name
        assert created_student["age"] == age
        
        # READ
        retrieved_student = api_client.get_student(student_id)
        assert retrieved_student["id"] == student_id
        assert retrieved_student["name"] == name
        
        # UPDATE
        new_name = test_data.get_random_update_name()
        new_age = test_data.get_random_update_age()
        updated_student = api_client.update_student(student_id, new_name, new_age)
        
        assert updated_student["name"] == new_name
        assert updated_student["age"] == new_age
        
        # DELETE
        delete_status = api_client.delete_student(student_id)
        assert delete_status in [200, 204]
        
        # VERIFY DELETION
        final_status = api_client.get_student_status_code(student_id)
        assert final_status == 404
