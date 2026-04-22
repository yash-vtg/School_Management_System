# 🏫 School Management System

A comprehensive **School Management System** built with **Python, Django, HTML, CSS, Bootstrap, and JavaScript**.  
This project provides three distinct login portals for **Admin, Teacher, and Student**, each with tailored features to streamline school operations.

---

## 🚀 Features

### 👨‍💼 Admin Portal
- Full control over the system
- Add/manage teachers and students
- Post notifications on the homepage
- Manage attendance records
- Edit and update user profiles

### 👩‍🏫 Teacher Portal
- Add and manage students
- Mark student attendance
- Upload and share learning materials by class
- Edit and update their own profile

### 👨‍🎓 Student Portal
- View attendance records marked by teachers
- Access learning materials provided by teachers
- View personal profile (limited editing rights)

---

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** (Add your database here, e.g., SQLite, PostgreSQL, MySQL)

---

## 📂 Project Structure
```
school-management-system/
│
├── manage.py
├── requirements.txt
├── templates/        # HTML templates
├── static/           # CSS, JS, Bootstrap files
├── apps/             # Django apps (admin, teacher, student)
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone (https://github.com/yash-vtg/School_Management_System.git)
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the system**
   - Admin: `http://127.0.0.1:8000/admin`
   - Teacher/Student: `http://127.0.0.1:8000/`

---

## 🔑 Login Portals
- **Admin:** Full system management
- **Teacher:** Manage students, attendance, and materials
- **Student:** View attendance and learning resources

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to fork this repo, create a branch, and submit a pull request.

---
