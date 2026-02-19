import json
import streamlit as st
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# Define scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]


# Load credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    creds_dict,
    scope
)


# Authorize client
client = gspread.authorize(creds)


# Spreadsheet name
SPREADSHEET_NAME = "DroneOps"


# Function to read sheet
def read_sheet(sheet_name):
    sheet = client.open(SPREADSHEET_NAME).worksheet(sheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)