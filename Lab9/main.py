from Lab9.facade import RunnerFacade


def main():
    facade = RunnerFacade()
    while True:
        facade.show_menu()
        try:
            choice = int(input("Оберіть лабораторну роботу: "))
            if choice == 0:
                break
            facade.run_lab(choice)
        except ValueError:
            print("Введіть коректний номер лабораторної роботи.")