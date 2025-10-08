# services/events.py
# -----------------------------------------------
# Eventbrite API integration to fetch upcoming events.
# Falls back to local sample events if token missing.
# -----------------------------------------------

import os, requests

EB_TOKEN = os.getenv("EVENTBRITE_TOKEN")

def get_events(city: str = "Abu Dhabi"):
    """Return a list of event dictionaries."""
    if not EB_TOKEN:
        # Fallback sample events
        return {
            "ok": False,
            "items": [
                {"title": "Abu Dhabi Sunset Kayak", "date": "Today 18:00", "url": "#"},
                {"title": "Corniche Night Run 5K", "date": "Fri 19:30", "url": "#"},
                {"title": "Cultural Tour at Qasr Al Hosn", "date": "Sat 10:00", "url": "#"},
            ]
        }

    try:
        url = "https://www.eventbriteapi.com/v3/events/search/"
        params = {"location.address": city, "sort_by": "date"}
        headers = {"Authorization": f"Bearer {EB_TOKEN}"}
        r = requests.get(url, params=params, headers=headers, timeout=8)
        r.raise_for_status()
        data = r.json()
        items = []
        for e in data.get("events", [])[:8]:
            items.append({
                "title": e.get("name", {}).get("text"),
                "date": e.get("start", {}).get("local", "")[:16].replace("T", " "),
                "url": e.get("url")
            })
        return {"ok": True, "items": items}
    except Exception:
        return {"ok": False, "items": []}
