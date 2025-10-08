# services/places.py
# -----------------------------------------------
# Google Places API integration (text search).
# Returns list of place cards with rating, image, and map links.
# -----------------------------------------------

import os, requests
from .utils import google_maps_link

PLACES_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

def text_search(query: str, region: str = "AE"):
    """Return a list of places with name, rating, photo, and map URL."""
    if not PLACES_KEY:
        # Fallback data if key not set
        samples = [
            {"name": "Louvre Abu Dhabi", "rating": 4.7, "photo_url": None, "map_url": "https://goo.gl/maps/...", "price_level": 2},
            {"name": "Corniche Beach", "rating": 4.6, "photo_url": None, "map_url": "https://goo.gl/maps/...", "price_level": 0},
            {"name": "Qasr Al Watan", "rating": 4.8, "photo_url": None, "map_url": "https://goo.gl/maps/...", "price_level": 2},
        ]
        return {"ok": False, "items": samples}

    try:
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {"query": query, "key": PLACES_KEY, "region": region}
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()

        items = []
        for it in data.get("results", [])[:8]:
            name = it.get("name")
            rating = it.get("rating")
            price = it.get("price_level")
            lat = it["geometry"]["location"]["lat"]
            lng = it["geometry"]["location"]["lng"]

            # Optional photo
            photo_url = None
            if it.get("photos"):
                ref = it["photos"][0]["photo_reference"]
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={ref}&key={PLACES_KEY}"

            items.append({
                "name": name,
                "rating": rating,
                "photo_url": photo_url,
                "map_url": google_maps_link(name, lat, lng),
                "price_level": price
            })
        return {"ok": True, "items": items}
    except Exception:
        return {"ok": False, "items": []}
