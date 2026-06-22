import tkinter as tk
from tkinter import ttk

from components import sounds

class CardScreen:


    def __init__(
        self,
        root,
        users_data,
        continue_callback
    ):

        self.root = root
        self.users_data = users_data
        self.continue_callback = continue_callback

        # ==========================
        # MAIN FRAME
        # ==========================

        self.frame = tk.Frame(
            root,
            bg="#001f3f"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # TITLE
        # ==========================

        tk.Label(
            self.frame,
            text="🏦 TechFact Bank ATM",
            bg="#001f3f",
            fg="white",
            font=("Segoe UI", 28, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            self.frame,
            text="Select Your ATM Card",
            bg="#001f3f",
            fg="lightgray",
            font=("Segoe UI", 12)
        ).pack()

        # ==========================
        # CARD IMAGE
        # ==========================

        try:

            self.card_img = tk.PhotoImage(
                file="assets/images/atm_card.png"
            )

            tk.Label(
                self.frame,
                image=self.card_img,
                bg="#001f3f"
            ).pack(
                pady=15
            )

        except:

            tk.Label(
                self.frame,
                text="💳",
                bg="#001f3f",
                fg="gold",
                font=("Segoe UI", 90)
            ).pack(
                pady=15
            )

        # ==========================
        # USER LIST
        # ==========================

        self.user_map = {}

        card_options = []

        for user in self.users_data["users"]:

            text = (
                f"{user['name']} "
                f"({user['account']})"
            )

            self.user_map[text] = user

            card_options.append(text)

        self.selected_card = tk.StringVar()

        if card_options:

            self.selected_card.set(
                card_options[0]
            )

        ttk.Combobox(
            self.frame,
            textvariable=self.selected_card,
            values=card_options,
            width=35,
            state="readonly"
        ).pack(
            pady=10
        )

        # ==========================
        # STATUS
        # ==========================

        self.status_label = tk.Label(
            self.frame,
            text="Please Insert Your ATM Card",
            bg="#001f3f",
            fg="cyan",
            font=("Segoe UI", 13, "bold")
        )

        self.status_label.pack(
            pady=20
        )

        # ==========================
        # INSERT BUTTON
        # ==========================

        self.insert_btn = tk.Button(
            self.frame,
            text="💳 Insert Card",
            bg="#2ECC40",
            fg="white",
            width=20,
            height=2,
            font=("Segoe UI", 12, "bold"),
            command=self.insert_card
        )

        self.insert_btn.pack(
            pady=10
        )

        # ==========================
        # FOOTER
        # ==========================

        tk.Label(
            self.frame,
            text="Powered by TechFactOfficial • Developed by EngrAwais",
            bg="#001f3f",
            fg="gray",
            font=("Segoe UI", 10)
        ).pack(
            side="bottom",
            pady=20
        )

    # ==========================
    # INSERT CARD
    # ==========================

    def insert_card(self):

        sounds.card_insert()

        self.insert_btn.config(
            state="disabled"
        )

        self.status_label.config(
            text="Reading ATM Card..."
        )

        self.root.after(
            1500,
            self.open_login
        )

    # ==========================
    # OPEN LOGIN
    # ==========================

    def open_login(self):

        selected_user = self.user_map[
            self.selected_card.get()
        ]

        self.frame.destroy()

        self.continue_callback(
            selected_user
        )

