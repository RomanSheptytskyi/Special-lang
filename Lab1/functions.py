import math
from variables import memory, history, decimal_places

def set_memory(value):
    global memory
    memory = value

def get_memory():
    return memory

def set_decimal_places():
    global decimal_places
    places = input("Вкажіть кількість знаків після коми? ")
    if places.isalpha():
        raise TypeError("Введіть ціле (додатнє) число.")
    elif int(places) >= 0:
        decimal_places = int(places)
        print(f"Кількість знаків після коми встановлено на {decimal_places}.")
    else:
        raise ValueError("Кількість знаків повинна бути не від'ємною. Спробуйте ще раз.")

def get_decimal_places():
    return decimal_places

def get_input():
    try:
        num1_input = input("Введіть перше число (або 'm' для використання значення з пам'яті): ")
        num1 = get_memory() if num1_input.lower() == 'm' else float(num1_input)

        operator = get_operator()
        num2 = None
        if operator != '√':
            while True:
                try:
                    num2_input = input("Введіть друге число (або 'm' для використання значення з пам'яті): ")
                    num2 = get_memory() if num2_input.lower() == 'm' else float(num2_input)
                    break
                except ValueError:
                    print("Неправильне введення другого числа. Спробуйте ще раз.")

        return num1, operator, num2
    except ValueError:
        print("Неправильне введення. Спробуйте ще раз.")
        return get_input()

def check_operator(operator):
    return operator in ['+', '-', '*', '/', '^', '√', '%']

def get_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if check_operator(operator):
            return operator
        else:
            print("Невірний оператор. Введіть правильний оператор.")

def calculate(num1, operator, num2):

    if operator == '+':
        return round(num1 + num2, get_decimal_places())
    elif operator == '-':
        return round(num1 - num2, get_decimal_places())
    elif operator == '*':
        return round(num1 * num2, get_decimal_places())
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return round(num1 / num2, get_decimal_places())
    elif operator == '^':
        return round(math.pow(num1, num2), get_decimal_places())
    elif operator == '√':
        if num1 < 0:
            raise ValueError("Квадратний корінь з від'ємного числа неможливий.")
        return round(math.sqrt(num1), get_decimal_places())
    elif operator == '%':
        if num2 == 0:
            raise ZeroDivisionError("Процент з нуля неможливий")
        return round(num1 % num2, get_decimal_places())


def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    if history:
        print("Історія обчислень:")
        for entry in history:
            print(entry)
    else:
        print("Історія порожня.")

def calculator():
    while True:
        num1, operator, num2 = get_input()

        result = calculate(num1, operator, num2)
        if result is not None:
            print(f"Результат: {result}")
            add_to_history(f"{num1} {operator} {num2 if num2 is not None else ''}", result)

            if input("Хочете зберегти результат у пам'ять? (y/n): ").lower() == 'y':
                set_memory(result)
                print(f"Результат {result} збережено в пам'яті.")

        if input("Хочете виконати ще одне обчислення? (y/n): ").lower() == 'n':
            break

def main():
    while True:
        print("\nГоловне меню:")
        print("1.Виконати обчислення")
        print("2.Переглянути історію")
        print("3.Отримати результат з пам'яті")
        print("4.Очистити результат з пам'яті")
        print("5.Налаштувати кількість знаків після коми")
        print("6.Вийти")

        choice = input("Оберіть дію: ")

        if choice == '1':
            try:
                calculator()
            except ZeroDivisionError as e:
                print(e)
            except ValueError as e:
                print(e)
        elif choice == '2':
            show_history()
        elif choice == '3':
            print(f"Збережене значення з пам'яті: {get_memory()}")
        elif choice == '4':
            set_memory(0)
            print("Збережене значення очищено")
        elif choice == '5':
            try:
                set_decimal_places()
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)
        elif choice == '6':
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

