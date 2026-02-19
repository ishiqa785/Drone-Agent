from sheets import read_sheet

# Get available pilots
def get_available_pilots():
    pilots = read_sheet("Pilot_Roster")

    available = pilots[
        (pilots["current_assignment"] == "-") |
        (pilots["current_assignment"].isna())
    ]

    return available

# Get available drones
def get_available_drones():
    drones = read_sheet("Drone_Fleet")
    available = drones[drones["status"].str.lower() == "available"]
    return available


# Get missions
def get_all_missions():
    missions = read_sheet("Missions")
    return missions


# Detect pilot conflicts (double booking)
def detect_pilot_conflicts():
    missions = read_sheet("Missions")

    # Print columns to debug
    print("Mission columns:", missions.columns)

    conflicts = []

    # Use correct column name
    pilot_column = None

    # Detect correct pilot column automatically
    for col in missions.columns:
        if "pilot" in col.lower():
            pilot_column = col
            break

    if pilot_column is None:
        return ["No pilot column found in Missions sheet"]

    for i in range(len(missions)):
        for j in range(i + 1, len(missions)):

            pilot1 = missions.iloc[i][pilot_column]
            pilot2 = missions.iloc[j][pilot_column]

            start1 = missions.iloc[i]["start_date"]
            end1 = missions.iloc[i]["end_date"]

            start2 = missions.iloc[j]["start_date"]
            end2 = missions.iloc[j]["end_date"]

            if pilot1 == pilot2:
                if not (end1 < start2 or end2 < start1):
                    conflicts.append(
                        f"Conflict: Pilot {pilot1} between missions "
                        f"{missions.iloc[i]['mission_id']} and "
                        f"{missions.iloc[j]['mission_id']}"
                    )

    return conflicts


# Match pilots to mission based on skill
def find_matching_pilots(required_skill):
    pilots = read_sheet("Pilot_Roster")

    matching = pilots[
        pilots["skills"].str.contains(required_skill, case=False, na=False)
    ]

    return matching
