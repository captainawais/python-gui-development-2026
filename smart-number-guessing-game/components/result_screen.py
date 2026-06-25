# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.home_screen import HomeScreen


# ==========================
# RESULT SCREEN CLASS
# ==========================

class ResultScreen:

    # ==========================
    # INIT
    # ==========================

    def __init__(
        self,
        root,
        win,
        score,
        secret_number
    ):

        self.root = root

        self.win = win

        self.score = score

        self.secret_number = secret_number

        # Main Frame

        self.frame = tk.Frame(
            root,
            bg="#0f172a"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # Show Result

        if self.win:

            self.show_win()

        else:

            self.show_lose()

    # ==========================
    # WIN SCREEN
    # ==========================

    def show_win(self):

        tk.Label(
            self.frame,
            text="🏆 Congratulations!",
            bg="#0f172a",
            fg="#22c55e",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=40
        )

        tk.Label(
            self.frame,
            text=f"You Guessed : {self.secret_number}",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI", 14)
        ).pack(
            pady=10
        )

        tk.Label(
            self.frame,
            text=f"Final Score : {self.score}",
            bg="#0f172a",
            fg="cyan",
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=10
        )

        tk.Button(
            self.frame,
            text="🔄 Play Again",
            command=self.play_again,
            bg="#22c55e",
            fg="white",
            width=20,
            height=2
        ).pack(
            pady=40
        )

    # ==========================
    # LOSE SCREEN
    # ==========================

    def show_lose(self):

        tk.Label(
            self.frame,
            text="❌ Game Over",
            bg="#0f172a",
            fg="red",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=40
        )

        tk.Label(
            self.frame,
            text=f"Correct Number : {self.secret_number}",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI", 14)
        ).pack(
            pady=10
        )

        tk.Button(
            self.frame,
            text="🔄 Try Again",
            command=self.play_again,
            bg="#2563eb",
            fg="white",
            width=20,
            height=2
        ).pack(
            pady=40
        )

    # ==========================
    # PLAY AGAIN
    # ==========================

    def play_again(self):

        self.frame.destroy()

        HomeScreen(
            self.root
        )