import json

class ColorManager:
    def __init__(self):
        self.color_code = ""
        self.colors = self.load_colors()

    def load_colors(self):
        with open('../Lab4/Config/colors.json', 'r', encoding='utf-8') as file:
            colors = json.load(file)
            return colors["colors"]

    def choose_color(self):
        print("Виберіть колір ASCII-арту:")
        for key in self.colors.keys():
            print(key)

        color_option = input("Виберіть опцію: ").strip()
        self.color_code = self.colors.get(color_option, "0")

    def apply_color(self, text):
        return f"\033[{self.color_code}m{text}\033[0m"
