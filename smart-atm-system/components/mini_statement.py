from tkinter import messagebox

from utils.database import get_history

def mini_statement(user):


    history = get_history(user)

    if not history:

        messagebox.showinfo(
            "Mini Statement",
            "No Transactions Found"
        )

        return

    recent = history[-5:]

    statement = "\n".join(recent)

    messagebox.showinfo(
        "Mini Statement",
        f"Last {len(recent)} Transactions\n\n{statement}"
    )

