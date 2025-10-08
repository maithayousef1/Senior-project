# --------------------------------------------
# 🌴 Yalla Planner | Flask App
# - Serves pages: Home, Explore, Planner, AI, Preferences, Profile
# - Handles DB + simple AI /chat endpoint + Preferences API
# --------------------------------------------

from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Local modules (your models + simple AI reply)
from models import db, User, ItineraryItem, Preference
from ai import chat_response

# Load .env (for DATABASE_URL etc.)
load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')

# --- Database config ---
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///planner.db")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS for frontend calls (e.g., fetch('/chat'))
CORS(app)
db.init_app(app)

# --- Create tables & seed a default user once ---
with app.app_context():
    db.create_all()
    if not User.query.first():
        db.session.add(User(name="Maitha", country="UAE"))
        db.session.add(Preference(interests="Cafes,Beaches", tone="Friendly", remember=True))
        db.session.commit()

# ---------- PAGE ROUTES ----------

@app.route('/')
def home_redirect():
    """Default route → send to the new landing page."""
    return redirect(url_for('home'))

@app.route('/home')
def home():
    """Landing page with greeting + big actions."""
    return render_template('home.html')

@app.route('/explore')
def explore():
    """City discovery (carousel + filters later)."""
    return render_template('explore.html')

@app.route('/planner')
def planner():
    """Daily planner view (Morning/Afternoon/Evening)."""
    return render_template('planner.html')

@app.route('/ai')
def ai_page():
    """Conversational AI UI."""
    return render_template('ai.html')

@app.route('/profile')
def profile_page():
    """Simple profile placeholder (you can keep or merge with Preferences)."""
    return render_template('profile.html')

@app.route('/preferences')
def preferences_page():
    """Preferences UI for interests, tone, memory toggle."""
    return render_template('preferences.html')

# ---------- SMALL JSON APIs ----------

@app.route('/api/profile', methods=['GET'])
def profile_api():
    """Return first user (for greeting) — expand later for auth."""
    user = User.query.first()
    return jsonify(user.to_dict())

@app.route('/api/preferences', methods=['GET', 'POST', 'DELETE'])
def preferences_api():
    """
    GET: return preferences
    POST: save/update preferences
    DELETE: reset preferences
    """
    pref = Preference.query.first()

    if request.method == 'GET':
        return jsonify(pref.to_dict() if pref else {})

    if request.method == 'POST':
        data = request.json or {}
        if not pref:
            pref = Preference()
            db.session.add(pref)
        pref.interests = ",".join(data.get('interests', []))
        pref.tone = data.get('tone', 'Friendly')
        pref.remember = bool(data.get('remember', True))
        db.session.commit()
        return jsonify({"ok": True, "saved": pref.to_dict()})

    if request.method == 'DELETE':
        if pref:
            db.session.delete(pref)
            db.session.commit()
        return jsonify({"ok": True})

# ---------- AI CHAT ENDPOINT ----------

@app.route('/chat', methods=['POST'])
def chat():
    """
    Body: { "message": "...", "tone": "Casual|Neutral|Professional" }
    Returns: { "reply": "..." }
    """
    data = request.json or {}
    text = data.get('message', '')
    tone = data.get('tone', 'Casual')
    # call simple local AI helper — you can swap with real GPT later
    reply = chat_response(text, city="Abu Dhabi", tone=tone)
    return jsonify({"reply": reply})

# ---------- RUN SERVER ----------
if __name__ == '__main__':
    app.run(debug=True)
