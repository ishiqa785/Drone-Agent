# 🚁 Drone Operations Coordinator AI

An intelligent AI-powered coordination system built with **Streamlit** and **Google Sheets** to manage drone operations, pilot availability, and mission readiness.

This application allows users to query real-time drone and pilot data using natural language-like commands.

---

## 🌐 Live Demo

🔗 Streamlit App:  
https://drone-agent-zxzl3c6t7ykedhigjkmuxn.streamlit.app/

---

## 📂 GitHub Repository

🔗 Repository Link:  
https://github.com/ishiqa785/drone-agent

---

## 🎯 Features

- ✅ View available pilots
- ✅ View available drones
- ✅ Detect pilot availability
- ✅ Mission coordination support
- ✅ Real-time data from Google Sheets
- ✅ Professional Streamlit UI
- ✅ Secure credential handling via Streamlit Secrets
- ✅ Cloud deployed application

---

## 🧠 Example Queries

Users can enter queries such as:

show pilots
show available pilots
show drones
show available drones


---

## 🏗️ Architecture

User (Streamlit UI)
│
▼
app.py (Frontend UI)
│
▼
agent.py (Query Handler)
│
▼
logic.py (Business Logic)
│
▼
sheets.py (Google Sheets Integration)
│
▼
Google Sheets (Database)


---

## 📊 Data Source

Google Sheets acts as the backend database.

Spreadsheet contains:

**pilots sheet**

**drones sheet**

---

## 🔐 Security

Sensitive credentials are stored securely using:


Credentials file is NOT exposed in GitHub.

---

## ⚙️ Installation (Local Setup)

### Step 1: Clone repository

```bash
git clone https://github.com/ishiqa785/drone-agent.git
cd drone-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
.streamlit/secrets.toml
streamlit run app.py
drone-agent/
│
├── app.py
├── agent.py
├── logic.py
├── sheets.py
├── requirements.txt
├── decision_log.md
├── README.md
└── credentials.json (local only, not pushed)
drone-agent/
│
├── app.py
├── agent.py
├── logic.py
├── sheets.py
├── requirements.txt
├── decision_log.md
├── README.md
└── credentials.json (local only, not pushed)
🧩 Technologies Used
Python 3.13
Streamlit
Google Sheets API
gspread
Pandas
OAuth2 Service Account
GitHub
Streamlit Cloud🧠 AI Logic
Query → Agent → Logic → Sheets → Response
Handles:
pilot availability
drone availability
mission readiness queries
