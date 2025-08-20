package callapi;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class BookService {
    private final List<Book> books = new ArrayList<>();
    private int currentId = 1;

    public Book createBook(String title, String author, String isbn) {
        Book book = new Book(currentId++, title, author, isbn);
        books.add(book);
        return book;
    }

    public void assignBookToStudent(int bookId, Integer studentId) {
        Optional<Book> bookOptional = books.stream()
                .filter(book -> book.getId() == bookId)
                .findFirst();
        bookOptional.ifPresent(book -> book.setStudentId(studentId));
    }

    public Optional<Book> getBook(int bookId) {
        return books.stream()
                .filter(book -> book.getId() == bookId)
                .findFirst();
    }

    public Optional<Book> updateBook(int bookId, String title, String author, String isbn) {
        Optional<Book> bookOptional = getBook(bookId);
        bookOptional.ifPresent(book -> {
            book.setTitle(title);
            book.setAuthor(author);
            book.setIsbn(isbn);
        });
        return bookOptional;
    }

    public boolean deleteBook(int bookId) {
        return books.removeIf(book -> book.getId() == bookId);
    }
}