# models.py
# SQLAlchemy models for Yalla Planner

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(80))
    country = db.Column(db.String(80))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "country": self.country}

class ItineraryItem(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title   = db.Column(db.String(120))
    date    = db.Column(db.String(20))   # keep simple for now
    time    = db.Column(db.String(10))
    city    = db.Column(db.String(80))
    notes   = db.Column(db.Text)

class Preference(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    interests = db.Column(db.Text, default="")    # CSV list e.g. "Cafes,Beaches"
    tone      = db.Column(db.String(20), default="Friendly")
    remember  = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "interests": [x for x in (self.interests or "").split(",") if x],
            "tone": self.tone,
            "remember": self.remember
        }
