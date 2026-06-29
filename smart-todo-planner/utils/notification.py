# ==========================
# IMPORTS
# ==========================

from tkinter import messagebox

# ==========================
# NOTIFICATION
# ==========================


class Notification:

    # ==========================
    # SUCCESS
    # ==========================

    @staticmethod
    def success(title="Success", message="Operation completed successfully."):

        messagebox.showinfo(title, message)

    # ==========================
    # ERROR
    # ==========================

    @staticmethod
    def error(title="Error", message="Something went wrong."):

        messagebox.showerror(title, message)

    # ==========================
    # WARNING
    # ==========================

    @staticmethod
    def warning(title="Warning", message="Please check your input."):

        messagebox.showwarning(title, message)

    # ==========================
    # CONFIRM
    # ==========================

    @staticmethod
    def confirm(title="Confirmation", message="Are you sure?"):

        return messagebox.askyesno(title, message)

    # ==========================
    # INFO
    # ==========================

    @staticmethod
    def info(title="Information", message="Information."):

        messagebox.showinfo(title, message)

    # ==========================
    # SAVE SUCCESS
    # ==========================

    @staticmethod
    def save_success():

        Notification.success("Saved", "Progress saved successfully.")

    # ==========================
    # RESET CONFIRM
    # ==========================

    @staticmethod
    def reset_confirm():

        return Notification.confirm("Reset", "Do you want to reset all data?")

    # ==========================
    # SETTINGS SAVED
    # ==========================

    @staticmethod
    def settings_saved():

        Notification.success("Settings", "Settings updated successfully.")

    # ==========================
    # FEATURE COMING SOON
    # ==========================

    @staticmethod
    def coming_soon():

        Notification.info("Coming Soon", "This feature will be available in Version 3.")
