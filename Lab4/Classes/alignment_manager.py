class AlignmentManager:

    def __init__(self):
        self.alignment = "center"

    def choose_alignment(self):
        print("Виберіть вирівнювання тексту:")
        print("1. Ліворуч")
        print("2. По центру")
        print("3. Праворуч")

        alignment_option = input("Виберіть опцію (1, 2 або 3): ").strip()
        if alignment_option == '1':
            self.alignment = "left"
        elif alignment_option == '2':
            self.alignment = "center"
        elif alignment_option == '3':
            self.alignment = "right"
        else:
            print("Неправильна опція. Встановлено вирівнювання по центру за замовчуванням.")
            self.alignment = "center"

    def _align_line(self, line, width):
        if self.alignment == 'left':
            return line.ljust(width)
        elif self.alignment == 'center':
            return line.center(width)
        elif self.alignment == 'right':
            return line.rjust(width)
        else:
            return line
