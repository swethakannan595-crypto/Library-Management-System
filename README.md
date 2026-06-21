<div align="center">

# 📖 Library Management System

**A web-based library management solution built with Django — manage books, members, and issue/return tracking from one clean dashboard.**

<img width="951" height="476" alt="image" src="https://github.com/user-attachments/assets/075bc035-3c32-441c-881a-bfcc65f0f1f1" />


<img width="950" height="467" alt="image" src="https://github.com/user-attachments/assets/4f090d1c-81d2-4a1a-8e69-87d1d3f79d5b" />


<img width="932" height="470" alt="image" src="https://github.com/user-attachments/assets/696bfa1a-3b57-486b-bfb1-1c8df5e7d24e" />


<img width="957" height="336" alt="image" src="https://github.com/user-attachments/assets/c3810a14-1616-4fbd-a8ab-ed8e8f92be34" />


<img width="938" height="463" alt="image" src="https://github.com/user-attachments/assets/f6750d43-0503-499b-9b64-e2545efbf10a" />

</div>

---

## 📖 Overview

**Library Management System** is a full-stack web application built with **Django** that digitizes the day-to-day operations of a library — cataloging books, registering members, and tracking which book is issued to whom and when it's due back. Built as a solo project, it follows Django's MVT (Model-View-Template) architecture with a clean, custom HTML/CSS interface on top.

This project demonstrates core full-stack web development fundamentals: relational data modeling, server-side rendering, CRUD operations, and form handling — the foundation of any real-world admin/management system.

---

## ✨ Features

### 📚 Book Record Management
- Add, edit, and delete book records
- Track title, author, genre, ISBN, and available copies
- Searchable and organized book catalog view

### 🧑‍🤝‍🧑 Member Registration
- Register new library members with contact details
- View and manage the full member directory
- Edit or remove member records

### 🔄 Issue / Return Tracking
- Issue a book to a registered member
- Track issue date and due date
- Mark books as returned and update availability automatically
- View currently issued and overdue books at a glance

### 🎨 Clean Interface
- Custom-built HTML/CSS templates (no heavy frontend framework)
- Simple, readable layout focused on usability
- Django template inheritance for consistent page structure

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Django (Python) |
| **Database** | SQLite (default Django ORM) |
| **Frontend** | HTML5, CSS3 |
| **Architecture** | MVT (Model-View-Template) |
| **Admin Interface** | Django Admin |

---

## 🏗️ Architecture


<img width="314" height="93" alt="image" src="https://github.com/user-attachments/assets/f587c67b-2af0-4508-a960-63973f9eb6b8" />


**Core flow:** Librarian/Admin logs in → manages book catalog → registers members → issues a book (creates an Issue record linking Book + Member + dates) → marks return (updates Issue record + restores book availability).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Database Setup

```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create an admin/superuser account
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Visit **`http://127.0.0.1:8000`** to access the app, or **`http://127.0.0.1:8000/admin`** for the Django admin panel.

---

## 📁 Project Structure

<img width="323" height="254" alt="image" src="https://github.com/user-attachments/assets/5bdd960e-e9ad-4128-b6d0-11b8a501ebad" />


---

## 🗺️ Roadmap

- [ ] User authentication for members (self-service portal)
- [ ] Fine calculation for overdue books
- [ ] Email/SMS due-date reminders
- [ ] Book cover image uploads
- [ ] Search and filter by genre/author/availability
- [ ] Export reports (issued books, overdue list) as PDF/CSV
- [ ] REST API layer (Django REST Framework)
- [ ] Deployment (Render / Railway / PythonAnywhere)

---

## 🎯 Skills Demonstrated

`Django` · `Python` · `MVT Architecture` · `Relational Database Design` · `CRUD Operations` · `Form Handling` · `Django Admin` · `HTML/CSS` · `Full-Stack Development`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

**A solo full-stack project built to practice real-world Django fundamentals — from data modeling to a working library workflow.**

`#Django` `#Python` `#LibraryManagement` `#WebApp` `#FullStackDevelopment` `#GitHubProject`

</div>

