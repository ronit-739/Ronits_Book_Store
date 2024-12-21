# Django Bookstore Backend

A backend for a Bookstore application built with Django and Django REST Framework (DRF). It includes user authentication via JWT and book management APIs.

## Features
- User authentication with JWT
- CRUD operations for books
- Django Admin panel for managing users and books

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bookstore-app.git
   cd bookstore-app
   
2. Set up a virtual environment:
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

4.  Install dependencies:
pip install -r requirements.txt

5.  Apply migrations:
python manage.py migrate
6.  Create a superuser:
python manage.py createsuperuser

8.  Run the development server:
python manage.py runserver

API Endpoints
Login (POST /api/token/) - Authenticate and get JWT tokens.
Refresh Token (POST /api/token/refresh/) - Refresh access token.
Get All Books (GET /api/books/) - List all books.
Create Book (POST /api/books/) - Add a new book.
Update Book (PUT /api/books/{id}/) - Update a book by ID.
Delete Book (DELETE /api/books/{id}/) - Delete a book by ID.
Dependencies
Django
djangorestframework
djangorestframework-simplejwt
