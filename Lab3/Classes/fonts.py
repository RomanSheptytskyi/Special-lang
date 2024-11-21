from Classes.error_handler import FontError

class FontManager:
    def __init__(self):
        self.fonts = [
            "dot", "starwars", "shadow", "banner", "cyberlarge",
            "straight", "univers", "caligraphy", "stellar", "3d", "ghost"
        ]

    def display_fonts(self):
        print("\nДоступні шрифти:")
        print(", ".join(self.fonts))

    def select_font(self):
        self.display_fonts()

        font_choice = input("Введіть назву шрифту з наведеного списку: ").strip()

        if font_choice not in self.fonts:
            raise FontError(f"Шрифт '{font_choice}' не знайдено. Спробуйте ще раз.")

        return font_choice
