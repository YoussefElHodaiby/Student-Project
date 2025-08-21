import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function StudentList() {
  const [students, setStudents] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      const response = await axios.get('http://localhost:8082/students');
      setStudents(response.data);
    } catch (err) {
      setError('Error fetching students');
      console.error('Error:', err);
    }
  };

  const deleteStudent = async (id) => {
    if (window.confirm('Are you sure you want to delete this student?')) {
      try {
        await axios.delete(`http://localhost:8082/students/${id}`);
        fetchStudents(); // Refresh the list
      } catch (err) {
        setError('Error deleting student');
        console.error('Error:', err);
      }
    }
  };

  return (
    <div>
      <h2>Students</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {students.map(student => (
            <tr key={student.id}>
              <td>{student.id}</td>
              <td>{student.name}</td>
              <td>{student.age}</td>
              <td>
                <Link to={`/edit/${student.id}`} className="btn btn-primary btn-sm me-2">Edit</Link>
                <button onClick={() => deleteStudent(student.id)} className="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <Link to="/add" className="btn btn-success">Add New Student</Link>
    </div>
  );
}

export default StudentList;
