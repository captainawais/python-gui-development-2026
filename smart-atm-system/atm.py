import tkinter as tk
from tkinter import messagebox

from components.card_screen import CardScreen
from components.login import LoginScreen
from components.dashboard import Dashboard

from utils.database import load_users


# ==========================
# GLOBAL DATA
# ==========================

users_data = load_users()

current_user = None
attempts_left = 3


# ==========================
# SHOW CARD SCREEN
# ==========================

def show_card_screen():

    CardScreen(
        window,
        users_data,
        show_login_screen
    )


# ==========================
# SHOW LOGIN SCREEN
# ==========================

def show_login_screen(selected_user):

    global attempts_left

    attempts_left = 3

    LoginScreen(
        window,
        selected_user,
        login_handler
    )


# ==========================
# LOGIN HANDLER
# ==========================

def login_handler(
    selected_user,
    pin,
    attempts,
    login_frame,
    login_obj
):

    global current_user
    global attempts_left

    # Verify PIN

    if selected_user["pin"] == pin:

        current_user = selected_user

        try:
            login_frame.destroy()
        except:
            pass

        messagebox.showinfo(
            "Login Success",
            f"Welcome {selected_user['name']}"
        )

        Dashboard(
            window,
            current_user,
            users_data,
            logout_callback=show_card_screen
        )

        return

    # Wrong PIN

    attempts_left -= 1

    login_obj.attempts = attempts_left

    login_obj.update_attempts()

    if attempts_left > 0:

        messagebox.showerror(
            "Invalid PIN",
            f"Incorrect ATM PIN\n\nAttempts Left: {attempts_left}"
        )

    else:

        messagebox.showerror(
            "ATM Locked",
            "Too many failed attempts.\nATM is now locked."
        )

        window.destroy()


# ==========================
# MAIN WINDOW
# ==========================

window = tk.Tk()

window.title(
    "TechFact Bank ATM v3.0"
)

window.geometry(
    "900x850"
)

window.configure(
    bg="#001f3f"
)

window.resizable(
    False,
    False
)


# ==========================
# START CARD SCREEN
# ==========================

show_card_screen()


# ==========================
# FOOTER
# ==========================

footer = tk.Label(
    window,
    text="Powered by TechFactOfficial • Developed by EngrAwais",
    bg="#001f3f",
    fg="white",
    font=("Segoe UI", 10)
)

footer.pack(
    side="bottom",
    pady=10
)


# ==========================
# START APPLICATION
# ==========================

window.mainloop()