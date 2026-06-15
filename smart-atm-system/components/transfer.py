from tkinter import simpledialog, messagebox
from utils.database import save_users, add_history
from components import sounds


def transfer_money(user, users_data, update_balance):

    account = simpledialog.askstring(
        "Transfer",
        "Enter Account Number"
    )

    if not account:
        return

    amount = simpledialog.askinteger(
        "Transfer",
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

    for target_user in users_data["users"]:

        if target_user["account"] == account:

            user["balance"] -= amount

            target_user["balance"] += amount

            save_users(users_data)

            add_history(
                f"{user['name']} Transfer PKR {amount} to {account}"
            )

            sounds.transfer()

            update_balance()

            messagebox.showinfo(
                "Success",
                f"Transferred PKR {amount}"
            )

            return

    sounds.error()

    messagebox.showerror(
        "Error",
        "Account Not Found"
    )
