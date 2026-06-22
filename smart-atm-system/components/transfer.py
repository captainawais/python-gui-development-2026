from tkinter import simpledialog
from tkinter import messagebox

from utils.database import (
    save_users,
    add_history
)

from components import sounds
from components.loading import LoadingScreen


def transfer_money(
    root,
    user,
    users_data,
    update_balance
):

    # ==========================
    # ACCOUNT NUMBER
    # ==========================

    account = simpledialog.askstring(
        "Transfer Money",
        "Enter Receiver Account Number"
    )

    if not account:
        return

    # ==========================
    # AMOUNT
    # ==========================

    amount = simpledialog.askinteger(
        "Transfer Money",
        "Enter Transfer Amount"
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
    # SELF TRANSFER BLOCK
    # ==========================

    if account == user["account"]:

        sounds.error()

        messagebox.showerror(
            "Transfer Error",
            "You cannot transfer money to your own account."
        )

        return

    # ==========================
    # BALANCE CHECK
    # ==========================

    if amount > user["balance"]:

        sounds.error()

        messagebox.showerror(
            "Insufficient Balance",
            "Not enough balance available."
        )

        return

    # ==========================
    # FIND RECEIVER
    # ==========================

    receiver = None

    for target_user in users_data["users"]:

        if target_user["account"] == account:

            receiver = target_user
            break

    if receiver is None:

        sounds.error()

        messagebox.showerror(
            "Account Not Found",
            "Receiver account does not exist."
        )

        return

    # ==========================
    # PROCESSING
    # ==========================

    sounds.loading()

    loading = LoadingScreen(
        root,
        "Transferring Funds..."
    )

    # ==========================
    # COMPLETE TRANSFER
    # ==========================

    def finish_transfer():

        user["balance"] -= amount

        receiver["balance"] += amount

        # Sender History

        add_history(
            user,
            f"Transfer -PKR {amount} To {receiver['account']}"
        )

        # Receiver History

        add_history(
            receiver,
            f"Received +PKR {amount} From {user['account']}"
        )

        save_users(
            users_data
        )

        loading.close()

        update_balance()

        sounds.stop_sound()
        sounds.success()

        messagebox.showinfo(
            "Transfer Successful",
            f"PKR {amount:,} transferred successfully.\n\nReceiver: {receiver['name']}"
        )

    root.after(
        2500,
        finish_transfer
    )