#  Fitness Studio Booking API

This project is a simple Booking API for a fictional fitness studio that offers classes like **Yoga**, **Zumba**, and **HIIT**. It allows users to view classes, book them, and check their booking history.

## Project Features

- View available fitness classes with date, time, instructor, and available slots.
- Book a class by providing your name, email, and class ID.
- Retrieve your booking history using your email.
- Handles booking validation, available slot management, and basic error handling.
- Includes an engaging home page with motivational messages for users.
---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite (In-Memory/Default)
- **Frontend:** Basic HTML (Template-based rendering)

---

## API Endpoints

### 1. View All Classes

- **GET** `/classes/`
- Returns: List of upcoming fitness classes

### 2. Book a Class

- **POST** `/book/`
- Body (JSON):
```json
{ "class_id": 1, "client_name": "Rakshitha","client_email": "testing@gmail.com"}

### 3. View Bookings by Email
- GET /bookings/?email=you@example.com

Sample JSON for a class:

```json
{"name": "Yoga","instructor": "Anjali", "date": "2025-06-08","time_slots":3,"available_slots": 10}


** 1.Create a virtual environment:**

python -m venv env

source env/bin/activate  # For Windows: env\Scripts\activate

** 2. Install requirements: **

pip install -r requirements.txt

## 3. Apply migrations:

python manage.py makemigrations

python manage.py migrate

## 4. Run the server:

python manage.py runserver


Home Page: http://127.0.0.1:8000/

Classes List: http://127.0.0.1:8000/classes/

Admin Panel: http://127.0.0.1:8000/admin/
