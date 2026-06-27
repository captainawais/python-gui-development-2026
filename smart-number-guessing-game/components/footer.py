import tkinter as tk

class Footer:

    def __init__(self,parent):

        tk.Label(

            parent,

            text="Smart Number Guessing Game • Version 2.0",

            bg="#0f172a",

            fg="gray",

            font=("Segoe UI",9)

        ).pack(
            side="bottom",
            pady=8
        )