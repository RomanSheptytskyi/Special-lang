import os

class FileManager:
    @staticmethod
    def save_to_file(filename, projection):
        os.makedirs("../Data", exist_ok=True)

        file_path = os.path.join("../Data", filename)

        try:
            with open(file_path, 'w') as file:
                for row in projection:
                    file.write("".join(row) + "\n")
            print(f"ASCII арт збережено в {file_path}")
        except Exception as e:
            print(f"Помилка при збереженні файлу: {e}")
