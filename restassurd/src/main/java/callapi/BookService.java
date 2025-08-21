package callapi;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class BookService {
    private final String FILE_PATH = "/Users/youssefelhodaiby/restapi/restassurd/data/books.json";
    private final ObjectMapper mapper = new ObjectMapper();
    private final StudentService studentService;
    private List<Book> initialBooks;

    public BookService(StudentService studentService) {
        this.studentService = studentService;
        initialBooks = new ArrayList<>();
        // Add some initial books
        initialBooks.add(new Book(1, "Clean Code"));
        initialBooks.add(new Book(2, "Design Patterns"));
        saveAllBooks(initialBooks);
    }

    public List<Book> getAllBooks() {
        try {
            File file = new File(FILE_PATH);
            List<Book> books;
            if (!file.exists()) {
                books = initialBooks;
            } else {
                books = mapper.readValue(file, new TypeReference<List<Book>>() {});
            }
            // Update student names from current student data
            for (Book book : books) {
                if (book.getStudentId() != null) {
                    studentService.getStudentById(book.getStudentId()).ifPresent(student -> {
                        book.setStudentName(student.getName());
                        // Ensure the book is in student's assigned books
                        if (!student.getAssignedBookIds().contains(book.getId())) {
                            studentService.addBookToStudent(student.getId(), book.getId());
                        }
                    });
                }
            }
            return books;
        } catch (Exception e) {
            return initialBooks;
        }
    }

    public Optional<Book> getBookById(int id) {
        return getAllBooks().stream()
                .filter(b -> b.getId() == id)
                .findFirst();
    }

    public List<Book> getBooksByStudent(int studentId) {
        return getAllBooks().stream()
                .filter(b -> studentId == (b.getStudentId() != null ? b.getStudentId() : -1))
                .toList();
    }



    public Book addBook(Book book) {
        List<Book> books = getAllBooks();
        book.setId(books.size() + 1);
        books.add(book);
        saveAllBooks(books);
        return book;
    }

    public Optional<Book> editBook(int id, Book updated) {
        List<Book> books = getAllBooks();
        for (Book b : books) {
            if (b.getId() == id) {
                b.setBookName(updated.getBookName());
                // Don't update studentId or assignedDate through edit
                saveAllBooks(books);
                return Optional.of(b);
            }
        }
        return Optional.empty();
    }

    public boolean deleteBook(int id) {
        List<Book> books = getAllBooks();
        boolean removed = books.removeIf(b -> b.getId() == id);
        if (removed) {
            saveAllBooks(books);
        }
        return removed;
    }

    public Optional<Book> assignBookToStudent(int bookId, int studentId) {
        // Verify both book and student exist
        Optional<Book> bookOpt = getBookById(bookId);
        Optional<Student> studentOpt = studentService.getStudentById(studentId);
        if (bookOpt.isEmpty() || studentOpt.isEmpty()) {
            return Optional.empty();
        }
        
        Book book = bookOpt.get();
        Student student = studentOpt.get();
        
        // Check if book is already assigned to another student
        if (book.getStudentId() != null && !book.getStudentId().equals(studentId)) {
            // Unassign from previous student
            studentService.removeBookFromStudent(book.getStudentId(), bookId);
        }
        
        book.setStudentId(studentId);
        book.setStudentName(student.getName());
        book.setAssignedDate(java.time.LocalDateTime.now());
        
        // Update the student's assigned books
        studentService.addBookToStudent(studentId, bookId);
        
        List<Book> books = getAllBooks();
        for (int i = 0; i < books.size(); i++) {
            if (books.get(i).getId() == bookId) {
                books.set(i, book);
                saveAllBooks(books);
                return Optional.of(book);
            }
        }
        return Optional.empty();
    }

    public Optional<Book> unassignBook(int bookId) {
        Optional<Book> bookOpt = getBookById(bookId);
        if (bookOpt.isEmpty()) {
            return Optional.empty();
        }

        Book book = bookOpt.get();
        Integer studentId = book.getStudentId();
        if (studentId != null) {
            studentService.removeBookFromStudent(studentId, bookId);
        }
        book.setStudentId(null);
        book.setStudentName(null);
        book.setAssignedDate(null);
        
        List<Book> books = getAllBooks();
        for (int i = 0; i < books.size(); i++) {
            if (books.get(i).getId() == bookId) {
                books.set(i, book);
                saveAllBooks(books);
                return Optional.of(book);
            }
        }
        return Optional.empty();
    }

    private void saveAllBooks(List<Book> books) {
        try {
            File file = new File(FILE_PATH);
            file.getParentFile().mkdirs();
            mapper.writeValue(file, books);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
