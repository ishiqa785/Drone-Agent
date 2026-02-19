from logic import (
    get_available_pilots,
    get_available_drones,
    detect_pilot_conflicts,
    find_matching_pilots,
)


def handle_query(user_input):

    user_input = user_input.lower()

    # Available pilots
    if "available pilots" in user_input:
        pilots = get_available_pilots()

        if pilots.empty:
            return "No pilots available."

        return pilots.to_string(index=False)

    # Available drones
    elif "available drones" in user_input:
        drones = get_available_drones()

        if drones.empty:
            return "No drones available."

        return drones.to_string(index=False)

    # Conflicts
    elif "conflict" in user_input:
        conflicts = detect_pilot_conflicts()

        if not conflicts:
            return "No conflicts detected."

        return str(conflicts)

    # Skill matching
    elif "find pilot with skill" in user_input:

        words = user_input.split()
        skill = words[-1]

        pilots = find_matching_pilots(skill)

        if pilots.empty:
            return f"No pilots found with skill {skill}"

        return pilots.to_string(index=False)

    else:
        return """I can help with:
        
• Show available pilots
• Show available drones
• Detect conflicts
• Find pilot with skill mapping

Example:
'show available pilots'
"""
