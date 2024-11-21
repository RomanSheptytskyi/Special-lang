from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

class CombinedChartVisualizer(DataVisualizer):
    def process_data(self):
        self.bar_data = self._data.groupby('Humidity')['Temperature'].sum()
        self.line_data = self._data.sort_values('Date')
        self.scatter_data = self._data[['X', 'Y']]

    def plot(self):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        # Стовпчикова діаграма
        self.bar_data.plot(kind='bar', color='skyblue', ax=axes[0])
        axes[0].set_title("Стовпчикова діаграма")
        axes[0].set_xlabel("Вологість повітря")
        axes[0].set_ylabel("Температура")

        # Лінійний графік
        axes[1].plot(self.line_data['Date'], self.line_data['Temperature'], marker='o', linestyle='-', color='green')
        axes[1].set_title("Лінійний графік")
        axes[1].set_xlabel("Дата")
        axes[1].set_ylabel("Температура")
        axes[1].tick_params(axis='x', rotation=45)

        # Діаграма розсіювання
        axes[2].scatter(self.scatter_data['X'], self.scatter_data['Y'], color='red', alpha=0.5)
        axes[2].set_title("Діаграма розсіювання")
        axes[2].set_xlabel("X")
        axes[2].set_ylabel("Y")

        plt.tight_layout()
