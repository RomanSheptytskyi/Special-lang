import os
import sys

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab4_root)


from Lab4.Classes.ASCIIart_generator import ArtGenerator
from Lab4.Classes.art_operations import ArtOperations

def main():
    while True:
        print("Вітаємо в програмі генерації ASCII-арту!")
        print("1. Генерувати ASCII-арт")
        print("2. Вийти з програми")
        choice = input("Виберіть опцію (1 або 2): ").strip()

        if choice == '1':
            generator = ArtOperations()

            generator.text = input("Введіть слово або фразу для конвертації в ASCII-арт: ")
            generator.width = int(input("Введіть ширину (за замовчуванням 10): ") or 10)
            generator.height = int(input("Введіть висоту (за замовчуванням 10): ") or 10)

            generator.choose_alignment()
            generator.choose_color()

            art_generator = ArtGenerator(generator.char_set, generator.width, generator.height, generator.text)
            ascii_art = art_generator.generate_art()

            generator.display_art(ascii_art)

            print("Бажаєте зберегти ASCII-арт у файл?")
            print("1. Так")
            print("2. Ні")
            save_option = input("Виберіть опцію (1 або 2): ").strip()

            if save_option == '1':
                generator.save_art_to_file(ascii_art)
            elif save_option == '2':
                print("ASCII-арт не збережено.")
            else:
                print("Неправильна опція. ASCII-арт не збережено.")

        elif choice == '2':
            print("Дякуємо за використання програми!")
            break
        else:
            print("Неправильна опція. Спробуйте ще раз.")

