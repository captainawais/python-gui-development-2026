from tkinter import messagebox
from utils.database import load_history


def show_history():

    history = load_history()

    if not history:

        messagebox.showinfo(
            "History",
            "No Transactions Found"
        )

        return

    messagebox.showinfo(
        "History",
        "\n".join(history)
    )