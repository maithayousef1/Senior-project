# Senior-project
Yalla app for UAE Discovery &amp; Itinerary Planner 

Perfect 🌟 thank you, Maitha — that gives me everything I need.
Based on your answers, here’s your **final, polished, university-ready, and GitHub-optimized `README.md`** — written naturally like a 22-year-old senior IT student project, but clear enough for professors and professional reviewers alike.

It blends a *human tone*, *academic professionalism*, and *technical clarity*.

---

```markdown
# 🌴 Yalla Planner — Smart AI Travel & Lifestyle Assistant for the UAE

Welcome to **Yalla Planner**, a senior project developed by three final-year **Information Technology students** majoring in **Web and App Development** at **Zayed University**.  

Our mission is simple — to make life in the **UAE** easier and more enjoyable by helping people **plan their day, explore new places, and manage events** through one intelligent, interactive platform.

---

## 🧠 Project Overview

**Yalla Planner** is an AI-powered lifestyle web application built using **Python (Flask)** that allows users to:
- Chat with an **AI assistant** to plan daily activities  
- Explore trending **places, events, and cafés** in the UAE  
- View personalized **itineraries** based on weather, mood, and preferences  
- Save favorite locations and customize settings  
- Enjoy a clean, minimal, and culturally aware user experience  

The project combines **technology, creativity, and real-world problem solving** — helping residents and tourists explore the UAE smarter.

---

## 🎓 Project Information

| Field             | Details                                   |
|-------            |          ----------                       |
| **Course**        |             CIT460 – Senior Project       |
| **University**    | Zayed University                          |
| **Major**         | Information Technology – Web & App Development |
| **Professor**     | Dr. Mohammed Kuhail                       |
| **Project Type**  | Final Year Capstone Project (2025)        |
| **Team Members**  | 3                                         |
| **Location**      | Abu Dhabi, UAE 🇦🇪                          |

---

## 👩🏻‍💻 Team Members & Roles

| Name | Role | Main Contributions |
|------|------|--------------------|
| **Maitha Yousef Alsaeedi** | AI Integration & Backend Logic | Flask setup, AI Chat design, data connections, testing |
| **Fatima Al Dahri** | Frontend Developer | UI/UX design, navigation system, planner and explore pages |
| **Ahmed Fahad** | API & Database Developer | Connected APIs (Maps, Weather, Events), PostgreSQL setup |

---

## 💡 Inspiration

We noticed that both **residents and tourists in the UAE** often struggle to find things to do or plan their day effectively.  
So we wanted to build something simple, elegant, and smart — a web assistant that **understands your preferences**, checks the **weather**, finds **places or events**, and helps you plan — all through one friendly chat interface.  

> “We wanted users to feel like they have a smart local friend helping them plan their day in the UAE.”

---

## 🧱 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask Framework) |
| **Database** | PostgreSQL |
| **AI Model** | (OpenAI / Groq – under integration) |
| **APIs** | Google Maps, Google Places, OpenWeatherMap, Eventbrite |
| **Design Tools** | Figma, Canva |
| **Environment** | PyCharm / VS Code |
| **Version Control** | GitHub |

---

## ⚙️ Project Structure

```

seniorproject_Yalla/
│
├── app.py                 → Main Flask app and route definitions
├── ai.py                  → Chatbot logic (Yalla AI responses)
├── models.py              → Database models (users, favorites, plans)
├── requirements.txt       → Dependencies
│
├── /services/             → Helper modules for smart features
│   ├── utils.py           → Tone, sentiment, and map helper functions
│   ├── weather.py         → Fetches weather data (OpenWeatherMap)
│   ├── places.py          → Finds UAE places via Google Places API
│   └── events.py          → Pulls event data from Eventbrite API
│
├── /templates/            → Frontend HTML pages
│   ├── base.html          → Shared layout (navbar, styles)
│   ├── home.html          → Welcome / landing page
│   ├── explore.html       → Discover UAE destinations
│   ├── planner.html       → Daily planner dashboard
│   ├── ai.html            → AI Chat page
│   ├── profile.html       → User profile & favorites
│   ├── preferences.html   → Personal preferences
│   └── index_backup.html  → Old layout (testing)
│
├── /static/               → Static design files
│   ├── style.css          → Global stylesheet
│   ├── app.js             → Main script
│   └── /images/
│        ├── logo.png
│        └── chatbot_icon.png
│
└── venv/ (ignored)        → Local virtual environment

````

---

## 🌟 Core Features

### 💬 1. AI Chat Assistant
- Friendly, conversational assistant (English & Arabic support planned)
- Suggests activities, cafés, and destinations  
- Generates 3-part itineraries (Morning / Afternoon / Evening)
- Adjusts based on **weather**, **tone**, and **budget**
- Responds visually with **icons, images, and maps**

### 🗓️ 2. Daily Planner
- Time-based activity cards  
- Mark tasks as ✅ Done or 🔁 Replace  
- Save events to calendar  
- Smart timeline (Morning / Afternoon / Evening)

### 🌆 3. Explore UAE
- AI-curated list of trending UAE destinations  
- Filters by “Nearby”, “Family”, “Free”, or “Popular”
- Displays **photos**, **ratings**, and **Google Maps** links

### 🌤️ 4. Weather-Aware Suggestions
- Uses OpenWeatherMap API  
- Suggests indoor/outdoor plans depending on conditions  

### ⚙️ 5. Personalized Preferences
- Choose tone (Friendly, Neutral, Professional)
- Select interests (Beaches, Cafés, Events, Fitness)
- Toggle “Allow AI to remember my preferences”

---

## 🎨 UI & Design

The interface follows a **modern-classic design** — minimal, clean, and comfortable to use.  
Inspired by the **UAE’s colors and lifestyle**, we used a soft **teal, beige, and white palette** to reflect simplicity and warmth.  

It’s responsive across devices and includes gentle shadows, glass effects, and animated transitions for a polished experience.

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/seniorproject_Yalla.git
cd seniorproject_Yalla
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate     # Windows
# or
source venv/bin/activate         # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Add your keys for APIs:

```bash
OPENAI_API_KEY=your_openai_key_here
OPENWEATHER_API_KEY=your_openweather_key_here
GOOGLE_PLACES_API_KEY=your_google_places_key_here
EVENTBRITE_TOKEN=your_eventbrite_token_here
DATABASE_URL=postgresql://user:password@localhost/yalla_planner
```

### 5. Run Flask

```bash
flask run
```

Then open → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧩 Future Enhancements

* ✅ Authentication system (Login / Register)
* ✅ Multi-language (Arabic + English)
* ✅ Voice chat assistant
* ✅ Budget-aware activity suggestions
* ✅ Community reviews & ratings
* ✅ Cloud deployment (Render or Replit)

---

## 👥 Team Reflections

> “We learned to bring design, logic, and AI together — to create something useful, smart, and uniquely Emirati.”

Through this project, we improved our **teamwork, API integration, problem-solving**, and **backend development** skills.
It was a hands-on experience in creating an **AI-driven real-world application** from concept to prototype.

---

## 📧 Contact

For inquiries or feedback:
📩 [202080207@zu.ac.ae](mailto:202080207@zu.ac.ae)
🌍 Abu Dhabi, United Arab Emirates

---

## 🪄 License

This project was developed for **educational and research purposes** at Zayed University.
All third-party APIs, data, and media belong to their respective owners.

---

> *“Plan smarter, live better — with Yalla Planner.”*

