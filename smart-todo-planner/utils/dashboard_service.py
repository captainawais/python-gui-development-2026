# ==========================
# IMPORTS
# ==========================

from utils.storage import Storage

# ==========================
# DASHBOARD SERVICE
# ==========================


class DashboardService:

    # ==========================
    # GET SUMMARY
    # ==========================

    @staticmethod
    def get_summary():

        data = Storage.load()

        habits = data.get("habits", [])

        total_habits = len(habits)

        total_days = 0
        completed = 0

        for habit in habits:

            days = habit.get("days", [])

            total_days += len(days)

            completed += sum(days)

        pending = total_days - completed

        if total_days == 0:

            success_rate = 0

        else:

            success_rate = round((completed / total_days) * 100, 1)

        return {
            "total_habits": total_habits,
            "completed": completed,
            "pending": pending,
            "success_rate": success_rate,
            "current_streak": data.get("current_streak", 0),
            "best_streak": data.get("best_streak", 0),
            "last_completed_date": data.get("last_completed_date", ""),
        }

    # ==========================
    # TOTAL COMPLETED
    # ==========================

    @staticmethod
    def total_completed():

        return DashboardService.get_summary()["completed"]

    # ==========================
    # TOTAL PENDING
    # ==========================

    @staticmethod
    def total_pending():

        return DashboardService.get_summary()["pending"]

    # ==========================
    # SUCCESS RATE
    # ==========================

    @staticmethod
    def success_rate():

        return DashboardService.get_summary()["success_rate"]

    # ==========================
    # CURRENT STREAK
    # ==========================

    @staticmethod
    def current_streak():

        return DashboardService.get_summary()["current_streak"]

    # ==========================
    # BEST STREAK
    # ==========================

    @staticmethod
    def best_streak():

        return DashboardService.get_summary()["best_streak"]
