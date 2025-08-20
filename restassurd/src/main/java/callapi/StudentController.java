package callapi;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import javax.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/students")
@CrossOrigin(origins = "http://localhost:3000")
@Tag(name = "Student Management", description = "APIs for managing student records")
public class StudentController {

    @Autowired
    private StudentService service;

    @Operation(summary = "Get all students", description = "Retrieves a list of all students")
    @ApiResponse(responseCode = "200", description = "List of students retrieved successfully")
    @GetMapping
    public ResponseEntity<List<Student>> getAll() {
        return ResponseEntity.ok(service.getAllStudents());
    }

    @Operation(summary = "Get student by ID", description = "Retrieves a student by their ID")
    @ApiResponses(value = {
        @ApiResponse(responseCode = "200", description = "Student found successfully"),
        @ApiResponse(responseCode = "404", description = "Student not found",
                    content = @Content(schema = @Schema(implementation = ApiError.class)))
    })
    @GetMapping("/{id}")
    public ResponseEntity<Student> getById(@PathVariable int id) {
        return service.getStudentById(id)
                .map(ResponseEntity::ok)
                .orElseThrow(() -> new StudentNotFoundException("Student not found with id: " + id));
    }

    @Operation(summary = "Create a new student", description = "Creates a new student record")
    @ApiResponses(value = {
        @ApiResponse(responseCode = "201", description = "Student created successfully"),
        @ApiResponse(responseCode = "400", description = "Invalid input", 
                    content = @Content(schema = @Schema(implementation = ApiError.class)))
    })
    @PostMapping
    public ResponseEntity<Student> create(@Valid @RequestBody Student student) {
        return new ResponseEntity<>(service.addStudent(student), HttpStatus.CREATED);
    }

    @Operation(summary = "Update a student", description = "Updates an existing student's information")
    @ApiResponses(value = {
        @ApiResponse(responseCode = "200", description = "Student updated successfully"),
        @ApiResponse(responseCode = "404", description = "Student not found", 
                    content = @Content(schema = @Schema(implementation = ApiError.class))),
        @ApiResponse(responseCode = "400", description = "Invalid input", 
                    content = @Content(schema = @Schema(implementation = ApiError.class)))
    })
    @PutMapping("/{id}")
    public ResponseEntity<Student> edit(@PathVariable int id, @Valid @RequestBody Student student) {
        return service.editStudent(id, student)
                .map(ResponseEntity::ok)
                .orElseThrow(() -> new StudentNotFoundException("Student not found with id: " + id));
    }

    @Operation(summary = "Delete a student", description = "Deletes a student by their ID")
    @ApiResponses(value = {
        @ApiResponse(responseCode = "204", description = "Student deleted successfully"),
        @ApiResponse(responseCode = "404", description = "Student not found", 
                    content = @Content(schema = @Schema(implementation = ApiError.class)))
    })
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable int id) {
        if (!service.deleteStudent(id)) {
            throw new StudentNotFoundException("Student not found with id: " + id);
        }
        return ResponseEntity.noContent().build();
    }
}
