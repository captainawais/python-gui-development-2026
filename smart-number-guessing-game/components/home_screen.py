# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from tkinter import messagebox
from utils.game_stats import GameStats
from components.game_screen import GameScreen
from utils.xp_system import XPSystem
from components.statistics_panel import StatisticsPanel 

# ==========================
# HOME SCREEN CLASS
# ==========================

class HomeScreen:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, root):

        self.root = root
        self.difficulty = tk.StringVar()
        self.stats = GameStats()
        self.xp = XPSystem()
        # Main Frame

        self.frame = tk.Frame(
            root,
            bg="#0f172a"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # Selected Difficulty

        self.difficulty = tk.StringVar(value="easy")

        # Build UI

        self.create_title()

        self.create_difficulty()

        self.create_start_button()
        StatisticsPanel(
         self.frame
            )
        tk.Button(
            self.frame,
            text="📊 Statistics",
            command=self.open_statistics,
            bg="#2563eb",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=20,
            height=2,
            border=0
        ).pack(pady=15)


    # ==========================
    # TITLE SECTION
    # ==========================

    def create_title(self):

        tk.Label(
            self.frame,
            text="🎯 Smart Number Guessing Game",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=50
        )

        tk.Label(
            self.frame,
            text="Version 1.2",
            bg="#0f172a",
            fg="#38bdf8",
            font=("Segoe UI", 13, "bold")
        ).pack(
            pady=(0, 40)
        )
        
        tk.Label(
            self.frame,
            text=f"🔥 Current Streak : {self.stats.get_current_streak()}",
            bg="#0f172a",
            fg="#22c55e",
            font=("Segoe UI", 11, "bold")
        ).pack()

        tk.Label(
            self.frame,
            text=f"👑 Best Streak : {self.stats.get_best_streak()}",
            bg="#0f172a",
            fg="#facc15",
            font=("Segoe UI", 11, "bold")
        ).pack(pady=(5,20))

        tk.Label(
            self.frame,
            text=f"⭐ Level : {self.xp.get_level()}",
            bg="#0f172a",
            fg="#38bdf8",
            font=("Segoe UI",11,"bold")
        ).pack()

        tk.Label(
            self.frame,
            text=f"💎 XP : {self.xp.get_xp()}",
            bg="#0f172a",
            fg="#22c55e",
            font=("Segoe UI",11,"bold")
        ).pack(
            pady=(5,20)
        )



    # ==========================
    # DIFFICULTY SECTION
    # ==========================

    def create_difficulty(self):

        tk.Label(
            self.frame,
            text="Select Difficulty",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(
            pady=(20, 10)
        )

        difficulty_frame = tk.LabelFrame(
            self.frame,
            text=" Difficulty ",
            bg="#0f172a",
            fg="white",
            padx=20,
            pady=15,
            font=("Segoe UI", 11, "bold")
        )

        difficulty_frame.pack()

        tk.Radiobutton(
            difficulty_frame,
            text="Easy (1-50)",
            variable=self.difficulty,
            value="easy",
            bg="#0f172a",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 11)
        ).pack(
            anchor="w"
        )

        tk.Radiobutton(
            difficulty_frame,
            text="Medium (1-100)",
            variable=self.difficulty,
            value="medium",
            bg="#0f172a",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 11)
        ).pack(
            anchor="w"
        )

        tk.Radiobutton(
            difficulty_frame,
            text="Hard (1-500)",
            variable=self.difficulty,
            value="hard",
            bg="#0f172a",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 11)
        ).pack(
            anchor="w"
        )

    # ==========================
    # START BUTTON
    # ==========================

    def create_start_button(self):

        tk.Button(
            self.frame,
            text="▶ Start Game",
            command=self.start_game,
            bg="#22c55e",
            fg="white",
            width=20,
            height=2,
            font=("Segoe UI", 11, "bold"),
            border=0
        ).pack(
            pady=30
        )


    # ==========================
    # START GAME
    # ==========================

    def start_game(self):

        if not self.difficulty.get():

            messagebox.showwarning(
                "Difficulty Required",
                "Please select a difficulty level."
            )

            return

        # Close Home Screen

        self.frame.destroy()

        # Open Game Screen

        GameScreen(
            self.root,
            self.difficulty.get()
        )
        
    def open_statistics(self):

        from components.statistics_panel import StatisticsPanel

        StatisticsPanel(self.root)   