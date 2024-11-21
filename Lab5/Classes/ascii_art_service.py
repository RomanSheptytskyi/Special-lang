from Classes.colormanager import ColorService
from Classes.cube import Cube
from Classes.cylinder import Cylinder
from Classes.file_saver import FileManager

class AsciiArtService:
    def __init__(self):
        self.shape = None
        self.color_service = ColorService()

    def display_ascii_art(self):
        if not self.shape:
            print("Форма не встановлена.")
            return
        projection = self.shape.project_to_2d()
        self.shape.render_ascii(projection)

    def set_shape(self, shape_type, size, height=None):
        if shape_type == "cube":
            self.shape = Cube(size)
        elif shape_type == "cylinder":
            self.shape = Cylinder(size, height or size)
        else:
            print("Невідома форма")

    def set_color(self, color_name):
        color_code = self.color_service.get_color_code(color_name)
        if self.shape:
            self.shape.set_color(color_code)

    def rotate_shape(self, angle_x, angle_y, angle_z):
        if self.shape:
            self.shape.rotate(angle_x, angle_y, angle_z)

    def save_to_file(self, filename):
        if not self.shape:
            print("Форма не встановлена.")
            return
        projection = self.shape.project_to_2d()
        FileManager.save_to_file(filename, projection)
