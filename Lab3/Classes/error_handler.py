class FontError(Exception):
    def __init__(self, font):
        self.message = f"Помилка: Невірний вибір шрифта '{font}'."
        super().__init__(self.message)

class ColorError(Exception):
    def __init__(self, color):
        self.message = f"Помилка: Невірний вибір кольору '{color}'."
        super().__init__(self.message)

class SymbolError(Exception):
    def __init__(self, symbol):
        self.message = "Помилка: Символ не може бути порожнім."
        super().__init__(self.message)
