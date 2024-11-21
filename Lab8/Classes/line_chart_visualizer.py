from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

class LineChartVisualizer(DataVisualizer):
    def process_data(self):
        self._data.sort_values('Date', inplace=True)
        print("Дані оброблено для лінійного графіка.")

    def plot(self):
        plt.plot(self._data['Date'], self._data['Temperature'], marker='o', linestyle='-', color='green')
        plt.title("Лінійний графік")
        plt.xlabel("Дата")
        plt.ylabel("Температура")
        plt.xticks(rotation=45)
        print("Лінійний графік побудовано.")
