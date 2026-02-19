import streamlit as st
import json
import gspread
from google.oauth2.service_account import Credentials

# Define scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=scope
)

client = gspread.authorize(creds)

# Spreadsheet name
SPREADSHEET_NAME = "DroneOps"

# Function to read sheet
def read_sheet(sheet_name):
    sheet = client.open(SPREADSHEET_NAME).worksheet(sheet_name)
    data = sheet.get_all_records()
    return data
