# services/utils.py
# -----------------------------------------------
# Helper utilities: language detection, tone, sentiment, and map link builder.
# Used by Yalla AI to understand user mood, budget, and preferences.
# -----------------------------------------------

import re
from urllib.parse import urlencode

# Basic Arabic Unicode range (for detecting Arabic text)
ARABIC_RANGE = re.compile(r'[\u0600-\u06FF]')

def is_arabic(text: str) -> bool:
    """Detect if the user message is in Arabic."""
    return bool(ARABIC_RANGE.search(text or ""))

def detect_tone(tone: str) -> str:
    """Normalize tone input for consistency."""
    t = (tone or "").lower()
    if t.startswith("pro"): return "Professional"
    if t.startswith("neu"): return "Neutral"
    return "Casual"

def quick_sentiment(text: str) -> str:
    """Simple sentiment guess based on keywords (no external AI)."""
    t = (text or "").lower()
    neg = any(w in t for w in ["tired", "sad", "busy", "overwhelmed", "stress"])
    pos = any(w in t for w in ["happy", "excited", "great", "amazing"])
    if neg and not pos: return "negative"
    if pos and not neg: return "positive"
    return "neutral"

def parse_budget(text: str) -> str:
    """Estimate if user prefers low, medium, or high budget."""
    t = (text or "").lower()
    if any(w in t for w in ["budget", "cheap", "low", "free", "student"]): return "low"
    if any(w in t for w in ["luxury", "expensive", "premium", "fine dining"]): return "high"
    return "medium"

def google_maps_link(place_name: str, lat=None, lng=None, query: str = None) -> str:
    """Build a Google Maps link based on coordinates or query."""
    if lat and lng:
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
    q = query or place_name
    return "https://www.google.com/maps/search/?" + urlencode({"api": 1, "query": q})
