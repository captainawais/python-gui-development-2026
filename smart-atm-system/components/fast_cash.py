from tkinter import messagebox

from utils.database import (
    save_users,
    add_history
)

from components import sounds
from components.loading import LoadingScreen


# ==========================
# FAST CASH
# ==========================

def fast_cash(
    root,
    user,
    users_data,
    update_balance,
    amount
):

    # ==========================
    # BALANCE CHECK
    # ==========================

    if amount > user["balance"]:

        sounds.error()

        messagebox.showerror(
            "Insufficient Balance",
            f"You do not have PKR {amount:,} available."
        )

        return

    # ==========================
    # PROCESSING SOUND
    # ==========================

    sounds.loading()

    # ==========================
    # LOADING SCREEN
    # ==========================

    loading = LoadingScreen(
        root,
        f"Dispensing PKR {amount:,}..."
    )

    # ==========================
    # COMPLETE WITHDRAW
    # ==========================

    def finish_fast_cash():

        user["balance"] -= amount

        add_history(
            user,
            f"Fast Cash -PKR {amount}"
        )

        save_users(
            users_data
        )

        update_balance()

        loading.close()

        sounds.stop_sound()

        sounds.success()

        messagebox.showinfo(
            "Cash Dispensed",
            f"Please collect your cash.\n\nPKR {amount:,}"
        )

    # ==========================
    # ATM DELAY
    # ==========================

    root.after(
        2500,
        finish_fast_cash
    )