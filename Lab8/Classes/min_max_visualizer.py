import pandas as pd

from Classes.data_visualizer import DataVisualizer


class MinMaxVisualizer(DataVisualizer):
    def visualize(self):
        try:
            self.load_data()
            self.process_data()
        except FileNotFoundError:
            print("Помилка: Файл не знайдено.")
        except pd.errors.EmptyDataError:
            print("Помилка: Файл порожній або має некоректний формат.")

    def process_data(self):
        print("\nМінімальні та максимальні значення для кожної колонки:")

        for column in self._data.columns:
            column_min = self._data[column].min()
            column_max = self._data[column].max()
            print(f"{column}: Minimum = {column_min}, Maximum = {column_max}")

    def plot(self):
        pass
