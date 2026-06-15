from tkinter import simpledialog, messagebox
from utils.database import save_users, add_history
from components import sounds


def withdraw_money(user, users_data, update_balance):

    amount = simpledialog.askinteger(
        "Withdraw",
        "Enter Amount"
    )

    if not amount:
        return

    if amount > user["balance"]:

        sounds.error()

        messagebox.showerror(
            "Error",
            "Insufficient Balance"
        )

        return

    user["balance"] -= amount

    save_users(users_data)

    add_history(
        f"{user['name']} Withdraw PKR {amount}"
    )

    update_balance()

    sounds.withdraw()

    messagebox.showinfo(
        "Success",
        f"PKR {amount} Withdrawn"
    )