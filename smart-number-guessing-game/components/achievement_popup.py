# ==========================
# IMPORTS
# ==========================

import tkinter as tk


# ==========================
# ACHIEVEMENT POPUP
# ==========================

class AchievementPopup:

    # ==========================
    # INIT
    # ==========================

    def __init__(
        self,
        root,
        achievement
    ):

        popup = tk.Toplevel(root)

        popup.title(
            "Achievement Unlocked"
        )

        popup.geometry(
            "420x230"
        )

        popup.configure(
            bg="#111827"
        )

        popup.resizable(
            False,
            False
        )

        # Center Screen

        popup.update_idletasks()

        x = (
            popup.winfo_screenwidth() // 2
        ) - (
            420 // 2
        )

        y = (
            popup.winfo_screenheight() // 2
        ) - (
            230 // 2
        )

        popup.geometry(
            f"420x230+{x}+{y}"
        )

        # Fade Animation

        popup.attributes(
            "-alpha",
            0
        )
        
        tk.Label(

            popup,

            text="🏆",

            bg="#111827",

            fg="#facc15",

            font=("Segoe UI",48)

        ).pack(
            pady=(20,5)
        )

        tk.Label(

            popup,

            text="🏆 Achievement Unlocked!",

            bg="#111827",

            fg="#facc15",

            font=("Segoe UI",18,"bold")

        ).pack(
            pady=20
        )

        tk.Label(

            popup,

            text=achievement,

            bg="#111827",

            fg="white",

            font=("Segoe UI",16)

        ).pack(
            pady=10
        )

        tk.Button(

            popup,

            text="Continue",

            command=popup.destroy,

            bg="#22c55e",

            fg="white",

            width=15

        ).pack(
            pady=25
        )
        
        # ==========================
        # FADE IN
        # ==========================

        def fade(value=0):

            popup.attributes(
                "-alpha",
                value
            )

            if value < 1:

                popup.after(

                    25,

                    lambda: fade(
                        value + 0.1
                    )

                )

        fade()
        
        # ==========================
        # AUTO CLOSE
        # ==========================

        popup.after(

            3000,

            popup.destroy

        )