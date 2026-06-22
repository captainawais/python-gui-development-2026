import tkinter as tk
from tkinter import ttk

from components import sounds


class LoadingScreen:

    def __init__(
        self,
        root,
        message="Processing Transaction..."
    ):

        # ==========================
        # WINDOW
        # ==========================

        self.win = tk.Toplevel(root)

        self.win.title(
            "TechFact Bank ATM"
        )

        self.win.geometry(
            "450x250"
        )

        self.win.configure(
            bg="#001f3f"
        )

        self.win.resizable(
            False,
            False
        )

        self.win.grab_set()

        # ==========================
        # BANK TITLE
        # ==========================

        tk.Label(
            self.win,
            text="🏦 TechFact Bank",
            bg="#001f3f",
            fg="white",
            font=("Segoe UI", 18, "bold")
        ).pack(
            pady=(20, 5)
        )

        # ==========================
        # PROCESSING MESSAGE
        # ==========================

        tk.Label(
            self.win,
            text=message,
            bg="#001f3f",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(
            pady=10
        )

        # ==========================
        # STATUS LABEL
        # ==========================

        self.status_label = tk.Label(
            self.win,
            text="Please Wait",
            bg="#001f3f",
            fg="cyan",
            font=("Segoe UI", 11)
        )

        self.status_label.pack()

        # ==========================
        # PROGRESS BAR
        # ==========================

        self.progress = ttk.Progressbar(
            self.win,
            orient="horizontal",
            length=320,
            mode="indeterminate"
        )

        self.progress.pack(
            pady=20
        )

        self.progress.start(10)

        # ==========================
        # ANIMATION LABEL
        # ==========================

        self.dots = tk.Label(
            self.win,
            text="",
            bg="#001f3f",
            fg="#2ECC40",
            font=("Segoe UI", 20, "bold")
        )

        self.dots.pack()

        self.count = 0

        # ==========================
        # START LOADING SOUND
        # ==========================

        try:
            sounds.loading()
        except:
            pass

        self.animate()

    # ==========================
    # DOTS ANIMATION
    # ==========================

    def animate(self):

        self.count += 1

        dots_text = "." * (self.count % 4)

        self.dots.config(
            text=dots_text
        )

        messages = [
            "Verifying Information",
            "Processing Request",
            "Connecting Secure Server",
            "Finalizing Transaction"
        ]

        self.status_label.config(
            text=messages[
                self.count % len(messages)
            ]
        )

        self.win.after(
            500,
            self.animate
        )

    # ==========================
    # CLOSE WINDOW
    # ==========================

    def close(self):

        try:
            self.progress.stop()
        except:
            pass

        try:
            sounds.stop()
        except:
            pass

        self.win.destroy()