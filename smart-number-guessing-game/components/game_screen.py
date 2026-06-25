# ==========================
# IMPORTS
# ==========================

import tkinter as tk
import random
from tkinter import messagebox


# ==========================
# GAME SCREEN CLASS
# ==========================

class GameScreen:

    # ==========================
    # INIT
    # ==========================

    def __init__(
        self,
        root,
        difficulty
    ):

        self.root = root

        self.difficulty = difficulty

        # Main Frame

        self.frame = tk.Frame(
            root,
            bg="#0f172a"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # Build Screen

        self.initialize_game()

        self.create_header()

        self.create_guess_input()

        self.create_attempts_label()

        self.create_score_label()

        self.create_hint_label()


    # ==========================
    # GAME VARIABLES
    # ==========================

    def initialize_game(self):

        self.secret_number = 0

        self.max_attempts = 0

        self.attempts_left = 0

        self.score = 100

        # Easy

        if self.difficulty == "easy":

            self.secret_number = random.randint(
                1,
                50
            )

            self.max_attempts = 10

        # Medium

        elif self.difficulty == "medium":

            self.secret_number = random.randint(
                1,
                100
            )

            self.max_attempts = 8

        # Hard

        else:

            self.secret_number = random.randint(
                1,
                500
            )

            self.max_attempts = 6

        self.attempts_left = self.max_attempts

        print(
            self.secret_number
        )


    # ==========================
    # HEADER
    # ==========================

    def create_header(self):

        tk.Label(
            self.frame,
            text=f"Difficulty : {self.difficulty.title()}",
            bg="#0f172a",
            fg="#facc15",
            font=("Segoe UI", 11, "bold")
        ).pack(
            pady=(0, 20)
        )

    # ==========================
    # GUESS INPUT SECTION
    # ==========================

    def create_guess_input(self):

        tk.Label(
            self.frame,
            text="Enter Your Guess",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack()

        self.guess_entry = tk.Entry(
            self.frame,
            width=20,
            justify="center",
            font=("Segoe UI", 16)
        )

        self.guess_entry.pack(
            pady=10
        )
        self.guess_entry.bind(
            "<Return>",
            lambda event: self.check_guess()
        )

        self.guess_btn = tk.Button(
            self.frame,
            text="🎯 Guess",
            command=self.check_guess,
            bg="#2563eb",
            fg="white",
            width=15,
            height=2
        )

        self.guess_btn.pack(
            pady=10
        )


    # ==========================
    # ATTEMPTS SECTION
    # ==========================

    def create_attempts_label(self):

        self.attempt_label = tk.Label(
            self.frame,
            text=f"Attempts Left : {self.attempts_left}",
            bg="#0f172a",
            fg="orange",
            font=("Segoe UI", 12, "bold")
        )

        self.attempt_label.pack()


    # ==========================
    # SCORE SECTION
    # ==========================

    def create_score_label(self):

        self.score_label = tk.Label(
            self.frame,
            text=f"Score : {self.score}",
            bg="#0f172a",
            fg="#22c55e",
            font=("Segoe UI", 12, "bold")
        )

        self.score_label.pack()


    # ==========================
    # HINT SECTION
    # ==========================

    def create_hint_label(self):

        self.hint_label = tk.Label(
            self.frame,
            text="Start Guessing...",
            bg="#0f172a",
            fg="cyan",
            font=("Segoe UI", 12, "bold")
        )

        self.hint_label.pack(
            pady=20
        )


        # ==========================
        # CHECK GUESS
        # =========================
        
    def check_guess(self):

            # Empty Input

            if not self.guess_entry.get().strip():

                messagebox.showwarning(
                    "Input Required",
                    "Please Enter A Number."
                )

                return

            # Invalid Input

            try:

                guess = int(
                    self.guess_entry.get()
                )

            except:

                messagebox.showerror(
                    "Invalid Input",
                    "Only Numbers Are Allowed."
                )

                return

            # Attempts

            self.attempts_left -= 1

            self.update_attempts()

            # Correct Guess

            if guess == self.secret_number:

                self.correct_guess()

                return

            # Too High

            if guess > self.secret_number:

                self.show_too_high()

            # Too Low

            else:

                self.show_too_low()

            # Score

            self.update_score()

            # Game Over

            if self.attempts_left <= 0:

                self.game_over()

            # Clear Entry

            self.guess_entry.delete(
                0,
                tk.END
            )


    # ==========================
    # TOO HIGH
    # ==========================

    def show_too_high(self):

        self.hint_label.config(
            text="📈 Too High! Try A Smaller Number.",
            fg="orange"
        )


    # ==========================
    # TOO LOW
    # ==========================

    def show_too_low(self):

        self.hint_label.config(
            text="📉 Too Low! Try A Bigger Number.",
            fg="cyan"
        )


    # ==========================
    # CORRECT GUESS
    # ==========================

    def correct_guess(self):

        messagebox.showinfo(
            "Congratulations 🎉",
            f"You Guessed The Correct Number!\n\n"
            f"Your Score : {self.score}"
        )

        # Close Game Screen

        self.frame.destroy()

        # Open Result Screen

        from components.result_screen import ResultScreen

        ResultScreen(
            self.root,
            True,
            self.score,
            self.secret_number
        )
        
    # ==========================
    # UPDATE SCORE
    # ==========================

    def update_score(self):

        # Reduce Score

        self.score -= 10

        # Minimum Score

        if self.score < 0:

            self.score = 0

        # Update Label

        self.score_label.config(
            text=f"Score : {self.score}"
        )

    # ==========================
    # UPDATE ATTEMPTS
    # ==========================

    def update_attempts(self):

        self.attempt_label.config(
            text=f"Attempts Left : {self.attempts_left}"
        )
    
    # ==========================
    # GAME OVER
    # ==========================

    def game_over(self):

        # Close Current Screen

        self.frame.destroy()

        # Open Result Screen

        from components.result_screen import ResultScreen

        ResultScreen(
            self.root,
            False,
            self.score,
            self.secret_number
        )
