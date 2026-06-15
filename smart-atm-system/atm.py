import tkinter as tk
from tkinter import messagebox

from components.login import LoginScreen
from components.dashboard import Dashboard

from utils.database import load_users

users_data = load_users()
current_user = None

# Global attempts counter
attempts_left = 3


def login_handler(
    pin,
    attempts,
    login_frame
):
    global current_user
    global attempts_left

    # Check PIN
    for user in users_data["users"]:

        if user["pin"] == pin:

            current_user = user

            messagebox.showinfo(
                "Login Success",
                f"Welcome {user['name']}"
            )

            login_frame.destroy()

            Dashboard(
                window,
                current_user,
                users_data
            )

            return

    # Wrong PIN
    attempts_left -= 1

    if attempts_left > 0:

        messagebox.showerror(
            "Invalid PIN",
            f"Wrong PIN!\nAttempts Left: {attempts_left}"
        )

    else:

        messagebox.showerror(
            "ATM Locked",
            "Too many failed attempts.\nATM is now locked."
        )

        window.destroy()


window = tk.Tk()

window.title("TechFact Bank ATM v2.0")

window.geometry("800x600")

window.configure(bg="#001f3f")

LoginScreen(
    window,
    login_handler
)

footer = tk.Label(
    window,
    text="Powered by TechFactOfficial • Developed by EngrAwais",
    bg="#001f3f",
    fg="white"
)

footer.pack(
    side="bottom",
    pady=10
)

window.mainloop()