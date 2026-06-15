from tkinter import simpledialog, messagebox
from utils.database import save_users, add_history
from components import sounds


def deposit_money(user, users_data, update_balance):

    amount = simpledialog.askinteger(
        "Deposit",
        "Enter Deposit Amount"
    )

    if not amount:
        return

    user["balance"] += amount

    save_users(users_data)

    add_history(
        f"{user['name']} Deposited PKR {amount}"
    )

    update_balance()

    sounds.deposit()

    messagebox.showinfo(
        "Success",
        f"PKR {amount} Deposited"
    )