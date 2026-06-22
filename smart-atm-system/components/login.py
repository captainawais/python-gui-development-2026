import tkinter as tk
from tkinter import messagebox

from components import sounds

class LoginScreen:


    def __init__(
        self,
        root,
        selected_user,
        login_success
    ):

        self.root = root
        self.selected_user = selected_user
        self.login_success = login_success

        self.attempts = 3

        # ==========================
        # MAIN FRAME
        # ==========================

        self.frame = tk.Frame(
            root,
            bg="white",
            padx=40,
            pady=40
        )

        self.frame.pack(
            expand=True
        )

        # ==========================
        # BANK TITLE
        # ==========================

        tk.Label(
            self.frame,
            text="🏦 TechFact Bank ATM",
            bg="white",
            fg="#001f3f",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(0, 15)
        )

        tk.Label(
            self.frame,
            text="Secure Banking System",
            bg="white",
            fg="gray",
            font=("Segoe UI", 11)
        ).pack()

        # ==========================
        # CARD VERIFIED
        # ==========================

        tk.Label(
            self.frame,
            text="💳 Card Verified",
            bg="white",
            fg="#2ECC40",
            font=("Segoe UI", 14, "bold")
        ).pack(
            pady=20
        )

        # ==========================
        # USER INFO
        # ==========================

        tk.Label(
            self.frame,
            text="Card Holder",
            bg="white",
            fg="gray",
            font=("Segoe UI", 10)
        ).pack()

        tk.Label(
            self.frame,
            text=self.selected_user["name"],
            bg="white",
            fg="#001f3f",
            font=("Segoe UI", 16, "bold")
        ).pack()

        tk.Label(
            self.frame,
            text=self.selected_user["account"],
            bg="white",
            fg="gray",
            font=("Consolas", 13)
        ).pack(
            pady=(0, 20)
        )

        # ==========================
        # PIN LABEL
        # ==========================

        tk.Label(
            self.frame,
            text="Enter ATM PIN",
            bg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(
            pady=(10, 5)
        )

        # ==========================
        # PIN ENTRY
        # ==========================

        self.pin_entry = tk.Entry(
            self.frame,
            show="*",
            width=20,
            justify="center",
            font=("Segoe UI", 18)
        )

        self.pin_entry.pack()

        self.pin_entry.bind(
            "<Key>",
            self.play_pin_sound
        )

        # ==========================
        # ATTEMPTS LABEL
        # ==========================

        self.attempt_label = tk.Label(
            self.frame,
            text="Attempts Remaining: 3",
            bg="white",
            fg="red",
            font=("Segoe UI", 10, "bold")
        )

        self.attempt_label.pack(
            pady=10
        )

        # ==========================
        # LOGIN BUTTON
        # ==========================

        tk.Button(
            self.frame,
            text="🔐 Login",
            command=self.login,
            bg="#0074D9",
            fg="white",
            width=20,
            height=2,
            font=("Segoe UI", 11, "bold")
        ).pack(
            pady=15
        )

    # ==========================
    # PIN SOUND
    # ==========================

    def play_pin_sound(
        self,
        event
    ):

        try:
            sounds.pin_beep()
        except:
            pass

    # ==========================
    # LOGIN
    # ==========================

    def login(self):

        pin = self.pin_entry.get().strip()

        if not pin:

            messagebox.showwarning(
                "Required",
                "Please enter ATM PIN."
            )

            return

        sounds.click()

        self.login_success(
            self.selected_user,
            pin,
            self.attempts,
            self.frame,
            self
        )

    # ==========================
    # UPDATE ATTEMPTS
    # ==========================

    def update_attempts(self):

        self.attempt_label.config(
            text=f"Attempts Remaining: {self.attempts}"
        )

