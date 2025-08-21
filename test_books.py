"""
Test suite for Book API endpoints using pytest
"""
import pytest
from student_api import BookAPIClient, TestDataGenerator


class TestBookAPI:
    """Test class for Book API endpoints"""
    
    @pytest.fixture
    def api_client(self):
        """Fixture to provide Book API client instance"""
        return BookAPIClient()
    
    @pytest.fixture
    def test_data(self):
        """Fixture to provide test data generator"""
        return TestDataGenerator()
    
    def test_create_book(self, api_client, test_data):
        """Test creating a new book"""
        title = test_data.get_random_book_title()
        author = test_data.get_random_author()
        isbn = test_data.generate_isbn()
        
        # Create book
        response_data = api_client.create_book(title, author, isbn)
        
        # Assertions
        assert "id" in response_data
        assert "title" in response_data
        assert "author" in response_data
        assert response_data["title"] == title
        assert response_data["author"] == author
        if "isbn" in response_data:
            assert response_data["isbn"] == isbn
        
        # Cleanup
        book_id = response_data["id"]
        api_client.delete_book(book_id)
    
    def test_create_book_without_isbn(self, api_client, test_data):
        """Test creating a book without ISBN"""
        title = test_data.get_random_book_title()
        author = test_data.get_random_author()
        
        # Create book without ISBN
        response_data = api_client.create_book(title, author)
        
        # Assertions
        assert "id" in response_data
        assert "title" in response_data
        assert "author" in response_data
        assert response_data["title"] == title
        assert response_data["author"] == author
        
        # Cleanup
        book_id = response_data["id"]
        api_client.delete_book(book_id)
    
    def test_get_book(self, api_client, test_data):
        """Test retrieving a book by ID"""
        title = test_data.get_random_book_title()
        author = test_data.get_random_author()
        isbn = test_data.generate_isbn()
        
        # Create book first
        created_book = api_client.create_book(title, author, isbn)
        book_id = created_book["id"]
        
        # Get book
        retrieved_book = api_client.get_book(book_id)
        
        # Assertions
        assert retrieved_book["id"] == book_id
        assert retrieved_book["title"] == title
        assert retrieved_book["author"] == author
        if "isbn" in retrieved_book:
            assert retrieved_book["isbn"] == isbn
        
        # Cleanup
        api_client.delete_book(book_id)
    
    def test_update_book(self, api_client, test_data):
        """Test updating a book"""
        # Create initial book
        original_title = test_data.get_random_book_title()
        original_author = test_data.get_random_author()
        original_isbn = test_data.generate_isbn()
        created_book = api_client.create_book(original_title, original_author, original_isbn)
        book_id = created_book["id"]
        
        # Update book
        new_title = test_data.get_random_update_title()
        new_author = test_data.get_random_author()
        new_isbn = test_data.generate_isbn()
        updated_book = api_client.update_book(book_id, new_title, new_author, new_isbn)
        
        # Assertions
        assert updated_book["id"] == book_id
        assert updated_book["title"] == new_title
        assert updated_book["author"] == new_author
        if "isbn" in updated_book:
            assert updated_book["isbn"] == new_isbn
        
        # Verify the update persisted
        retrieved_book = api_client.get_book(book_id)
        assert retrieved_book["title"] == new_title
        assert retrieved_book["author"] == new_author
        
        # Cleanup
        api_client.delete_book(book_id)
    
    def test_update_book_without_isbn(self, api_client, test_data):
        """Test updating a book without providing ISBN"""
        # Create initial book
        original_title = test_data.get_random_book_title()
        original_author = test_data.get_random_author()
        created_book = api_client.create_book(original_title, original_author)
        book_id = created_book["id"]
        
        # Update book without ISBN
        new_title = test_data.get_random_update_title()
        new_author = test_data.get_random_author()
        updated_book = api_client.update_book(book_id, new_title, new_author)
        
        # Assertions
        assert updated_book["id"] == book_id
        assert updated_book["title"] == new_title
        assert updated_book["author"] == new_author
        
        # Cleanup
        api_client.delete_book(book_id)
    
    def test_delete_book(self, api_client, test_data):
        """Test deleting a book"""
        # Create book first
        title = test_data.get_random_book_title()
        author = test_data.get_random_author()
        created_book = api_client.create_book(title, author)
        book_id = created_book["id"]
        
        # Delete book
        status_code = api_client.delete_book(book_id)
        
        # Assertions
        assert status_code == 200 or status_code == 204  # Both are valid for successful deletion
        
        # Verify book is deleted (should return 404)
        status_code_after_delete = api_client.get_book_status_code(book_id)
        assert status_code_after_delete == 404
    
    def test_get_nonexistent_book(self, api_client):
        """Test getting a book that doesn't exist"""
        # Test with a book ID that likely doesn't exist
        nonexistent_id = 99999
        status_code = api_client.get_book_status_code(nonexistent_id)
        
        # Should return 404 for non-existent book
        assert status_code == 404
    
    def test_complete_book_crud_workflow(self, api_client, test_data):
        """Test complete CRUD workflow for books in sequence"""
        # CREATE
        title = test_data.get_random_book_title()
        author = test_data.get_random_author()
        isbn = test_data.generate_isbn()
        created_book = api_client.create_book(title, author, isbn)
        book_id = created_book["id"]
        
        assert created_book["title"] == title
        assert created_book["author"] == author
        
        # READ
        retrieved_book = api_client.get_book(book_id)
        assert retrieved_book["id"] == book_id
        assert retrieved_book["title"] == title
        assert retrieved_book["author"] == author
        
        # UPDATE
        new_title = test_data.get_random_update_title()
        new_author = test_data.get_random_author()
        new_isbn = test_data.generate_isbn()
        updated_book = api_client.update_book(book_id, new_title, new_author, new_isbn)
        
        assert updated_book["title"] == new_title
        assert updated_book["author"] == new_author
        
        # DELETE
        delete_status = api_client.delete_book(book_id)
        assert delete_status in [200, 204]
        
        # VERIFY DELETION
        final_status = api_client.get_book_status_code(book_id)
        assert final_status == 404
