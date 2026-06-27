# ==========================
# IMPORTS
# ==========================

import tkinter as tk


# ==========================
# GAME TIMER CLASS
# ==========================

class GameTimer:

    # ==========================
    # INIT
    # ==========================

    def __init__(
        self,
        parent
    ):

        self.parent = parent

        self.seconds = 0

        self.running = False

        self.timer_id = None

        self.label = tk.Label(

            parent,

            text="⏱ Time : 00:00",

            bg="#0f172a",

            fg="#38bdf8",

            font=("Segoe UI", 12, "bold")

        )

        self.label.pack(
            pady=5
        )

    # ==========================
    # START TIMER
    # ==========================

    def start(self):

        self.running = True

        self.update()

    # ==========================
    # UPDATE TIMER
    # ==========================

    def update(self):

        if not self.running:

            return

        self.seconds += 1

        minutes = self.seconds // 60

        seconds = self.seconds % 60

        self.label.config(

            text=f"⏱ Time : {minutes:02}:{seconds:02}"

        )

        self.timer_id = self.parent.after(

            1000,

            self.update

        )

    # ==========================
    # STOP TIMER
    # ==========================

    def stop(self):

        self.running = False

        if self.timer_id:

            self.parent.after_cancel(
                self.timer_id
            )

    # ==========================
    # RESET TIMER
    # ==========================

    def reset(self):

        self.stop()

        self.seconds = 0

        self.label.config(
            text="⏱ Time : 00:00"
        )

    # ==========================
    # GET TIME
    # ==========================

    def get_time(self):

        return self.seconds