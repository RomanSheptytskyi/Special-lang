import os

class FileManager:
    @staticmethod
    def save_art_to_file(ascii_art):
        if not os.path.exists('../Data'):
            os.makedirs('../Data')

        filename = input("Введіть ім'я файлу для збереження ASCII-арту (наприклад, art.txt): ")
        filepath = os.path.join('../Data', filename)

        with open(filepath, 'w') as file:
            for line in ascii_art:
                file.write(line + '\n')

        print(f"ASCII-арт збережено у файл {filepath}")
