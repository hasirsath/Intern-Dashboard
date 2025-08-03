# 🧑‍💼 Intern Dashboard – Flask + JSON (Dummy Login & Leaderboard)

A simple, full-stack intern dashboard built using **Flask** and **HTML/CSS/JS**, designed as part of an internship submission task. This project demonstrates front-end design, back-end integration with dummy data, and API endpoints — all without real authentication.

---

## 🌟 Features

### ✅ Frontend
- Dummy **Login/Signup page** (no auth)
- **Intern Dashboard** with:
  - Name (dynamic)
  - Referral code (dynamic)
  - Total donations raised
  - Rewards/unlockables list (bullet-aligned & centered)
- **Leaderboard** page sorted by donations
- **Logout** flow with a Thank You page
- Clean, responsive UI using Google Fonts and Flexbox

### ✅ Backend (Flask)
- RESTful APIs serving dummy intern data from JSON
  - `GET /api/user` – single user
  - `GET /api/users` – all interns
- User selected by name/referral query on dashboard route
- Data stored in static `dummy_data.json`

---

## 📁 Project Structure

intern_dashboard/
│
├── app.py 
|
├── data/
│ └── dummy_data.json
|
├── static/
│ └── style.css
|
├── templates/
│ ├── index.html 
│ ├── dashboard.html 
│ ├── leaderboard.html 
│ └── logout.html 
|
└── README.md 

---

**Setup Instructions**

1. 📦 Clone the Repository
git clone https://github.com/hasirsath/intern-dashboard.git
cd intern-dashboard

2. 🐍 Create a Virtual Environment (Recommended)  
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Mac/Linux

3. 📥 Install Dependencies
pip install -r requirements.txt

4. 🚀 Run the Flask App
python app.py

The app will start running at:
👉 http://127.0.0.1:5000
