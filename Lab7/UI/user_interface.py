import os
import sys

lab7_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab7_root)

from Classes.console_app import ConsoleApp

def main():
    app = ConsoleApp()

    while True:
        print("\n--- Консольний додаток ---")
        print("1. Показати користувачів")
        print("2. Показати пости")
        print("3. Додати нового користувача")
        print("4. Додати новий пост")
        print("5. Видалити користувача")
        print("6. Видалити пост")
        print("7. Зберегти користувачів")
        print("8. Зберегти пости")
        print("9. Переглянути історію")
        print("10. Вийти")
        choice = input("Оберіть опцію: ")

        match choice:
            case "1":
                app.show_users()
            case "2":
                app.show_posts()
            case "3":
                app.add_user()
            case "4":
                app.add_post()
            case "5":
                app.delete_user()
            case "6":
                app.delete_post()
            case "7":
                app.save_users()
            case "8":
                app.save_posts()
            case "9":
                app.show_history()
            case "10":
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")
