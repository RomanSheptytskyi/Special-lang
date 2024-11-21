import os
import sys

lab8_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab8_root)

from Classes.bar_chart_visualizer import BarChartVisualizer
from Classes.line_chart_visualizer import LineChartVisualizer
from Classes.scatter_plot_visualizer import ScatterPlotVisualizer
from Classes.min_max_visualizer import MinMaxVisualizer
from Classes.combined_chart_visualizer import CombinedChartVisualizer

def main():
    while True:
        print("\nОберіть опцію:")
        print("1. Стовпчикова діаграма")
        print("2. Лінійний графік")
        print("3. Діаграма розсіювання")
        print("4. Показати мінімальні та максимальні значення")
        print("5. Відобразити всі діаграми одночасно")
        print("6. Вийти")

        choice = input("Введіть номер опції: ")

        if choice == '6':
            print("Програма завершена.")
            break

        file_path = input("Введіть шлях до CSV-файлу: ")

        if choice == '1':
            visualizer = BarChartVisualizer(file_path)
        elif choice == '2':
            visualizer = LineChartVisualizer(file_path)
        elif choice == '3':
            visualizer = ScatterPlotVisualizer(file_path)
        elif choice == '4':
            visualizer = MinMaxVisualizer(file_path)
        elif choice == '5':
            visualizer = CombinedChartVisualizer(file_path)
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            continue

        visualizer.visualize()
