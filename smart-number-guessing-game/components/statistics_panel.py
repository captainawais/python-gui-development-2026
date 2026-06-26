# ==========================
# IMPORTS
# ==========================

import tkinter as tk

from utils.storage import Storage

# ==========================
# STATISTICS PANEL
# ==========================

class StatisticsPanel:

    # ==========================
    # INIT
    # ==========================

    def __init__(
        self,
        parent
    ):

        self.parent = parent
        self.window = tk.Toplevel(parent)

        self.window.title("Player Statistics")

        self.window.geometry("500x650")

        self.window.configure(bg="#1e293b")

        self.window.resizable(False, False)

        self.storage = Storage()

        self.create_panel()


    # ==========================
    # CREATE PANEL
    # ==========================

    def create_panel(self):

        data = self.storage.load_stats()

        frame = tk.Frame(
            self.window,
            bg="#1e293b",
            bd=1,
            relief="solid"
        )

        frame.pack(
            pady=20,
            padx=20,
            fill="x"
        )

        # Title

        tk.Label(
            frame,
            text="📊 PLAYER STATISTICS",
            bg="#1e293b",
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(
            pady=(10,15)
        )

        # Games

        tk.Label(
            frame,
            text=f"🎮 Games Played : {data['games_played']}",
            bg="#1e293b",
            fg="white",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        tk.Label(
            frame,
            text=f"🏆 Games Won : {data['games_won']}",
            bg="#1e293b",
            fg="#22c55e",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        tk.Label(
            frame,
            text=f"❌ Games Lost : {data['games_lost']}",
            bg="#1e293b",
            fg="#ef4444",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        # Win Rate

        if data["games_played"] == 0:

            rate = 0

        else:

            rate = round(
                (
                    data["games_won"] /
                    data["games_played"]
                ) * 100
            )

        tk.Label(
            frame,
            text=f"📈 Win Rate : {rate}%",
            bg="#1e293b",
            fg="#38bdf8",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20, pady=(5,0))

        # Divider

        tk.Frame(
            frame,
            bg="#334155",
            height=2
        ).pack(
            fill="x",
            padx=15,
            pady=12
        )

        # Streak

        tk.Label(
            frame,
            text=f"🔥 Current Streak : {data['current_streak']}",
            bg="#1e293b",
            fg="#22c55e",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        tk.Label(
            frame,
            text=f"👑 Best Streak : {data['best_streak']}",
            bg="#1e293b",
            fg="#facc15",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        # Divider

        tk.Frame(
            frame,
            bg="#334155",
            height=2
        ).pack(
            fill="x",
            padx=15,
            pady=12
        )

        # XP & Level

        tk.Label(
            frame,
            text=f"⭐ Level : {data['level']}",
            bg="#1e293b",
            fg="#38bdf8",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        tk.Label(
            frame,
            text=f"💎 XP : {data['xp']}",
            bg="#1e293b",
            fg="#22c55e",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        # Divider

        tk.Frame(
            frame,
            bg="#334155",
            height=2
        ).pack(
            fill="x",
            padx=15,
            pady=12
        )

        # High Scores

        tk.Label(
            frame,
            text=f"🥇 Easy : {data['easy_high_score']}",
            bg="#1e293b",
            fg="white",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        tk.Label(
            frame,
            text=f"🥈 Medium : {data['medium_high_score']}",
            bg="#1e293b",
            fg="white",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20)

        tk.Label(
            frame,
            text=f"🥉 Hard : {data['hard_high_score']}",
            bg="#1e293b",
            fg="white",
            anchor="w",
            font=("Segoe UI",11)
        ).pack(fill="x", padx=20, pady=(0,15))