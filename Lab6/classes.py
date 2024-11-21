import math

from Shared.components import BaseCalculator


class Calculator(BaseCalculator):
    def perform_operators(self, num1, operator, num2):
        decimal_places = self.settings.get_decimal_places()

        match operator:
            case '+':
                return round(num1 + num2, decimal_places)
            case '-':
                return round(num1 - num2, decimal_places)
            case '*':
                return round(num1 * num2, decimal_places)
            case '/':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе.")
                return round(num1 / num2, decimal_places)
            case '^':
                return round(math.pow(num1, num2), decimal_places)
            case '√':
                if num1 < 0:
                    raise ValueError("Квадратний корінь з від'ємного числа неможливий.")
                return round(math.sqrt(num1), decimal_places)
            case '%':
                if num2 == 0:
                    raise ZeroDivisionError("Процент з нуля неможливий.")
                return round(num1 % num2, decimal_places)
            case _:
                raise ValueError("Невідомий оператор.")

    def calculate(self):
        while True:
            num1, operator, num2 = self.get_input()
            result = self.perform_operators(num1, operator, num2)
            if result is not None:
                print(f"Результат: {result}")
                self.history.add_to_history(f"{num1} {operator} {num2 if num2 is not None else ''}", result)

                if input("Хочете зберегти результат у пам'ять? (y/n): ").lower() == 'y':
                    self.memory.set_memory(result)
                    print(f"Результат {result} збережено в пам'яті.")

            if input("Хочете виконати ще одне обчислення? (y/n): ").lower() == 'n':
                break
