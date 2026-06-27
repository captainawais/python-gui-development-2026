# ==========================
# IMPORTS
# ==========================

import tkinter as tk
import random
from tkinter import messagebox
from utils.game_stats import GameStats
from utils.xp_system import XPSystem
from components.timer import GameTimer
from components.sounds import (
    play_click,
    play_win,
    play_lose,
    play_near,
    play_far,
    play_error
)


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
        
        # Game Managers

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

        # Build Screen

        self.initialize_game()

        self.create_header()
        
        self.timer = GameTimer(
            self.frame
        )

        self.timer.start()

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



    # ==========================
    # HEADER
    # ==========================

    def create_header(self):

        tk.Label(
            self.frame,
            text="🎯 Guess The Number",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(30,10)
        )

        tk.Label(
            self.frame,
            text=f"Difficulty : {self.difficulty.title()}",
            bg="#0f172a",
            fg="#facc15",
            font=("Segoe UI", 12, "bold")
        ).pack(
            pady=(0, 30)
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
        self.guess_entry.focus_set()
        
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
                play_error()
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter numbers only."
                )

                self.guess_entry.delete(
                    0,
                    tk.END
                )

                self.guess_entry.focus_set()

                return


            # Attempts

            self.attempts_left -= 1

            self.update_attempts()

            
            play_click()
            
            # Correct Guess

            if guess == self.secret_number:

                self.correct_guess()

                return
            

            # Smart Hint

            self.show_hint(
                guess
            )


            # Score

            self.update_score()


            # Game Over

            if self.attempts_left <= 0:

                self.game_over()

            return


    # ==========================
    # SMART HINT SYSTEM
    # ==========================

    def show_hint(self, guess):

        difference = abs(
            guess - self.secret_number
        )

        # Difficulty Wise Range

        if self.difficulty == "easy":

            very_close = 2
            close = 5
            medium = 10

        elif self.difficulty == "medium":

            very_close = 5
            close = 10
            medium = 20

        else:

            very_close = 10
            close = 20
            medium = 40

        # Decide Direction

        if guess < self.secret_number:

            direction = "Try Higher ⬆"

        else:

            direction = "Try Lower ⬇"

        # Very Close

        if difference <= very_close:
            play_near()
            self.hint_label.config(
                text=f"🔥 Very Close! Go {direction}",
                fg="#22c55e"
            )

        # Close

        elif difference <= close:
            play_near()
            self.hint_label.config(
                text=f"😊 Close! Go {direction}",
                fg="#38bdf8"
            )

        # Medium

        elif difference <= medium:
            play_near()
            self.hint_label.config(
                text=f"🙂 Getting Closer! Go {direction}",
                fg="#facc15"
            )

        # Far

        else:
            play_far()
            self.hint_label.config(
                text=f"😅 Too Far! Go {direction}",
                fg="#f97316"
            )
            
        
    # ==========================
    # CORRECT GUESS
    # ==========================
    
    
    def correct_guess(self):

        # ==========================
        # SAVE GAME STATS
        # ==========================
        
                # Stop Timer

        self.timer.stop()

        # Play Win Sound

        play_win()

        # Total Guesses

        guesses = self.max_attempts - self.attempts_left

        # ==========================
        # UPDATE GAME STATS
        # ==========================

        self.stats.update_games_played()

        self.stats.update_games_won()

        self.stats.update_total_score(
            self.score
        )

        self.stats.update_total_guesses(
            guesses
        )

        self.stats.update_high_score(
            self.difficulty,
            self.score
        )

        self.stats.update_win_streak()
        
        # ==========================
        # ADD XP
        # ==========================

        self.xp.add_xp(
            self.score
        )


        # ==========================
        # CHECK ACHIEVEMENTS
        # ==========================

        from utils.achievement_manager import AchievementManager

        achievement = AchievementManager()

        unlocked = achievement.check(

            score=self.score,

            attempts=guesses,

            difficulty=self.difficulty,

            seconds=self.timer.get_time()

        )


        # ==========================
        # SHOW ACHIEVEMENT POPUPS
        # ==========================

        from components.achievement_popup import AchievementPopup

        for item in unlocked:

            AchievementPopup(
                self.root,
                item
            )

        # ==========================
        # CLOSE GAME SCREEN
        # ==========================

        self.frame.destroy()
    

        # ==========================
        # OPEN RESULT SCREEN
        # ==========================

        from components.result_screen import ResultScreen

        ResultScreen(

            self.root,

            True,

            self.score,

            self.secret_number,

            self.timer.get_time(),
            self.difficulty

        )  
            
    
    # ==========================
    # UPDATE SCORE
    # ==========================

    def update_score(self):

        # Reduce Score

        self.score = max(
            0,
            self.score - 10
        )

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
        play_lose()
        # Close Current Screen

        self.frame.destroy()
        self.stats.update_games_lost()
        self.stats.reset_win_streak()
        self.xp.add_xp(
            5
        )

        # Open Result Screen

        from components.result_screen import ResultScreen

        ResultScreen(
            self.root,
            False,
            self.score,
            self.secret_number,
            self.timer.get_time(),
            self.difficulty
        )
