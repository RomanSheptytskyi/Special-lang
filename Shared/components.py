import math
from abc import ABC, abstractmethod

memory = 0
history = []
decimal_places = 2


class Memory:
    def __init__(self):
        self.__memory = memory

    def set_memory(self, value):
        self.__memory = value

    def get_memory(self):
        return self.__memory

    def clear_memory(self):
        self.__memory = 0


class History:
    def __init__(self):
        self.__history = history

    def add_to_history(self, expression, result):
        self.__history.append(f"{expression} = {result}")

    def show_history(self):
        if self.__history:
            print("Історія обчислень:")
            for entry in self.__history:
                print(entry)
        else:
            print("Історія порожня.")


class Settings:
    def __init__(self):
        self.__decimal_places = decimal_places

    def set_decimal_places(self):
        places = input("Вкажіть кількість знаків після коми: ")
        if places.isalpha():
            raise TypeError("Введіть ціле (додатнє) число.")
        elif int(places) >= 0:
            self.__decimal_places = int(places)
            print(f"Кількість знаків після коми встановлено на {self.__decimal_places}.")
        else:
            raise ValueError("Кількість знаків повинна бути не від'ємною. Спробуйте ще раз.")

    def get_decimal_places(self):
        return self.__decimal_places


class BaseCalculator(ABC):
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.settings = Settings()

    def get_input(self):
        try:
            num1_input = input("Введіть перше число (або 'm' для використання значення з пам'яті): ")
            num1 = self.memory.get_memory() if num1_input.lower() == 'm' else float(num1_input)
            operator = self.get_operator()

            num2 = None
            if operator != '√':
                while True:
                    try:
                        num2_input = input("Введіть друге число (або 'm' для використання значення з пам'яті): ")
                        num2 = self.memory.get_memory() if num2_input.lower() == 'm' else float(num2_input)
                        break
                    except ValueError:
                        print("Неправильне введення другого числа. Спробуйте ще раз.")
            return num1, operator, num2
        except ValueError:
            print("Неправильне введення. Спробуйте ще раз.")
            return self.get_input()

    def check_operator(self, operator):
        return operator in ['+', '-', '*', '/', '^', '√', '%']

    def get_operator(self):
        while True:
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            if self.check_operator(operator):
                return operator
            else:
                print("Невірний оператор. Введіть правильний оператор.")

    @abstractmethod
    def perform_operators(self, num1, operator, num2):
        pass
