# Expense-Tracker-API
A backend API for an Expense Tracker built using **Django** and **Django REST Framework**, with **JWT authentication**, expense CRUD, and analytics.

---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt
- SQLite 

---

## API Endpoints

### Authentication

| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| POST   | `/api/register/` | Register a user      |
| POST   | `/api/login/`    | Login & get JWT pair |

---

### Expenses

| Method | Endpoint                          | Description                              |
|--------|-----------------------------------|------------------------------------------|
| POST   | `/api/expenses/`                  | Create a new expense                     |
| GET    | `/api/expenses/?start=&end=`      | List user’s expenses (optional filters)  |

---

### Analytics

| Method | Endpoint                | Description                      |
|--------|-------------------------|----------------------------------|
| GET    | `/api/expenses/analytics/` | Total, category-wise, and trends |

---

## Getting Started (Run Locally)

```bash
git clone https://github.com/Sukhmanpreet16/Expense-Tracker-API.git
cd Expense-Tracker-API

# Create virtual env & activate
python -m venv venv
venv\Scripts\activate  # On Windows

# Install requirements
pip install -r requirements.txt

# Migrate DB
python manage.py makemigrations
python manage.py migrate


# Run the server
python manage.py runserver
