# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from tkinter import messagebox

from components.game_screen import GameScreen


# ==========================
# HOME SCREEN CLASS
# ==========================

class HomeScreen:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, root):

        self.root = root

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

        self.difficulty = tk.StringVar()

        # Build UI

        self.create_title()

        self.create_difficulty()

        self.create_start_button()

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
            text="Version 1.0",
            bg="#0f172a",
            fg="cyan",
            font=("Segoe UI", 14)
        ).pack(
            pady=(0, 30)
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

        difficulty_frame = tk.Frame(
            self.frame,
            bg="#0f172a"
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