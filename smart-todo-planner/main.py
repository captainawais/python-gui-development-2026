# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.dashboard import Dashboard

# ==========================
# APPLICATION
# ==========================


class TechFactHabitTrackApp:

    # ==========================
    # INIT
    # ==========================

    def __init__(self):

        self.window = tk.Tk()

        self.configure_window()

        Dashboard(self.window)

    # ==========================
    # WINDOW SETTINGS
    # ==========================

    def configure_window(self):

        self.window.title("TechFact Habit Track v2.0")

        self.window.geometry("1400x850")

        self.window.minsize(1200, 700)

        self.window.configure(bg="#F8FAFC")

        try:

            self.window.state("zoomed")

        except Exception:

            self.window.attributes("-zoomed", True)

        self.window.bind("<Escape>", lambda event: self.window.destroy())

    # ==========================
    # RUN APPLICATION
    # ==========================

    def run(self):

        self.window.mainloop()


# ==========================
# START APPLICATION
# ==========================

if __name__ == "__main__":

    app = TechFactHabitTrackApp()

    app.run()
