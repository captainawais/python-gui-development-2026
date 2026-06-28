# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from components.sidebar import Sidebar
from components.habit_table import HabitTable
from components.statistics import Statistics
from components.progress_panel import ProgressPanel
from components.calendar import CalendarView
from components.footer import Footer


# ==========================
# DASHBOARD CLASS
# ==========================

class Dashboard:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, root):

        self.root = root

        self.main_frame = tk.Frame(
            root,
            bg="#0F172A"
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.create_layout()


        # ==========================
        # CREATE LAYOUT
        # ==========================

    def create_layout(self):

        # ==========================
        # SIDEBAR
        # ==========================

        Sidebar(
            self.main_frame
        )

        # ==========================
        # CONTENT
        # ==========================

        content = tk.Frame(
            self.main_frame,
            bg="#F8FAFC"
        )

        content.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ==========================
        # SCROLLABLE CANVAS
        # ==========================

        canvas = tk.Canvas(
            content,
            bg="#F8FAFC",
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            content,
            orient="vertical",
            command=canvas.yview
        )

        scroll_frame = tk.Frame(
            canvas,
            bg="#F8FAFC"
        )

        scroll_frame.bind(

            "<Configure>",

            lambda e: canvas.configure(

                scrollregion=canvas.bbox("all")

            )

        )

        canvas.create_window(

            (0,0),

            window=scroll_frame,

            anchor="nw"

        )

        canvas.configure(

            yscrollcommand=scrollbar.set

        )

        canvas.pack(

            side="left",

            fill="both",

            expand=True

        )

        scrollbar.pack(

            side="right",

            fill="y"

        )

        # Mouse Wheel Scroll

        canvas.bind_all(

            "<MouseWheel>",

            lambda event:

            canvas.yview_scroll(

                int(-1*(event.delta/120)),

                "units"

            )

        )

        # ==========================
        # HEADER
        # ==========================

        tk.Label(

            scroll_frame,

            text="TechFact Habit Track",

            font=("Segoe UI",28,"bold"),

            bg="#F8FAFC",

            fg="#111827"

        ).pack(
            pady=(30,5)
        )

        tk.Label(

            scroll_frame,

            text="Build Better Habits Every Day 🚀",

            font=("Segoe UI",13),

            bg="#F8FAFC",

            fg="gray"

        ).pack(
            pady=(0,20)
        )

        # ==========================
        # COMPONENTS
        # ==========================

        HabitTable(
            scroll_frame
        )

        Statistics(
            scroll_frame
        )

        ProgressPanel(
            scroll_frame
        )

        CalendarView(
            scroll_frame
        )

        Footer(
            scroll_frame
        )