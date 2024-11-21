import os
import sys

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab3_root)


from Classes.art_operations import ArtOperations
from Classes.ascii_art import AsciiArtGenerator
from Classes.color_utils import ColorManager
from Classes.file_manager import FileManager
from Classes.fonts import FontManager
from Classes.error_handler import FontError, ColorError, SymbolError

def main():
    print("\nASCII-ART Генератор\n")

    while True:
        print("Виберіть опцію:")
        print("1 - Створити новий ASCII-арт")
        print("2 - Вийти з програми")

        choice = input("Ваш вибір (1 або 2): ")

        if choice == '1':
            text = input("Введіть текст для створення ASCII-арту: ")

            try:
                font_manager = FontManager()
                font_choice = font_manager.select_font()

                symbol = input("Введіть символ для створення ASCII-арту: ")
                art_generator = AsciiArtGenerator(text, font_choice, symbol)
                ascii_art = art_generator.generate_art()

                color_manager = ColorManager()
                color_choice = color_manager.select_color()
                ascii_art_colored = color_manager.get_colored_art(ascii_art, color_choice)

                print("\nASCII-арт з вибраними символами")
                print(ascii_art_colored)

                art_operations = ArtOperations(ascii_art)
                art_operations.change_symbol(color_choice, color_manager)

                resize_option = input("Бажаєте змінити розмір ASCII-арту? (yes/no): ").strip().lower()
                if resize_option in ['yes']:
                    resized_art = art_generator.resize_art()
                    ascii_art_colored = color_manager.get_colored_art(resized_art, color_choice)
                    print("\nASCII-арт з новим розміром")
                    print(ascii_art_colored)

                save_option = input("Зберегти ASCII-арт у файл? (yes/no): ").strip().lower()
                if save_option in ['yes']:
                    FileManager.save_to_file(ascii_art)

            except (FontError, ColorError, SymbolError) as e:
                print(e)
            except ValueError as e:
                print(e)

        elif choice == '2':
            print("Вихід")
            break

        else:
            print("Невірний вибір. Виберіть 1 або 2.")
