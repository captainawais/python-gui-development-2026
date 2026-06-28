# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from tkinter import ttk


# ==========================
# PROGRESS PANEL
# ==========================

class ProgressPanel:

    def __init__(self, parent):

        card = tk.Frame(
            parent,
            bg="white",
            bd=1,
            relief="solid",
            padx=20,
            pady=20
        )

        card.pack(
            side="right",
            fill="y",
            padx=(10,40),
            pady=30
        )

        tk.Label(
            card,
            text="Today's Progress",
            bg="white",
            fg="#111827",
            font=("Segoe UI",16,"bold")
        ).pack(pady=(0,20))

        self.add_item(card,"🔥 Current Streak","0 Days","#2563eb")
        self.add_item(card,"🏆 Best Streak","0 Days","#16a34a")
        self.add_item(card,"🎯 Today's Goal","0 / 10","#f59e0b")
        self.add_item(card,"✅ Completed","0","#22c55e")
        self.add_item(card,"❌ Pending","10","#ef4444")

        tk.Label(
            card,
            text="Overall Progress",
            bg="white",
            fg="#374151",
            font=("Segoe UI",11,"bold")
        ).pack(pady=(25,5))

        self.progress = ttk.Progressbar(
            card,
            orient="horizontal",
            length=220,
            mode="determinate"
        )

        self.progress["value"] = 0
        self.progress.pack()

        self.percent = tk.Label(
            card,
            text="0%",
            bg="white",
            fg="#2563eb",
            font=("Segoe UI",12,"bold")
        )

        self.percent.pack(pady=10)

    def add_item(self,parent,title,value,color):

        frame = tk.Frame(
            parent,
            bg="white"
        )

        frame.pack(
            fill="x",
            pady=8
        )

        tk.Label(
            frame,
            text=title,
            bg="white",
            anchor="w",
            font=("Segoe UI",10)
        ).pack(side="left")

        tk.Label(
            frame,
            text=value,
            bg="white",
            fg=color,
            font=("Segoe UI",10,"bold")
        ).pack(side="right")