import json
import csv
import os

class DataSaver:
    @staticmethod
    def save_to_json(data, filename):
        os.makedirs("../data", exist_ok=True)
        filepath = os.path.join("../data", filename)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Дані збережено в {filepath}")

    @staticmethod
    def save_to_csv(data, filename):
        os.makedirs("../data", exist_ok=True)
        filepath = os.path.join("../data", filename)
        if data:
            keys = data[0].keys()
            with open(filepath, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
        print(f"Дані збережено в {filepath}")

    @staticmethod
    def save_to_txt(data, filename):
        os.makedirs("../data", exist_ok=True)
        filepath = os.path.join("../data", filename)
        with open(filepath, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
        print(f"Дані збережено в {filepath}")

    @staticmethod
    def select_save_format(data, data_type):
        print("\nОберіть формат файлу для збереження:")
        print("1. JSON")
        print("2. CSV")
        print("3. TXT")
        choice = input("Виберіть опцію: ")

        filename = input("Введіть бажану назву файлу (без розширення): ")

        if choice == "1":
            filename += ".json"
            DataSaver.save_to_json(data, filename)
        elif choice == "2":
            filename += ".csv"
            DataSaver.save_to_csv(data, filename)
        elif choice == "3":
            filename += ".txt"
            DataSaver.save_to_txt(data, filename)
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            DataSaver.select_save_format(data, data_type)
