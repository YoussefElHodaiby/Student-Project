package callapi;

import javax.validation.constraints.NotBlank;

public class Book {
    private int id;
    
    @NotBlank(message = "Book name is required")
    private String bookName;
    
    private Integer studentId;  // The ID of the student who has been assigned this book
    
    private String studentName;  // Name of the student who has been assigned this book
    
    private java.time.LocalDateTime assignedDate;  // Date when the book was assigned

    public Book() {}
    
    public Book(int id, String bookName) {
        this.id = id;
        this.bookName = bookName;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getBookName() { return bookName; }
    public void setBookName(String bookName) { this.bookName = bookName; }
    public Integer getStudentId() { return studentId; }
    public void setStudentId(Integer studentId) { this.studentId = studentId; }
    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }
    public java.time.LocalDateTime getAssignedDate() { return assignedDate; }
    public void setAssignedDate(java.time.LocalDateTime assignedDate) { this.assignedDate = assignedDate; }
}
