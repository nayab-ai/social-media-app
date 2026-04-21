
# 🚀 Social Media App (Django Project)

This is a simple **Social Media Web Application** built using **Django (Python)** as part of my internship Task 2 at **CodeAlpha**.

The project demonstrates basic social media functionality with user authentication and profile management.

---

## 📌 Project Overview

This application allows users to:
- Create an account (Signup)
- Login to their account
- View user profile
- Access a simple home page

It uses Django’s built-in authentication system and follows the MVT (Model-View-Template) architecture.

---

## ✨ Features

- 🔐 User Signup System  
- 🔑 User Login System  
- 👤 User Profile Page  
- 🏠 Home Page  
- 🚪 Logout Functionality  
- 🗄️ SQLite Database Integration  
- ⚙️ Django Backend System  

---

## ⚙️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS (Django Templates)
- Database: SQLite
- Server: Django Development Server

---

## 📁 Project Structure

```

config/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── profile.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
manage.py
db.sqlite3

## 🚀 How to Run This Project

1. Clone the repository:
```bash
git clone https://github.com/nayab-ai/social-media-app.git
````

2. Go to project folder:

```bash
cd social-media-app
```

3. Install Django:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start server:

```bash
python manage.py runserver
```

6. Open in browser:

```
http://127.0.0.1:8000/
```
## 🎯 What I Learned

* Django project setup and structure
* User authentication system (Signup/Login)
* Views, URLs, and Templates concept
* Database integration using SQLite
* Backend development workflow

---





