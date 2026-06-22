from tkinter import simpledialog
from tkinter import messagebox

from utils.database import (
    save_users,
    add_history
)

from components import sounds


def change_pin(
    user,
    users_data
):

    # ==========================
    # CURRENT PIN
    # ==========================

    old_pin = simpledialog.askstring(
        "Change PIN",
        "Enter Current PIN",
        show="*"
    )

    if not old_pin:
        return

    if old_pin != user["pin"]:

        sounds.error()

        messagebox.showerror(
            "Invalid PIN",
            "Incorrect Current PIN"
        )

        return

    # ==========================
    # NEW PIN
    # ==========================

    new_pin = simpledialog.askstring(
        "Change PIN",
        "Enter New PIN",
        show="*"
    )

    if not new_pin:
        return

    if not new_pin.isdigit():

        sounds.error()

        messagebox.showerror(
            "Invalid PIN",
            "PIN must contain digits only."
        )

        return

    if len(new_pin) != 4:

        sounds.error()

        messagebox.showerror(
            "Invalid PIN",
            "PIN must be exactly 4 digits."
        )

        return

    if new_pin == user["pin"]:

        sounds.error()

        messagebox.showerror(
            "Invalid PIN",
            "New PIN cannot be same as old PIN."
        )

        return

    # ==========================
    # CONFIRM PIN
    # ==========================

    confirm_pin = simpledialog.askstring(
        "Change PIN",
        "Confirm New PIN",
        show="*"
    )

    if not confirm_pin:
        return

    if new_pin != confirm_pin:

        sounds.error()

        messagebox.showerror(
            "PIN Mismatch",
            "PIN confirmation does not match."
        )

        return

    # ==========================
    # UPDATE PIN
    # ==========================

    user["pin"] = new_pin

    add_history(
        user,
        "Security: ATM PIN Changed"
    )

    save_users(
        users_data
    )

    sounds.success()

    messagebox.showinfo(
        "Success",
        "ATM PIN changed successfully."
    )