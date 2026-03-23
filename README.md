# Django Library Management System (LMS)

A premium, fast, and fully-featured web-based Library Management System built with Django, Tailwind CSS, Flowbite, and HTMX. 

## ✨ Key Features

- **Modern UI & UX:** Beautifully crafted with Tailwind CSS and Flowbite components, featuring smooth transitions, glassmorphism, and gradient accents.
- **Single Page Application (SPA) Feel:** Powered by HTMX for lightning-fast, seamless navigation without full page reloads.
- **Dark & Light Mode:** Fully cohesive and polished themes for both dark and light modes, saving user preferences seamlessly.
- **Authentication & Security:** Premium split-screen Login and Signup pages. All routes are protected. Safe logout using Django 5.0+ POST requirements.
- **User Settings:** Tabbed interface for users to update their profile and securely change passwords.
- **Advanced Book Management:** Includes a book cover image system (URL-based) with an instant Grid/List view toggle.
- **Dashboard Analytics:** Visual stat cards and an active borrows table with automatically generated avatar initials.
- **Backend Optimization:** Engineered with `select_related` and `db_index` implementations to resolve N+1 queries and guarantee scalable performance.
- **Branded Admin Panel:** Custom Django admin interface securely mapped to a unique URL endpoint.

## 🛠️ Technologies Used

- **Backend:** Python 3.10+, Django 5.x, SQLite3
- **Frontend Core:** HTML5, HTMX
- **Styling:** Tailwind CSS (via CDN), Flowbite v4

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ installed
- `pip` installed

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/pranishs999/Library_Management_system-LMS.git
cd Library_Management_system-LMS
```

2. **Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply database migrations**
```bash
python manage.py migrate
```

5. **Create a Superuser (Admin)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

### Accessing the Application
- **Main App:** `http://127.0.0.1:8000/`
- **Admin Panel:** `http://127.0.0.1:8000/lib-control-panel/`

## ✍️ Author
Designed and developed by **Pranish Shrestha**.

## 📄 License
This project is licensed under the MIT License.
