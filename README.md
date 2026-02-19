# Drone Operations Coordinator AI

This project is a Streamlit-based AI assistant that helps coordinate drone operations using Google Sheets.

## Features

- Show available pilots
- Show available drones
- Detect scheduling conflicts
- Skill-based pilot assignment

## Live Demo

https://drone-agent-zxzl3c67ykedhigjkmuxn.streamlit.app

## GitHub Repository

https://github.com/ishiq785/drone-agent

## Tech Stack

- Python
- Streamlit
- Google Sheets API
- gspread

## How it works

The app connects to Google Sheets using a service account and retrieves operational data. The AI agent processes queries and returns structured results.

## Run locally

pip install -r requirements.txt

streamlit run app.py
