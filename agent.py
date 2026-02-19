from logic import get_available_pilots, get_available_drones


def handle_query(query):

    query = query.lower()

    try:

        if "pilot" in query:
            return get_available_pilots()

        elif "drone" in query:
            return get_available_drones()

        else:
            return """
Supported queries:
• show pilots
• show drones
• show available pilots
• show available drones
"""

    except Exception as e:
        return f"System error: {str(e)}"
