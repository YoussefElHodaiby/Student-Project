# Book Management API

This project is a simple Book Management API built using Spring Boot. It allows users to manage books, including creating, assigning to students, retrieving, updating, and deleting books.

## Project Structure

```
restassurd
├── src
│   └── main
│       └── java
│           └── callapi
│               ├── Book.java          # Defines the Book class with properties and validation
│               ├── BookService.java   # Contains business logic for managing books
│               ├── BookController.java # Handles HTTP requests for book operations
│               └── Application.java    # Entry point for the Spring Boot application
├── pom.xml                             # Maven configuration file for dependencies and build
└── README.md                            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd restassurd
   ```

2. **Build the project:**
   Make sure you have Maven installed. Run the following command to build the project:
   ```
   mvn clean install
   ```

3. **Run the application:**
   You can run the application using the following command:
   ```
   mvn spring-boot:run
   ```

## API Endpoints

### Create a Book
- **POST** `/books`
- Request Body: 
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "isbn": "ISBN Number"
  }
  ```

### Assign a Book to a Student
- **POST** `/books/{id}/assign`
- Path Variable: `id` (Book ID)
- Request Body:
  ```json
  {
    "studentId": 1
  }
  ```

### Retrieve a Book
- **GET** `/books/{id}`
- Path Variable: `id` (Book ID)

### Update a Book
- **PUT** `/books/{id}`
- Path Variable: `id` (Book ID)
- Request Body:
  ```json
  {
    "title": "Updated Title",
    "author": "Updated Author",
    "isbn": "Updated ISBN"
  }
  ```

### Delete a Book
- **DELETE** `/books/{id}`
- Path Variable: `id` (Book ID)

## Usage Examples

- To create a new book, send a POST request to `/books` with the required fields.
- To retrieve a book, send a GET request to `/books/{id}` where `{id}` is the ID of the book you want to retrieve.

## Dependencies

This project uses the following dependencies:
- Spring Boot
- Jakarta Validation
- Maven

## License

This project is licensed under the MIT License.