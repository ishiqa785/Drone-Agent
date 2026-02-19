from logic import get_available_pilots, get_available_drones


def handle_query(query):
    query = query.lower()

    try:

        if "pilot" in query:
            return get_available_pilots()

        elif "drone" in query:
            return get_available_drones()

        elif "conflict" in query:
            return "Conflict detection not implemented yet."

        else:
            return """
Supported queries:
• show available pilots
• show available drones
• show pilots
• show drones
"""

    except Exception as e:
        return f"System error: {str(e)}"
