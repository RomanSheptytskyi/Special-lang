from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import os


class DataVisualizer(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = None

    def visualize(self):
        try:
            self.load_data()
            self.process_data()
            self.plot()
            self.export()
        except KeyError as e:
            print(f"Помилка: Відсутній необхідний стовпець у файлі - {e}")
        except FileNotFoundError:
            print("Помилка: Файл не знайдено.")
        except pd.errors.EmptyDataError:
            print("Помилка: Файл порожній або має некоректний формат.")

    def load_data(self):
        self._data = pd.read_csv(self.file_path)
        print("Дані завантажено успішно.")

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def plot(self):
        pass

    def export(self):
        save_option = input("Бажаєте зберегти діаграму? (так/ні): ").strip().lower()
        if save_option == 'так':
            file_format = input("Оберіть формат файлу для збереження (png/svg): ").strip().lower()
            if file_format not in ['png', 'svg']:
                print("Невірний формат. Діаграму буде збережено у форматі PNG за замовчуванням.")
                file_format = 'png'

            file_name = input("Введіть назву файлу (без розширення): ").strip()
            if not file_name:
                file_name = "chart"

            folder_path = 'data'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_name_with_extension = os.path.join(folder_path, f"{file_name}.{file_format}")
            try:
                plt.tight_layout()
                plt.savefig(file_name_with_extension)
                print(f"Діаграму збережено як '{file_name_with_extension}'.")
            except Exception as e:
                print(f"Помилка під час збереження файлу: {e}")
        else:
            print("Діаграму не збережено.")
        plt.show()
