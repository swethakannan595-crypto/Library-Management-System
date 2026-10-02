# Library Management System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Backend-Django-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/Frontend-HTML5%20%2B%20CSS3-E34F26?logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

A web-based library management application built with Django. It lets a librarian manage books, register members and track issues and returns from one clean interface.

<img width="951" height="476" alt="Library Management System dashboard" src="https://github.com/user-attachments/assets/075bc035-3c32-441c-881a-bfcc65f0f1f1" />

---

## Overview

Library Management System is a full-stack Django application that digitizes day-to-day library operations: cataloguing books, registering members, and tracking which book is issued to whom and when it is due back.

It was built as a solo project and follows Django's Model-View-Template (MVT) architecture, with custom HTML and CSS templates. The project covers core full-stack fundamentals: relational data modelling, server-side rendering, CRUD operations and form handling.

## Key Features

### Book management

- Add, edit and delete book records
- Track title, author, genre, ISBN and available copies
- Organized, searchable catalog view

<img width="938" height="463" alt="Book catalog" src="https://github.com/user-attachments/assets/4f090d1c-81d2-4a1a-8e69-87d1d3f79d5b" />

### Member management

- Register new members with contact details
- View and manage the full member directory
- Edit or remove member records

<img width="938" height="463" alt="Member directory" src="https://github.com/user-attachments/assets/696bfa1a-3b57-486b-bfb1-1c8df5e7d24e" />

### Issue and return tracking

- Issue a book to a registered member
- Record the issue date and due date
- Mark a book as returned, which updates availability automatically
- See currently issued and overdue books at a glance

<img width="938" height="463" alt="Issue and return tracking" src="https://github.com/user-attachments/assets/c3810a14-1616-4fbd-a8ab-ed8e8f92be34" />

### Interface

- Custom HTML and CSS templates, with no heavy frontend framework
- Simple, readable layout focused on usability
- Django template inheritance for consistent page structure
- Django Admin panel for administrative access

<img width="938" height="463" alt="Application interface" src="https://github.com/user-attachments/assets/f6750d43-0503-499b-9b64-e2545efbf10a" />

## How It Works

```mermaid
flowchart LR
    A[Librarian logs in] --> B[Manage book catalog]
    A --> C[Register members]
    B --> D[Issue a book<br/>creates an Issue record:<br/>book + member + dates]
    C --> D
    D --> E[Mark as returned<br/>updates the Issue record<br/>and restores availability]
```

## Architecture

```mermaid
flowchart LR
    U[Browser] --> URL[URL routing]
    URL --> V[Views]
    V --> M[Models and Django ORM]
    M --> DB[(SQLite)]
    V --> T[Templates<br/>HTML + CSS]
    T --> U
```

<img width="314" height="93" alt="Architecture diagram" src="https://github.com/user-attachments/assets/f587c67b-2af0-4508-a960-63973f9eb6b8" />

## Tech Stack

| Layer | Technology |
|---|---|
| Backend framework | Django (Python) |
| Database | SQLite through the Django ORM |
| Frontend | HTML5, CSS3 |
| Architecture | MVT (Model-View-Template) |
| Admin interface | Django Admin |

## Project Structure

<img width="323" height="254" alt="Project structure" src="https://github.com/user-attachments/assets/5bdd960e-e9ad-4128-b6d0-11b8a501ebad" />

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### Installation

```bash
git clone https://github.com/swethakannan595-crypto/library-management-system.git
cd library-management-system
```

Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Database setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Run the server

```bash
python manage.py runserver
```

| Page | URL |
|---|---|
| Application | http://127.0.0.1:8000 |
| Django Admin | http://127.0.0.1:8000/admin |

## Roadmap

- [ ] Member login and self-service portal
- [ ] Fine calculation for overdue books
- [ ] Email and SMS due-date reminders
- [ ] Book cover image uploads
- [ ] Advanced filters by genre, author and availability
- [ ] Export reports (issued and overdue books) as PDF or CSV
- [ ] REST API layer with Django REST Framework
- [ ] Deployment (Render, Railway or PythonAnywhere)

## Concepts Demonstrated

Django, Python, MVT architecture, relational database design, CRUD operations, form handling, Django Admin, HTML and CSS, full-stack development.

## Author

**Swetha Kannan**
B.Sc. Information Technology
[GitHub](https://github.com/swethakannan595-crypto)

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.
