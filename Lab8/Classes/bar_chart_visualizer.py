from matplotlib import pyplot as plt
from Classes.data_visualizer import DataVisualizer

class BarChartVisualizer(DataVisualizer):
    def process_data(self):
        self._data = self._data.groupby('Humidity')['Temperature'].sum()
        print("Дані оброблено для стовпчикової діаграми.")

    def plot(self):
        self._data.plot(kind='bar', color='skyblue')
        plt.title("Стовпчикова діаграма")
        plt.xlabel("Вологість повітря")
        plt.ylabel("Температура")
        print("Стовпчикову діаграму побудовано.")
