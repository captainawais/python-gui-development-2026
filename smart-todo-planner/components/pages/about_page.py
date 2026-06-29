# ==========================
# IMPORTS
# ==========================

import tkinter as tk

# ==========================
# ABOUT PAGE
# ==========================


class AboutPage:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        # ==========================
        # PAGE TITLE
        # ==========================

        tk.Label(
            parent,
            text="About",
            bg="#F8FAFC",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(pady=(30, 5))

        tk.Label(
            parent,
            text="TechFact Habit Track Information",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 12),
        ).pack(pady=(0, 25))

        # ==========================
        # ABOUT CARD
        # ==========================

        card = tk.Frame(parent, bg="white", bd=1, relief="solid")

        card.pack(fill="x", padx=30, pady=20)

        tk.Label(
            card,
            text="📖 About Application",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        about_text = (
            "TechFact Habit Track is a modern desktop application "
            "designed to help users build consistent daily habits, "
            "track progress in real time, monitor streaks, "
            "analyze statistics and improve productivity.\n\n"
            "The application stores all habit data locally using JSON "
            "and is designed with a modular architecture that can "
            "easily be migrated to SQLite, Django REST API or any "
            "other backend in future versions."
        )

        tk.Label(
            card,
            text=about_text,
            justify="left",
            wraplength=850,
            bg="white",
            fg="#475569",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=20, pady=(0, 20))

        # ==========================
        # PROJECT INFORMATION
        # ==========================

        info = tk.Frame(parent, bg="white", bd=1, relief="solid")

        info.pack(fill="x", padx=30, pady=20)

        tk.Label(
            info,
            text="📋 Project Information",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        self.add_item(info, "Application", "TechFact Habit Track")
        self.add_item(info, "Version", "2.0")
        self.add_item(info, "Architecture", "V2 Modular")
        self.add_item(info, "Backend", "JSON Storage")
        self.add_item(info, "UI Framework", "Tkinter")
        self.add_item(info, "Language", "Python 3")

        # ==========================
        # DEVELOPER
        # ==========================

        developer = tk.Frame(parent, bg="white", bd=1, relief="solid")

        developer.pack(fill="x", padx=30, pady=20)

        tk.Label(
            developer,
            text="👨‍💻 Developer",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        self.add_item(developer, "Name", "Engr. Awais Farooq")
        self.add_item(developer, "Role", "Software Engineer")
        self.add_item(developer, "Project", "TechFact Habit Track")
        self.add_item(developer, "License", "MIT License")

        # ==========================
        # TECHNOLOGY STACK
        # ==========================

        stack = tk.Frame(parent, bg="white", bd=1, relief="solid")

        stack.pack(fill="x", padx=30, pady=20)

        tk.Label(
            stack,
            text="🚀 Technology Stack",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 15))

        technologies = [
            "🐍 Python",
            "🖥 Tkinter",
            "📂 JSON Storage",
            "📊 Matplotlib",
            "🏗 Modular Architecture",
            "🔄 Real-Time Data Management",
        ]

        for tech in technologies:

            tk.Label(
                stack, text=tech, bg="white", fg="#374151", font=("Segoe UI", 11)
            ).pack(anchor="w", padx=30, pady=4)

        # ==========================
        # FOOTER
        # ==========================

        tk.Label(
            parent,
            text="© 2026 TechFact Habit Track • All Rights Reserved",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 10),
        ).pack(pady=25)

    # ==========================
    # ADD ITEM
    # ==========================

    def add_item(self, parent, title, value):

        row = tk.Frame(parent, bg="white")

        row.pack(fill="x", padx=20, pady=6)

        tk.Label(row, text=title, bg="white", fg="#374151", font=("Segoe UI", 11)).pack(
            side="left"
        )

        tk.Label(
            row, text=value, bg="white", fg="#2563EB", font=("Segoe UI", 11, "bold")
        ).pack(side="right")
