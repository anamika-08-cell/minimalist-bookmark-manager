#  Minimal Bookmark Manager

A simple, lightweight bookmark management application built with **FastAPI and SQLite** to help users save interesting links and keep useful online resources organized in one place.

##  About the Project

Have you ever found an interesting study resource, tutorial, or website and later struggled to find it again?

The Minimal Bookmark Manager is designed to solve this everyday problem. It provides a simple way to keep useful links together so they can be revisited whenever needed.

This project is also part of my journey toward learning backend development with Python and building practical software solutions.

## Key Features

- **Bookmark Management:** A project focused on saving and organizing useful links.annotated.
- **FastAPI Backend:** Uses FastAPI to build the application's backend.
- **SQLite Database:** Stores bookmark data in a local database.
- **SQLAlchemy ORM:** Uses SQLAlchemy to interact with the database.
- **Simple Web Interface:** Includes an HTML template for the user interface.
- **Lightweight Setup:** Uses a local database instead of requiring a separate database server.

##  Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Core programming language   |
| FastAPI    | Backend framework           |
| SQLite     | Database                    |
| SQLAlchemy | Database operations and ORM |
| HTML       | Web interface               |
| Jinja2     | HTML templating             |
| Uvicorn    | ASGI server                 |

##  Installation and Setup

### 1. Clone the repository

````bash
```bash
git clone https://github.com/anamika-08-cell/minimalist-bookmark-manager.git
cd minimalist-bookmark-manager
``` 
cd minimal bookmark
````

Replace the placeholders with your actual GitHub repository URL and project folder name.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

If your FastAPI application instance is named `app` inside `main.py`, run:

```bash
uvicorn main:app --reload
```

If your Python file has a different name, replace `main` with that filename, without the `.py` extension.

### 6. Open the application

Visit the local address:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

FastAPI's interactive API documentation is generally available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

##  Database

The application uses SQLite with the following database URL:

```python
DATABASE_URL = "sqlite:///./bookmarks.db"
```

The database file is stored locally in the working directory. SQLAlchemy is used to connect to the database and perform database operations.

##  Project Goals

- Solve a common problem through a practical application.
- Strengthen my understanding of Python backend development.
- Learn database integration using SQLAlchemy and SQLite.
- Build a foundation for future improvements and features.

##  Future Improvements

The following features are planned for future development:

- User registration and login.
- Personal bookmarks for individual users.
- Bookmark search and filtering.
- Bookmark categories and tags.
- Improved user interface and user experience.

These are planned improvements, not claims about features already implemented.

## Author

**Anamika Pal**

Aspiring Python Backend Developer, learning by building practical projects.

