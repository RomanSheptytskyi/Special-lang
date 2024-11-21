from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

class ScatterPlotVisualizer(DataVisualizer):
    def process_data(self):
        print("Дані готові для діаграми розсіювання.")

    def plot(self):
        plt.scatter(self._data['X'], self._data['Y'], color='red', alpha=0.5)
        plt.title("Діаграма розсіювання")
        plt.xlabel("X")
        plt.ylabel("Y")
        print("Діаграму розсіювання побудовано.")
