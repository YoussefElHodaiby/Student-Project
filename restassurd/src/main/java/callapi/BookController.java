package callapi;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/books")
@Tag(name = "Book Controller", description = "Book management endpoints")
public class BookController {
    private final BookService bookService;

    @Autowired
    public BookController(BookService bookService) {
        this.bookService = bookService;
    }

    @Operation(summary = "Get all books", description = "Retrieves a list of all books in the system")
    @GetMapping
    public List<Book> getAllBooks() {
        return bookService.getAllBooks();
    }

    @Operation(summary = "Get book by ID", description = "Retrieves a specific book by its ID")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Book found"),
        @ApiResponse(responseCode = "404", description = "Book not found")
    })
    @GetMapping("/{id}")
    public ResponseEntity<Book> getBookById(@Parameter(description = "ID of the book") @PathVariable int id) {
        return bookService.getBookById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @Operation(summary = "Create new book", description = "Creates a new book in the system")
    @ApiResponse(responseCode = "200", description = "Book created successfully")
    @PostMapping
    public Book createBook(@RequestBody Book book) {
        return bookService.addBook(book);
    }

    @Operation(summary = "Update book", description = "Updates an existing book's information")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Book updated successfully"),
        @ApiResponse(responseCode = "404", description = "Book not found")
    })
    @PutMapping("/{id}")
    public ResponseEntity<Book> updateBook(
            @Parameter(description = "ID of the book to update") @PathVariable int id,
            @RequestBody Book book) {
        return bookService.editBook(id, book)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @Operation(summary = "Delete book", description = "Deletes a book from the system")
    @ApiResponses({
        @ApiResponse(responseCode = "204", description = "Book deleted successfully"),
        @ApiResponse(responseCode = "404", description = "Book not found")
    })
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteBook(@Parameter(description = "ID of the book to delete") @PathVariable int id) {
        return bookService.deleteBook(id) ? ResponseEntity.noContent().build() : ResponseEntity.notFound().build();
    }

    @Operation(summary = "Assign book to student", description = "Assigns a book to a specific student. Can also update book details during assignment.")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Book assigned successfully"),
        @ApiResponse(responseCode = "400", description = "Invalid book or student ID")
    })
    @PostMapping("/{bookId}/assign/{studentId}")
    public ResponseEntity<Book> assignBook(
            @Parameter(description = "ID of the book to assign") @PathVariable int bookId,
            @Parameter(description = "ID of the student") @PathVariable int studentId,
            @Parameter(description = "Updated book details (optional)") @RequestBody(required = false) Book bookDetails) {
        if (bookDetails != null) {
            bookService.editBook(bookId, bookDetails);
        }
        return bookService.assignBookToStudent(bookId, studentId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.badRequest().build());
    }

    @Operation(summary = "Unassign book", description = "Removes the assignment of a book from a student")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Book unassigned successfully"),
        @ApiResponse(responseCode = "400", description = "Invalid book ID")
    })
    @PostMapping("/{bookId}/unassign")
    public ResponseEntity<Book> unassignBook(
            @Parameter(description = "ID of the book to unassign") @PathVariable int bookId) {
        return bookService.unassignBook(bookId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.badRequest().build());
    }

    @Operation(summary = "Get books by student", description = "Retrieves all books assigned to a specific student")
    @GetMapping("/student/{studentId}")
    public List<Book> getBooksByStudent(
            @Parameter(description = "ID of the student") @PathVariable int studentId) {
        return bookService.getBooksByStudent(studentId);
    }
}
