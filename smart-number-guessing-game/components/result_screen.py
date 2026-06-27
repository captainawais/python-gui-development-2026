# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from components.footer import Footer 
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
        secret_number,
        time_taken,
        difficulty
    ):

        self.root = root

        self.win = win

        self.score = score

        self.secret_number = secret_number

        self.time_taken = time_taken

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

        # Show Result

        if self.win:

            self.show_win()

        else:

            self.show_lose()
            
            Footer(self.frame)

    # ==========================
    # WIN SCREEN
    # ==========================

    def show_win(self):

        minutes = self.time_taken // 60
        seconds = self.time_taken % 60

        tk.Label(
            self.frame,
            text="🏆",
            bg="#0f172a",
            fg="#facc15",
            font=("Segoe UI", 60)
        ).pack(
            pady=(20,5)
        )

        tk.Label(
            self.frame,
            text="YOU WON!",
            bg="#0f172a",
            fg="#22c55e",
            font=("Segoe UI",26,"bold")
        ).pack()

        tk.Label(
            self.frame,
            text=f"⭐ Score : {self.score}",
            bg="#0f172a",
            fg="cyan",
            font=("Segoe UI",15,"bold")
        ).pack(
            pady=5
        )

        tk.Label(
            self.frame,
            text=f"⏱ Time : {minutes:02}:{seconds:02}",
            bg="#0f172a",
            fg="#38bdf8",
            font=("Segoe UI",13)
        ).pack()

        tk.Label(
            self.frame,
            text=f"🎯 Number : {self.secret_number}",
            bg="#0f172a",
            fg="#facc15",
            font=("Segoe UI",13)
        ).pack()

        tk.Label(
            self.frame,
            text=f"🎮 Difficulty : {self.difficulty.title()}",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI",12)
        ).pack(
            pady=(5,20)
        )

        tk.Button(
            self.frame,
            text="🔄 Play Again",
            command=self.play_again,
            bg="#2563eb",
            fg="white",
            width=22,
            height=2
        ).pack(
            pady=5
        )

        tk.Button(
            self.frame,
            text="🏠 Home",
            command=self.go_home,
            bg="#22c55e",
            fg="white",
            width=22,
            height=2
        ).pack()

    # ==========================
    # LOSE SCREEN
    # ==========================

    def show_lose(self):

        minutes = self.time_taken // 60
        seconds = self.time_taken % 60

        tk.Label(
            self.frame,
            text="💀",
            bg="#0f172a",
            fg="red",
            font=("Segoe UI",60)
        ).pack(
            pady=(20,5)
        )

        tk.Label(
            self.frame,
            text="GAME OVER",
            bg="#0f172a",
            fg="red",
            font=("Segoe UI",24,"bold")
        ).pack()

        tk.Label(
            self.frame,
            text=f"Correct Number : {self.secret_number}",
            bg="#0f172a",
            fg="white",
            font=("Segoe UI",14)
        ).pack(
            pady=5
        )

        tk.Label(
            self.frame,
            text=f"⏱ Time : {minutes:02}:{seconds:02}",
            bg="#0f172a",
            fg="#38bdf8",
            font=("Segoe UI",13)
        ).pack(
            pady=(5,20)
        )

        tk.Button(
            self.frame,
            text="🔄 Try Again",
            command=self.play_again,
            bg="#2563eb",
            fg="white",
            width=22,
            height=2
        ).pack(
            pady=5
        )

        tk.Button(
            self.frame,
            text="🏠 Home",
            command=self.go_home,
            bg="#22c55e",
            fg="white",
            width=22,
            height=2
        ).pack()

    # ==========================
    # PLAY AGAIN
    # ==========================

    def play_again(self):

        # Close Result Screen
        self.frame.destroy()

        # Remove old Enter binding
        self.root.unbind("<Return>")

        from components.game_screen import GameScreen

        GameScreen(
            self.root,
            self.difficulty
        )
        
    # ==========================
    # GO HOME
    # ==========================

    def go_home(self):

        # Close Result Screen
        self.frame.destroy()

        # Remove old Enter binding
        self.root.unbind("<Return>")

        HomeScreen(
            self.root
        )    