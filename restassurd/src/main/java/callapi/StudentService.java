package callapi;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class StudentService {
    private final String FILE_PATH = "/Users/youssefelhodaiby/restapi/restassurd/data/students.json";
    private final ObjectMapper mapper = new ObjectMapper();
    private List<Student> initialStudents;

    public StudentService() {
        // Initialize with dummy data
        initialStudents = new ArrayList<>();
        initialStudents.add(new Student(1, "John Doe", 20));
        initialStudents.add(new Student(2, "Jane Smith", 21));
        initialStudents.add(new Student(3, "Mike Johnson", 19));
        initialStudents.add(new Student(4, "Sarah Williams", 22));
        // Save initial data to file
        saveAllStudents(initialStudents);
    }

    public List<Student> getAllStudents() {
        try {
            File file = new File(FILE_PATH);
            if (!file.exists()) {
                return initialStudents;
            }
            return mapper.readValue(file, new TypeReference<List<Student>>() {});
        } catch (Exception e) {
            return initialStudents;
        }
    }

    public Optional<Student> getStudentById(int id) {
        List<Student> students = getAllStudents();
        return students.stream()
                .filter(s -> s.getId() == id)
                .findFirst();
    }

    public void saveAllStudents(List<Student> students) {
        try {
            File file = new File(FILE_PATH);
            file.getParentFile().mkdirs(); // Create the data directory if it doesn't exist
            mapper.writeValue(file, students);
        } catch (Exception e) {
            System.err.println("Error saving students: " + e.getMessage());
        }
    }

    public Student addStudent(Student student) {
        List<Student> students = getAllStudents();
        student.setId(students.size() + 1);
        students.add(student);
        saveAllStudents(students);
        return student;
    }

    public Optional<Student> editStudent(int id, Student updated) {
        List<Student> students = getAllStudents();
        for (Student s : students) {
            if (s.getId() == id) {
                s.setName(updated.getName());
                s.setAge(updated.getAge());
                saveAllStudents(students);
                return Optional.of(s);
            }
        }
        return Optional.empty();
    }

    public boolean deleteStudent(int id) {
        List<Student> students = getAllStudents();
        boolean removed = students.removeIf(s -> s.getId() == id);
        if (removed) saveAllStudents(students);
        return removed;
    }

    public void addBookToStudent(int studentId, int bookId) {
        List<Student> students = getAllStudents();
        for (Student student : students) {
            if (student.getId() == studentId) {
                if (!student.getAssignedBookIds().contains(bookId)) {
                    student.getAssignedBookIds().add(bookId);
                    saveAllStudents(students);
                }
                break;
            }
        }
    }

    public void removeBookFromStudent(int studentId, int bookId) {
        List<Student> students = getAllStudents();
        for (Student student : students) {
            if (student.getId() == studentId) {
                student.getAssignedBookIds().remove(Integer.valueOf(bookId));
                saveAllStudents(students);
                break;
            }
        }
    }
}
