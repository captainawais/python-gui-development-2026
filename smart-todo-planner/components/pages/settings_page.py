# ==========================
# IMPORTS
# ==========================

import tkinter as tk
from tkinter import messagebox
from utils.settings import Settings
from utils.storage import Storage


# ==========================
# SETTINGS PAGE
# ==========================


class SettingsPage:

    # ==========================
    # INIT
    # ==========================

    def __init__(self, parent):

        self.parent = parent

        # ==========================
        # PAGE TITLE
        # ==========================

        tk.Label(
            parent,
            text="Settings",
            bg="#F8FAFC",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(pady=(30, 5))

        tk.Label(
            parent,
            text="Manage your application settings ⚙️",
            bg="#F8FAFC",
            fg="gray",
            font=("Segoe UI", 12),
        ).pack(pady=(0, 25))

        # ==========================
        # SETTINGS CARD
        # ==========================

        card = tk.Frame(parent, bg="white", bd=1, relief="solid")

        card.pack(fill="x", padx=30, pady=20)

        tk.Label(
            card,
            text="Application Settings",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=20, pady=(20, 20))

        # Auto Save

        self.auto_save = tk.BooleanVar(value=True)

        tk.Checkbutton(
            card,
            text="Enable Auto Save",
            variable=self.auto_save,
            bg="white",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=25, pady=5)

        # Notifications

        self.notifications = tk.BooleanVar(value=True)

        tk.Checkbutton(
            card,
            text="Enable Notifications",
            variable=self.notifications,
            bg="white",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=25, pady=5)

        # Dark Mode

        self.dark_mode = tk.BooleanVar(value=False)

        tk.Checkbutton(
            card,
            text="Dark Mode (Coming Soon)",
            variable=self.dark_mode,
            bg="white",
            state="disabled",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=25, pady=5)

        # Sync

        self.sync = tk.BooleanVar(value=False)

        tk.Checkbutton(
            card,
            text="Cloud Sync (Coming Soon)",
            variable=self.sync,
            bg="white",
            state="disabled",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=25, pady=5)

        # ==========================
        # BUTTONS
        # ==========================

        button_frame = tk.Frame(card, bg="white")

        button_frame.pack(pady=25)

        tk.Button(
            button_frame,
            text="💾 Save Settings",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=18,
            relief="flat",
            cursor="hand2",
            command=self.save_settings,
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="🗑 Reset All Data",
            bg="#DC2626",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=18,
            relief="flat",
            cursor="hand2",
            command=self.reset_data,
        ).pack(side="left", padx=10)

    # ==========================
    # SAVE SETTINGS
    # ==========================

    def save_settings(self):

        settings = {
            "auto_save": self.auto_save.get(),
            "notifications": self.notifications.get(),
            "dark_mode": self.dark_mode.get(),
            "cloud_sync": self.sync.get()
        }

        Settings.save(settings)

        messagebox.showinfo("Settings", "Settings saved successfully.")

    # ==========================
    # RESET DATA
    # ==========================

    def reset_data(self):

        confirm = messagebox.askyesno(
            "Reset", "Are you sure you want to delete all habit data?"
        )

        if not confirm:

            return

        Storage.reset()

        messagebox.showinfo("Success", "All habit data has been reset.")
        
        