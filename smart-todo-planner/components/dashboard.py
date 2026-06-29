# ==========================
# IMPORTS
# ==========================
import tkinter as tk

from components.sidebar import Sidebar

from components.pages.dashboard_page import DashboardPage
from components.pages.habits_page import HabitsPage
from components.pages.calendar_page import CalendarPage
from components.pages.statistics_page import StatisticsPage
from components.pages.streak_page import StreakPage
from components.pages.settings_page import SettingsPage
from components.pages.about_page import AboutPage
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

        self.main_frame = tk.Frame(root, bg="#0F172A")

        self.main_frame.pack(fill="both", expand=True)

        self.create_layout()

        # ==========================
        # CREATE LAYOUT
        # ==========================

    def create_layout(self):

        # ==========================
        # SIDEBAR
        # ==========================

        Sidebar(self.main_frame, self)

        self.content = tk.Frame(self.main_frame, bg="#F8FAFC")

        self.content.pack(side="left", fill="both", expand=True)

        # ==========================
        # SCROLLABLE AREA
        # ==========================

        canvas = tk.Canvas(self.content, bg="#F8FAFC", highlightthickness=0)

        scrollbar = tk.Scrollbar(self.content, orient="vertical", command=canvas.yview)

        self.scroll_frame = tk.Frame(canvas, bg="#F8FAFC")

        self.scroll_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        window = canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(window, width=e.width))

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)

        scrollbar.pack(side="right", fill="y")

        canvas.bind(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"),
        )

        self.show_dashboard()

    # ==========================
    # CLEAR PAGE
    # ==========================

    def clear_page(self):

        for widget in self.scroll_frame.winfo_children():

            widget.destroy()

    # ==========================
    # DASHBOARD
    # ==========================

    def show_dashboard(self):

        self.clear_page()

        DashboardPage(self.scroll_frame)
        
        Footer(self.scroll_frame)

    # ==========================
    # HABITS
    # ==========================

    def show_habits(self):

        self.clear_page()

        HabitsPage(self.scroll_frame)
        
   

    # ==========================
    # CALENDAR
    # ==========================

    def show_calendar(self):

        self.clear_page()

        CalendarPage(self.scroll_frame)

    # ==========================
    # STATISTICS
    # ==========================

    def show_statistics(self):

        self.clear_page()

        StatisticsPage(self.scroll_frame)

  

    # ==========================
    # STREAK
    # ==========================

    def show_streaks(self):

        self.clear_page()

        StreakPage(self.scroll_frame)



    # ==========================
    # SETTINGS
    # ==========================

    def show_settings(self):

        self.clear_page()

        SettingsPage(self.scroll_frame)



    # ==========================
    # ABOUT
    # ==========================

    def show_about(self):

        self.clear_page()

        AboutPage(self.scroll_frame)
       

