import tkinter as tk
from tkinter import messagebox

from components import sounds


class LoginScreen:

    def __init__(self, root, login_success):

        self.root = root
        self.login_success = login_success

        self.attempts = 3

        self.frame = tk.Frame(
            root,
            bg="white",
            padx=30,
            pady=30
        )

        self.frame.pack(pady=80)

        tk.Label(
            self.frame,
            text="🏦 TechFact Bank",
            bg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=10)

        tk.Label(
            self.frame,
            text="Enter ATM PIN",
            bg="white",
            font=("Segoe UI", 14)
        ).pack()

        self.pin_entry = tk.Entry(
            self.frame,
            show="*",
            justify="center",
            font=("Segoe UI", 18)
        )

        self.pin_entry.pack(pady=15)

        # PIN typing sound
        self.pin_entry.bind(
            "<Key>",
            self.play_pin_sound
        )

        tk.Button(
            self.frame,
            text="Login",
            command=self.login,
            bg="#0074D9",
            fg="white",
            width=15,
            font=("Segoe UI", 12, "bold")
        ).pack(pady=10)

    # -----------------------
    # PIN Beep Sound
    # -----------------------

    def play_pin_sound(self, event):

        try:
            sounds.pin_beep()
        except:
            pass

    # -----------------------
    # Login
    # -----------------------

    def login(self):

        pin = self.pin_entry.get()

        # Empty PIN Check

        if not pin:

            messagebox.showwarning(
                "PIN Required",
                "Please enter ATM PIN."
            )

            return

        self.login_success(
            pin,
            self.attempts,
            self.frame
        )