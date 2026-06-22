from tkinter import simpledialog
from tkinter import messagebox

from utils.database import (
    save_users,
    add_history
)

from components import sounds
from components.loading import LoadingScreen


def deposit_money(
    root,
    user,
    users_data,
    update_balance
):

    # ==========================
    # ASK AMOUNT
    # ==========================

    amount = simpledialog.askinteger(
        "TechFact Bank",
        "Enter Deposit Amount"
    )

    if amount is None:
        return

    if amount <= 0:

        sounds.error()

        messagebox.showerror(
            "Invalid Amount",
            "Please enter a valid amount."
        )

        return

    # ==========================
    # LOADING SCREEN
    # ==========================

    sounds.loading()

    loading = LoadingScreen(
        root,
        "Processing Deposit..."
    )

    # ==========================
    # COMPLETE DEPOSIT
    # ==========================

    def finish_deposit():

        user["balance"] += amount

        add_history(
            user,
            f"Deposit +PKR {amount}"
        )

        save_users(
            users_data
        )

        update_balance()

        loading.close()

        sounds.stop_sound()
        sounds.success()

        messagebox.showinfo(
            "Deposit Successful",
            f"PKR {amount:,} deposited successfully."
        )

    # ==========================
    # ATM PROCESSING DELAY
    # ==========================

    root.after(
        2500,
        finish_deposit
    )