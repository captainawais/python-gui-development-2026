# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from datetime import datetime

from components.deposit import deposit_money
from components.withdraw import withdraw_money
from components.transfer import transfer_money

from components.history import show_history
from components.mini_statement import mini_statement
from components.change_pin import change_pin

from components.fast_cash import fast_cash
from components import sounds

from utils.database import get_last_transaction



# ==========================
# DASHBOARD CLASS
# ==========================

class Dashboard:


# ==========================
# INIT
# ==========================

    def __init__(
        self,
        root,
        user,
        users_data,
        logout_callback=None
    ):

        self.root = root
        self.user = user
        self.users_data = users_data
        self.logout_callback = logout_callback

        # Main Frame

        self.frame = tk.Frame(
            root,
            bg="#f4f6f8"
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # Build Dashboard

        self.create_header()

        self.create_balance_card()

        self.create_last_transaction()

        self.create_fast_cash()

        self.create_action_buttons()



    # ==========================
    # HEADER SECTION
    # ==========================

    def create_header(self):

        self.header = tk.Frame(
            self.frame,
            bg="#001f3f",
            height=90
        )

        self.header.pack(
            fill="x"
        )

        tk.Label(
            self.header,
            text="🏦 TechFact Bank ATM",
            bg="#001f3f",
            fg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(10, 0)
        )

        tk.Label(
            self.header,
            text="Secure Banking System",
            bg="#001f3f",
            fg="lightgray",
            font=("Segoe UI", 10)
        ).pack()
    
    
    
        self.time_label = tk.Label(
        self.header,
         text="",
            bg="#001f3f",
            fg="lightgray",
            font=("Segoe UI", 9)
        )

        self.time_label.pack(
          pady=(2, 5)
            )

        self.update_time()    
        
        
    # ==========================
    # LAST TRANSACTION
    # ==========================

    def create_last_transaction(self):

        self.transaction_frame = tk.Frame(
            self.frame,
            bg="white",
            padx=15,
            pady=10
        )

        self.transaction_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        tk.Label(
            self.transaction_frame,
            text="Last Transaction",
            bg="white",
            fg="#001f3f",
            font=("Segoe UI", 11, "bold")
        ).pack(
            anchor="w"
        )

        self.last_txn_label = tk.Label(
            self.transaction_frame,
            text="No Transaction",
            bg="white",
            fg="gray",
            font=("Segoe UI", 10)
        )

        self.last_txn_label.pack(
            anchor="w",
            pady=(5, 0)
        )

        self.update_last_transaction()
        
        # ==========================

        # UPDATE LAST TRANSACTION

        # ==========================

    def update_last_transaction(self):


        self.last_txn_label.config(
            text=get_last_transaction(
                self.user
            )
        )

        

    # ==========================
    # BALANCE CARD
    # ==========================

    def create_balance_card(self):

        self.balance_card = tk.Frame(
            self.frame,
            bg="#2ECC40",
            padx=25,
            pady=25
        )

        self.balance_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Card Title

        tk.Label(
            self.balance_card,
            text="Available Balance",
            bg="#2ECC40",
            fg="white",
            font=("Segoe UI", 12)
        ).pack()

        # Balance Amount

        self.balance_label = tk.Label(
            self.balance_card,
            text="PKR 0",
            bg="#2ECC40",
            fg="white",
            font=("Segoe UI", 28, "bold")
        )

        self.balance_label.pack(
            pady=5
        )

        # Account Status

        tk.Label(
            self.balance_card,
            text="Account Status : Active",
            bg="#2ECC40",
            fg="white",
            font=("Segoe UI", 10)
        ).pack()

        # Load Current Balance

        self.update_balance()


    # ==========================
    # FAST CASH
    # ==========================

    def create_fast_cash(self):

        self.fast_cash_frame = tk.LabelFrame(
            self.frame,
            text="Fast Cash",
            bg="#f4f6f8",
            font=("Segoe UI", 11, "bold")
        )

        self.fast_cash_frame.pack(
            pady=10
        )

        for amount in [500, 1000, 2000, 5000, 10000]:

            tk.Button(
                self.fast_cash_frame,
                text=f"PKR {amount}",
                width=10,
                command=lambda amt=amount:
                fast_cash(
                    self.root,
                    self.user,
                    self.users_data,
                    self.update_balance,
                    amt
                )
            ).pack(
                side="left",
                padx=5,
                pady=5
            )

    # ==========================
    # ACTION BUTTONS
    # ==========================

    def create_action_buttons(self):

        self.btn_frame = tk.Frame(
            self.frame,
            bg="#f4f6f8"
        )

        self.btn_frame.pack(
            pady=40
        )

        # Deposit

        tk.Button(
            self.btn_frame,
            text="💰 Deposit",
            width=20,
            height=2,
            bg="#2ECC40",
            fg="white",
            command=lambda:
            deposit_money(
                self.root,
                self.user,
                self.users_data,
                self.update_balance
            )
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        # Withdraw

        tk.Button(
            self.btn_frame,
            text="💸 Withdraw",
            width=20,
            height=2,
            bg="#E74C3C",
            fg="white",
            command=lambda:
            withdraw_money(
                self.root,
                self.user,
                self.users_data,
                self.update_balance
            )
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Transfer

        tk.Button(
            self.btn_frame,
            text="🔄 Transfer",
            width=20,
            height=2,
            bg="#F39C12",
            fg="white",
            command=lambda:
            transfer_money(
                self.root,
                self.user,
                self.users_data,
                self.update_balance
            )
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        # History

        tk.Button(
            self.btn_frame,
            text="📜 History",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            command=lambda:
            show_history(
                self.user
            )
        ).grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # Change PIN

        tk.Button(
            self.btn_frame,
            text="🔐 Change PIN",
            width=20,
            height=2,
            bg="#9B59B6",
            fg="white",
            command=lambda:
            change_pin(
                self.user,
                self.users_data
            )
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        # Mini Statement

        tk.Button(
            self.btn_frame,
            text="🧾 Mini Statement",
            width=20,
            height=2,
            bg="#16A085",
            fg="white",
            command=lambda:
            mini_statement(
                self.user
            )
        ).grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # Exit ATM

        tk.Button(
            self.frame,
            text="🚪 Exit ATM",
            bg="black",
            fg="white",
            width=25,
            height=2,
            command=self.exit_atm
        ).pack(
            pady=15
        )

    # ==========================
    # UPDATE BALANCE
    # ==========================

    def update_balance(self):

        self.balance_label.config(
            text=f"PKR {self.user['balance']:,}"
        )

        if hasattr(
            self,
            "last_txn_label"
        ):

            self.update_last_transaction()

    # ==========================
    # UPDATE CLOCK
    # ==========================

    def update_time(self):

        now = datetime.now()

        self.time_label.config(
            text=now.strftime(
                "%d-%b-%Y  %I:%M:%S %p"
            )
        )

        self.root.after(
            1000,
            self.update_time
        )

    # ==========================
    # EXIT ATM
    # ==========================

    def exit_atm(self):

        sounds.card_eject()

        popup = tk.Toplevel(
            self.root
        )

        popup.title(
            "TechFact Bank ATM"
        )

        popup.geometry(
            "400x250"
        )

        popup.configure(
            bg="white"
        )

        popup.grab_set()

        tk.Label(
            popup,
            text="🏦",
            bg="white",
            font=("Segoe UI", 40)
        ).pack(
            pady=(20, 10)
        )

        tk.Label(
            popup,
            text="Thank You For Using",
            bg="white",
            fg="#001f3f",
            font=("Segoe UI", 16, "bold")
        ).pack()

        tk.Label(
            popup,
            text="TechFact Bank ATM",
            bg="white",
            fg="#2ECC40",
            font=("Segoe UI", 14)
        ).pack(
            pady=5
        )

        tk.Label(
            popup,
            text="Please Take Your Card",
            bg="white",
            fg="gray",
            font=("Segoe UI", 11)
        ).pack(
            pady=10
        )

# ==========================
# RETURN TO LOGIN
# ==========================

        def return_to_login():

            popup.destroy()

            self.frame.destroy()

            if self.logout_callback:

                self.logout_callback()

        popup.after(
            3000,
            return_to_login
        )