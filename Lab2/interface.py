from Lab2.classes import Calculator

def main():
    try:
        calc = Calculator()
    except TypeError as e:
        print(e)
        exit(1)

    while True:
        print("\nГоловне меню:")
        print("1. Виконати обчислення")
        print("2. Переглянути історію")
        print("3. Отримати результат з пам'яті")
        print("4. Очистити результат з пам'яті")
        print("5. Налаштувати кількість знаків після коми")
        print("6. Вийти")

        choice = input("Оберіть дію: ")

        match choice:
            case '1':
                try:
                    calc.calculate()
                except ZeroDivisionError as e:
                    print(e)
                except ValueError as e:
                    print(e)
            case '2':
                calc.history.show_history()
            case '3':
                print(f"Збережене значення з пам'яті: {calc.memory.get_memory()}")
            case '4':
                calc.memory.clear_memory()
                print("Збережене значення очищено")
            case '5':
                try:
                    calc.settings.set_decimal_places()
                except ValueError as e:
                    print(e)
                except TypeError as e:
                    print(e)
            case '6':
                print("Вихід із програми.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")
