import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# ==========================
# DATA FILES
# ==========================

USER_FILE = "data/users.json"
HISTORY_FILE = "data/history.json"

# ==========================
# LOAD USER DATA
# ==========================

with open(USER_FILE, "r") as file:
    user = json.load(file)

# ==========================
# SAVE FUNCTIONS
# ==========================

def save_user():
    with open(USER_FILE, "w") as file:
        json.dump(user, file, indent=4)

def add_history(text):
    try:
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    except:
        history = []

    history.append(text)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

# ==========================
# LOGIN FUNCTION
# ==========================

def login():
    entered_pin = pin_entry.get()

    if entered_pin == user["pin"]:
        login_frame.pack_forget()
        dashboard_frame.pack(expand=True)
        update_balance()

    else:
        messagebox.showerror(
            "Access Denied",
            "Incorrect ATM PIN!"
        )

# ==========================
# BALANCE UPDATE
# ==========================

def update_balance():
    balance_label.config(
        text=f"PKR {user['balance']}"
    )

# ==========================
# DEPOSIT
# ==========================

def deposit():

    amount = simpledialog.askinteger(
        "Deposit",
        "Enter amount:"
    )

    if amount and amount > 0:

        user["balance"] += amount

        save_user()

        add_history(
            f"Deposit: +PKR {amount}"
        )

        update_balance()

        messagebox.showinfo(
            "Success",
            f"PKR {amount} deposited."
        )

# ==========================
# WITHDRAW
# ==========================

def withdraw():

    amount = simpledialog.askinteger(
        "Withdraw",
        "Enter amount:"
    )

    if amount and amount > 0:

        if amount > user["balance"]:

            messagebox.showerror(
                "Error",
                "Insufficient Balance!"
            )

            return

        user["balance"] -= amount

        save_user()

        add_history(
            f"Withdraw: -PKR {amount}"
        )

        update_balance()

        messagebox.showinfo(
            "Success",
            f"PKR {amount} withdrawn."
        )

# ==========================
# HISTORY
# ==========================

def show_history():

    try:
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    except:
        history = []

    history_text = "\n".join(history)

    if not history_text:
        history_text = "No transactions yet."

    messagebox.showinfo(
        "Transaction History",
        history_text
    )

# ==========================
# WINDOW
# ==========================

window = tk.Tk()

window.title("TechFact Bank ATM")
window.geometry("600x650")
window.configure(bg="#001f3f")
window.resizable(False, False)

# ==========================
# TITLE
# ==========================

title = tk.Label(
    window,
    text="🏦 TechFact Bank",
    bg="#001f3f",
    fg="white",
    font=("Segoe UI", 24, "bold")
)

title.pack(pady=20)

# ==========================
# LOGIN FRAME
# ==========================

login_frame = tk.Frame(
    window,
    bg="white",
    padx=30,
    pady=30
)

login_frame.pack(pady=60)

tk.Label(
    login_frame,
    text="ATM Login",
    bg="white",
    font=("Segoe UI", 18, "bold")
).pack(pady=10)

pin_entry = tk.Entry(
    login_frame,
    show="*",
    font=("Segoe UI", 16),
    justify="center"
)

pin_entry.pack(pady=15)

tk.Button(
    login_frame,
    text="Login",
    command=login,
    bg="#0074D9",
    fg="white",
    width=15,
    height=2,
    font=("Segoe UI", 12, "bold"),
    border=0
).pack()

# ==========================
# DASHBOARD
# ==========================

dashboard_frame = tk.Frame(
    window,
    bg="white",
    padx=30,
    pady=30
)

balance_title = tk.Label(
    dashboard_frame,
    text="Current Balance",
    bg="white",
    font=("Segoe UI", 16)
)

balance_title.pack()

balance_label = tk.Label(
    dashboard_frame,
    text="PKR 0",
    bg="white",
    fg="green",
    font=("Segoe UI", 24, "bold")
)

balance_label.pack(pady=10)

tk.Button(
    dashboard_frame,
    text="💰 Deposit",
    command=deposit,
    width=20,
    bg="#2ECC40",
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=8)

tk.Button(
    dashboard_frame,
    text="💸 Withdraw",
    command=withdraw,
    width=20,
    bg="#FF4136",
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=8)

tk.Button(
    dashboard_frame,
    text="📜 History",
    command=show_history,
    width=20,
    bg="#0074D9",
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=8)

tk.Button(
    dashboard_frame,
    text="❌ Exit",
    command=window.destroy,
    width=20,
    bg="black",
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=8)

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

footer.pack(side="bottom", pady=10)

window.mainloop()