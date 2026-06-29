```markdown
# 🚀 TechFact Habit Track v2.0

A modern desktop Habit Tracker application built with **Python** and **Tkinter**. The project is designed using a modular architecture and stores data in JSON, making it ready for future migration to **Django + REST API + PostgreSQL**.

---

# ✨ Features

- ✅ Beautiful Modern UI
- ✅ Dashboard Overview
- ✅ Habit Management
- ✅ Weekly Progress Tracking
- ✅ Monthly Calendar
- ✅ Statistics Dashboard
- ✅ Streak Tracking
- ✅ Settings Page
- ✅ About Page
- ✅ Real-Time JSON Storage
- ✅ Progress Charts
- ✅ Scrollable Layout
- ✅ Responsive Desktop Design
- ✅ Future Backend Ready

---

# 📂 Project Structure

```

smart-todo-planner/

│
├── assets/
│   ├── icons/
│   └── images/
│
├── components/
│   ├── pages/
│   │   ├── dashboard_page.py
│   │   ├── habits_page.py
│   │   ├── calendar_page.py
│   │   ├── statistics_page.py
│   │   ├── streak_page.py
│   │   ├── settings_page.py
│   │   ├── about_page.py
│   │   └── progress_page.py
│   │
│   ├── dashboard.py
│   ├── sidebar.py
│   ├── habit_table.py
│   ├── calendar.py
│   ├── statistics.py
│   ├── progress_panel.py
│   └── footer.py
│
├── data/
│   ├── habits.json
│   └── settings.json
│
├── utils/
│   ├── storage.py
│   ├── dashboard_service.py
│   ├── charts.py
│   ├── helpers.py
│   ├── notification.py
│   └── settings.py
│
├── main.py
├── requirements.txt
└── README.md

```

---

# 🖥️ Application Pages

- 🏠 Dashboard
- ✅ Habits
- 📅 Calendar
- 📊 Statistics
- 🔥 Streak
- ⚙️ Settings
- ℹ️ About

---

# 📊 Dashboard

Dashboard displays real-time information including:

- Total Habits
- Completed Tasks
- Pending Tasks
- Success Rate
- Current Streak
- Best Streak
- Weekly Progress Chart

---

# ✅ Habits

- Track daily habits
- 7-day completion system
- Auto percentage calculation
- Save progress
- Real-time updates

---

# 📅 Calendar

Calendar automatically reads saved data and highlights completed activity.

Features:

- Monthly View
- Current Day Highlight
- Completed Day Indicator
- Real-Time History Support

---

# 📈 Statistics

Displays:

- Total Habits
- Completed
- Pending
- Success Rate
- Weekly Progress Chart

---

# 🔥 Streak

Track:

- Current Streak
- Best Streak
- Success Percentage
- Weekly Summary

---

# ⚙️ Settings

User preferences include:

- Notifications
- Dark Mode (Future)
- Auto Save
- Reset Data

Settings are stored separately inside:

```

data/settings.json

```

---

# 💾 Data Storage

Habit data is stored inside:

```

data/habits.json

```

Settings are stored inside:

```

data/settings.json

````

No database is required in Version 2.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/techfact-habit-track.git
````

Open the project:

```bash
cd smart-todo-planner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

# 🛠️ Technologies Used

* Python
* Tkinter
* JSON
* Matplotlib
* Pillow
* TkCalendar

---

# 🚀 Future Roadmap (Version 3)

* Django Backend
* Django REST Framework
* PostgreSQL
* User Authentication
* Cloud Sync
* Multi-Device Support
* Login System
* Email Notifications
* Analytics Dashboard
* Habit Categories
* AI Habit Suggestions

---

# 👨‍💻 Developer

**Engr. Awais Farooq**

Software Engineer

GitHub:
https://github.com/captainawais

LinkedIn:
https://linkedin.com/in/awais-farooq-388346405

---

# 📜 License

This project is developed for educational and portfolio purposes.

© 2026 Engr. Awais Farooq. All Rights Reserved.

```
```
