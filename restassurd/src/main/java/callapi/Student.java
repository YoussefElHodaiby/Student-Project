package callapi;

import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.util.ArrayList;
import java.util.List;

public class Student {
    private int id;
    
    @NotBlank(message = "Name is required")
    private String name;
    
    @NotNull(message = "Age is required")
    @Min(value = 16, message = "Age must be at least 16")
    private Integer age;
    
    private List<Integer> assignedBookIds;

    public Student() {
        this.assignedBookIds = new ArrayList<>();
    }
    
    public Student(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.assignedBookIds = new ArrayList<>();
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
    public List<Integer> getAssignedBookIds() { return assignedBookIds; }
    public void setAssignedBookIds(List<Integer> assignedBookIds) { this.assignedBookIds = assignedBookIds; }
}
