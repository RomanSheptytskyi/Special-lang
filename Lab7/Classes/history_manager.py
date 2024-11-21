from datetime import datetime
from tabulate import tabulate


class HistoryManager:
    def __init__(self):
        self.__history = []

    def log(self, operation, details=""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__history.append({"timestamp": timestamp, "operation": operation, "details": details})

    def show_history(self):
        print("\n--- Історія операцій ---")
        table = [[entry["timestamp"], entry["operation"], entry["details"]] for entry in self.__history]
        print(tabulate(table, headers=["Час", "Операція", "Деталі"], tablefmt="grid"))
