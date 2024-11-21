from pathlib import Path

class FileManager:
    @staticmethod
    def save_to_file(ascii_art):
        data_dir = Path('../data')
        data_dir.mkdir(parents=True, exist_ok=True)

        filename = input("Введіть назву файлу для збереження (без розширення): ") + '.txt'
        file_path = data_dir / filename

        with file_path.open('w') as f:
            f.write(ascii_art)

        print(f"ASCII-арт збережено у файл {file_path}")
