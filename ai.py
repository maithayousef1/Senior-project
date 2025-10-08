# ai.py
# Simple, local "AI" placeholder you can replace with real GPT later.

def chat_response(message, city="Abu Dhabi", tone="Casual"):
    text = (message or "").lower()

    # Tiny rule-based ideas to simulate helpfulness
    if "event" in text or "do" in text or "plan" in text:
        base = f"Here are a few ideas around {city}: Sheikh Zayed Grand Mosque, Louvre Abu Dhabi, Corniche walk, and a sunset dhow cruise."
    elif "weather" in text:
        base = f"The weather in {city} is usually sunny; try morning outdoor plans and indoor activities after noon."
    else:
        base = f"I can plan your day in {city}, suggest routes, and book-friendly activities."

    # Adjust tone
    if tone.lower().startswith("cas"):
        return "Sure thing! " + base
    if tone.lower().startswith("pro"):
        return "Recommendation: " + base
    return "Here’s a thought: " + base
