import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function AddBook() {
  const [book, setBook] = useState({
    title: '',
    author: '',
    isbn: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8082/api/books', book);
      navigate('/books');
    } catch (err) {
      setError(err.response?.data?.message || 'Error adding book');
    }
  };

  const handleChange = (e) => {
    setBook({ ...book, [e.target.name]: e.target.value });
  };

  return (
    <div className="container">
      <div className="row">
        <div className="col-md-6 offset-md-3 border rounded p-4 mt-2 shadow">
          <h2 className="text-center m-4">Add Book</h2>
          {error && <div className="alert alert-danger">{error}</div>}
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Title</label>
              <input
                type="text"
                className="form-control"
                name="title"
                value={book.title}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Author</label>
              <input
                type="text"
                className="form-control"
                name="author"
                value={book.author}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">ISBN</label>
              <input
                type="text"
                className="form-control"
                name="isbn"
                value={book.isbn}
                onChange={handleChange}
                required
              />
            </div>
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
            <button
              type="button"
              className="btn btn-danger mx-2"
              onClick={() => navigate('/books')}
            >
              Cancel
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default AddBook;
