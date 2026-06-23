# 🚔 Smart Traffic Surveillance System (STSS)

## 📌 Overview

Smart Traffic Surveillance System (STSS) is an AI-powered Automatic Number Plate Recognition (ANPR) platform that automates vehicle identification, verification, and traffic law enforcement.

The system uses **YOLOv8** for number plate detection, **EasyOCR** for character recognition, and **Supabase PostgreSQL** for vehicle record management. It can identify vehicles, verify ownership details, detect stolen or suspicious vehicles, and automatically generate traffic challans in PDF format.

This project demonstrates the integration of **Computer Vision**, **Artificial Intelligence**, **Optical Character Recognition (OCR)**, **Database Management**, and **Web Technologies** to build a smart traffic monitoring solution.

---

# 🎯 Features

### ✅ Automatic Number Plate Recognition (ANPR)

* Detects vehicle number plates from uploaded images.
* Extracts license plate text using OCR.
* Supports Indian vehicle registration plates.

### ✅ Vehicle Detection & Verification

* Retrieves vehicle information from the database.
* Displays owner details and vehicle status.
* Performs real-time record verification.

### ✅ Stolen Vehicle Alert System

* Identifies vehicles marked as stolen.
* Generates alert notifications instantly.
* Assists law enforcement agencies.

### ✅ Suspicious/Fake Number Plate Detection

* Flags suspicious vehicle records.
* Helps identify potentially fraudulent registrations.
* Supports investigation workflows.

### ✅ Automatic Challan Generation

* Generates PDF traffic challans automatically.
* Includes violation details and fine amount.
* Maintains digital enforcement records.

### ✅ Modern Dashboard Interface

* User-friendly web interface.
* Image preview before detection.
* Real-time result display.

---

# 🏗️ System Architecture

```text
Vehicle Image Upload
        │
        ▼
Flask Backend
        │
        ▼
YOLOv8 Number Plate Detection
        │
        ▼
Plate Cropping
        │
        ▼
EasyOCR Text Recognition
        │
        ▼
Extracted Plate Number
        │
        ▼
Supabase PostgreSQL Database
        │
        ▼
Vehicle Verification
        │
 ┌──────┼───────────┐
 ▼      ▼           ▼
Stolen  Suspicious  Violation
Check   Check       Check
 │       │           │
 └───────┴───────────┘
         │
         ▼
Automatic PDF Challan
         │
         ▼
Results Dashboard
```

---

# 🧠 Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask
* Flask-CORS

## AI & Machine Learning

* YOLOv8
* EasyOCR
* OpenCV

## Database

* Supabase
* PostgreSQL

## PDF Generation

* ReportLab

---

# 📂 Project Structure

```text
Smart-Traffic-Surveillance-System
│
├── backend
│   ├── app.py
│   ├── detection.py
│   ├── database.py
│   ├── challan_generator.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── models
│   └── best.pt
│
├── uploads
├── challans
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YaminiShankari/Smart-Traffic-Surveillance-System.git
cd Smart-Traffic-Surveillance-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Start Backend

```bash
cd backend
python app.py
```

Expected Output:

```text
Running on http://127.0.0.1:5000
```

## Launch Frontend

Open:

```text
frontend/index.html
```

or use VS Code Live Server.

---

# 📊 Database Schema

## Vehicles Table

| Column           | Description                 |
| ---------------- | --------------------------- |
| plate_number     | Vehicle Registration Number |
| owner_name       | Owner Name                  |
| vehicle_type     | Car/Bike/etc.               |
| status           | Normal / Stolen             |
| violation        | Traffic Violation           |
| fine_amount      | Fine Amount                 |
| violation_date   | Date of Violation           |
| challan_status   | Paid / Unpaid               |
| suspicious_plate | True / False                |

---

# 📄 Sample Output

### Vehicle Detected

```text
Vehicle Number : MH20EE7602

Owner : Arjun Kumar

Status : Normal

Violation : Overspeeding

Fine Amount : ₹2500

Challan Generated Successfully
```

### Stolen Vehicle Alert

```text
Vehicle Number : MH20EJ0364

Owner : Nikhil Patil

Status : Stolen

🚨 STOLEN VEHICLE DETECTED 🚨

Violation : Vehicle Theft

Fine Amount : ₹5000
```

---

# 🔒 Security Considerations

* Database credentials stored securely.
* Input validation for uploaded files.
* CORS-enabled backend communication.
* Database access restricted through Supabase.

---

# 🔮 Future Enhancements

* Live CCTV Camera Integration
* Real-Time Vehicle Tracking
* Speed Violation Detection
* Traffic Analytics Dashboard
* Government Vehicle Registry Integration
* Mobile Application Support
* Multi-Camera Monitoring System

---

# 🎓 Academic Relevance

This project demonstrates practical applications of:

* Computer Vision
* Artificial Intelligence
* Deep Learning
* Optical Character Recognition
* Database Systems
* Web Development
* Intelligent Transportation Systems

---

# 👩‍💻 Author

**Yamini**

B.Tech Computer Science Engineering

AI-Powered Smart Traffic Surveillance System using ANPR
