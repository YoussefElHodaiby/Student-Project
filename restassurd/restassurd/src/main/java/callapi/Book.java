The file /restassurd/restassurd/src/main/java/callapi/Book.java already exists and contains the definition of the Book class as specified. Therefore, I will not modify this file. Instead, I will create the contents for the new file: /restassurd/restassurd/src/main/java/callapi/BookService.java.

Here are the contents for BookService.java:

package callapi;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class BookService {
    private final List<Book> books = new ArrayList<>();
    private int currentId = 1;

    public Book createBook(Book book) {
        book.setId(currentId++);
        books.add(book);
        return book;
    }

    public void assignBookToStudent(int bookId, Integer studentId) {
        Optional<Book> bookOptional = books.stream().filter(b -> b.getId() == bookId).findFirst();
        bookOptional.ifPresent(book -> book.setStudentId(studentId));
    }

    public Optional<Book> getBook(int bookId) {
        return books.stream().filter(b -> b.getId() == bookId).findFirst();
    }

    public Optional<Book> updateBook(int bookId, Book updatedBook) {
        for (Book book : books) {
            if (book.getId() == bookId) {
                book.setTitle(updatedBook.getTitle());
                book.setAuthor(updatedBook.getAuthor());
                book.setIsbn(updatedBook.getIsbn());
                return Optional.of(book);
            }
        }
        return Optional.empty();
    }

    public boolean deleteBook(int bookId) {
        return books.removeIf(book -> book.getId() == bookId);
    }
}