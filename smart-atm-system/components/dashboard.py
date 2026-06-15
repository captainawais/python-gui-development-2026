import tkinter as tk

from components.deposit import deposit_money
from components.withdraw import withdraw_money
from components.transfer import transfer_money
from components.history import show_history


class Dashboard:

    def __init__(
        self,
        root,
        user,
        users_data
    ):

        self.root = root
        self.user = user
        self.users_data = users_data

        self.frame = tk.Frame(
            root,
            bg="white",
            padx=30,
            pady=30
        )

        self.frame.pack(expand=True)

        tk.Label(
            self.frame,
            text=f"Welcome {user['name']}",
            bg="white",
            font=("Segoe UI", 18, "bold")
        ).pack()

        tk.Label(
            self.frame,
            text="Current Balance",
            bg="white",
            font=("Segoe UI", 14)
        ).pack()

        self.balance_label = tk.Label(
            self.frame,
            text="PKR 0",
            bg="white",
            fg="green",
            font=("Segoe UI", 22, "bold")
        )

        self.balance_label.pack(pady=10)

        self.update_balance()

        tk.Button(
            self.frame,
            text="💰 Deposit",
            width=20,
            command=lambda:
            deposit_money(
                self.user,
                self.users_data,
                self.update_balance
            )
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="💸 Withdraw",
            width=20,
            command=lambda:
            withdraw_money(
                self.user,
                self.users_data,
                self.update_balance
            )
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="🔄 Transfer",
            width=20,
            command=lambda:
            transfer_money(
                self.user,
                self.users_data,
                self.update_balance
            )
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="📜 History",
            width=20,
            command=show_history
        ).pack(pady=5)

    def update_balance(self):

        self.balance_label.config(
            text=f"PKR {self.user['balance']}"
        )