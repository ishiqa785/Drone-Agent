from sheets import read_sheet
import pandas as pd


# Normalize column names
def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


# Safe column getter
def get_column(df, possible_names):
    for name in possible_names:
        if name in df.columns:
            return name
    return None


# Get available pilots safely
def get_available_pilots():
    try:
        pilots = read_sheet("pilots")

        if pilots is None or len(pilots) == 0:
            return "No pilots data found."

        pilots = normalize_columns(pilots)

        status_col = get_column(pilots, ["status", "availability"])
        assignment_col = get_column(pilots, ["current_assignment", "assignment", "assigned"])

        if status_col:
            available = pilots[pilots[status_col].astype(str).str.lower() == "available"]

        elif assignment_col:
            available = pilots[pilots[assignment_col].astype(str).isin(["", "-", "none", "null"])]

        else:
            return f"No availability column found. Columns: {list(pilots.columns)}"

        if len(available) == 0:
            return "No available pilots."

        return available.to_string(index=False)

    except Exception as e:
        return f"Error reading pilots data: {str(e)}"


# Get available drones safely
def get_available_drones():
    try:
        drones = read_sheet("drones")

        if drones is None or len(drones) == 0:
            return "No drones data found."

        drones = normalize_columns(drones)

        status_col = get_column(drones, ["status", "availability"])

        if status_col is None:
            return f"No status column found. Columns: {list(drones.columns)}"

        available = drones[drones[status_col].astype(str).str.lower() == "available"]

        if len(available) == 0:
            return "No available drones."

        return available.to_string(index=False)

    except Exception as e:
        return f"Error rea
