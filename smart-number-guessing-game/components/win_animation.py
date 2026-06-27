import tkinter as tk

class WinAnimation:

    def __init__(self, root):

        self.label = tk.Label(
            root,
            text="🎉🎉🎉",
            bg="#0f172a",
            fg="#facc15",
            font=("Segoe UI",40)
        )

        self.label.place(
            relx=0.5,
            rely=0.15,
            anchor="center"
        )

        root.after(
            1800,
            self.label.destroy
        )