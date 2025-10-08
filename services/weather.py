# services/weather.py
# -----------------------------------------------
# Weather data service using OpenWeatherMap API.
# Returns temperature and conditions for a given city.
# -----------------------------------------------

import os, requests

OWM_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_summary(city: str = "Abu Dhabi", units: str = "metric"):
    """Return a small dict with weather summary (fallback if no key)."""
    if not OWM_KEY:
        # Fallback if API key not set
        return {
            "ok": False,
            "city": city,
            "summary": "Sunny and warm (simulated). Morning outdoor, afternoon indoor.",
            "temp": 32,
            "icon": "01d"
        }

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": OWM_KEY, "units": units}
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
        weather = data["weather"][0]
        main = data["main"]
        return {
            "ok": True,
            "city": city,
            "summary": weather["description"].title(),
            "temp": int(main["temp"]),
            "icon": weather.get("icon", "01d")
        }
    except Exception:
        return {
            "ok": False,
            "city": city,
            "summary": "Weather unavailable; assume warm daytime.",
            "temp": 30,
            "icon": "01d"
        }
