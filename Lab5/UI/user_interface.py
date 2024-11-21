import os
import sys

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab5_root)

from Classes.ascii_art_service import AsciiArtService
from Classes.cylinder import Cylinder


def user_interface():
    ascii_art_service = AsciiArtService()

    while True:
        ascii_art_service.display_ascii_art()

        print("\nМеню:")
        print("1. Встановити форму (cube/cylinder)")
        print("2. Встановити розмір")
        print("3. Встановити висоту (тільки для циліндра)")
        print("4. Обертати форму")
        print("5. Зберегти ASCII арт у файл")
        print("6. Встановити колір")
        print("7. Вихід")
        choice = input("Виберіть опцію: ").strip()

        match choice:
            case '1':
                shape_type = input("Виберіть форму (cube/cylinder): ").strip().lower()
                size = int(input("Введіть розмір форми: "))
                height = int(input("Введіть висоту циліндра: ")) if shape_type == "циліндр" else None
                ascii_art_service.set_shape(shape_type, size, height)
            case '2':
                size = int(input("Введіть новий розмір: "))
                if ascii_art_service.shape:
                    ascii_art_service.shape.size = size
            case '3':
                if isinstance(ascii_art_service.shape, Cylinder):
                    height = int(input("Введіть нову висоту для циліндра: "))
                    ascii_art_service.shape.height = height
                else:
                    print("Коригування висоти доступне тільки для циліндра.")
            case '4':
                angle_x = float(input("Введіть обертання навколо X (градуси): "))
                angle_y = float(input("Введіть обертання навколо Y (градуси): "))
                angle_z = float(input("Введіть обертання навколо Z (градуси): "))
                ascii_art_service.rotate_shape(angle_x, angle_y, angle_z)
            case '5':
                filename = input("Введіть ім'я файлу для збереження ASCII арту (наприклад, 'art.txt'): ")
                ascii_art_service.save_to_file(filename)
            case '6':
                print("Доступні кольори:", ", ".join(ascii_art_service.color_service.list_colors()))
                color_name = input("Виберіть колір: ").strip()
                ascii_art_service.set_color(color_name)
            case '7':
                print("Вихід з програми. До побачення!")
                break
            case _:
                print("Неправильна опція. Будь ласка, спробуйте ще раз.")
