import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function BookList() {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    loadBooks();
  }, []);

  const loadBooks = async () => {
    try {
      const result = await axios.get('http://localhost:8082/api/books');
      setBooks(result.data);
    } catch (err) {
      setError(err.response?.data?.message || 'Error loading books');
    }
  };

  const deleteBook = async (id) => {
    try {
      await axios.delete(`http://localhost:8082/api/books/${id}`);
      loadBooks();
    } catch (err) {
      setError(err.response?.data?.message || 'Error deleting book');
    }
  };

  const assignBook = async (bookId, studentId) => {
    try {
      await axios.post(`http://localhost:8082/api/books/${bookId}/assign/${studentId}`);
      loadBooks();
    } catch (err) {
      setError(err.response?.data?.message || 'Error assigning book');
    }
  };

  const unassignBook = async (bookId) => {
    try {
      await axios.post(`http://localhost:8082/api/books/${bookId}/unassign`);
      loadBooks();
    } catch (err) {
      setError(err.response?.data?.message || 'Error unassigning book');
    }
  };

  return (
    <div className="container">
      <div className="py-4">
        <h2>Book List</h2>
        {error && <div className="alert alert-danger">{error}</div>}
        <Link to="/add-book" className="btn btn-primary mb-3">
          Add Book
        </Link>
        <table className="table border shadow">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">ISBN</th>
              <th scope="col">Assigned To</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            {books.map((book, index) => (
              <tr key={book.id}>
                <th scope="row">{index + 1}</th>
                <td>{book.title}</td>
                <td>{book.author}</td>
                <td>{book.isbn}</td>
                <td>
                  {book.studentId ? (
                    <>
                      Student #{book.studentId}
                      <button
                        className="btn btn-warning btn-sm ms-2"
                        onClick={() => unassignBook(book.id)}
                      >
                        Unassign
                      </button>
                    </>
                  ) : (
                    <input
                      type="number"
                      placeholder="Student ID"
                      className="form-control form-control-sm d-inline-block w-50"
                      onKeyPress={(e) => {
                        if (e.key === 'Enter') {
                          assignBook(book.id, e.target.value);
                        }
                      }}
                    />
                  )}
                </td>
                <td>
                  <Link
                    to={`/edit-book/${book.id}`}
                    className="btn btn-primary btn-sm me-2"
                  >
                    Edit
                  </Link>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => deleteBook(book.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default BookList;
