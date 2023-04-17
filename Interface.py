from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import ezdxf


class ProgrammInterface:
    """
    Класс для создания интерфейса приложения на Tkinter
    """

    def __init__(self):
        self.window = Tk()
        self.doc = None
        self.filename = ''

    def main_menu(self):
        """
        Создаем окно и запускаем программу
        :return:
        """
        self.window.title('DXF converter programm')
        self.window.geometry('600x500')
        self.create_dxf_file_button()
        self.draw_poliline_button()
        self.saving_files_button()

        self.window.mainloop()

    def create_dxf_file_button_handler(self):
        """
        Функция-обработчик создания dxf файла
        :return:
        """
        self.doc = ezdxf.new('R2000')
        messagebox.showinfo('Создание файла', f'Файл создан!')

    def create_dxf_file_button(self):
        """
        Создание кнопки создания dxf файла
        :return:
        """
        create_file_lbl = Label(self.window, text='Создать файл')
        create_file_lbl.grid(column=0, row=1)
        create_dxf_file_button = Button(self.window,
                                  text='Создать',
                                  command=self.create_dxf_file_button_handler)
        create_dxf_file_button.grid(column=1, row=1)

    def save_file_handler(self) -> None:
        """
        Функция-обработчик сохренения файла с возможностью выбора пути
        :return:
        """

        save_path_name = asksaveasfilename(initialfile='Untitled.dxf', defaultextension=".dxf",
                          filetypes=[("All Files", "*.*"), ("Dxf documents", "*.dxf")])
        self.doc.saveas(save_path_name)
        self.filename = save_path_name

    def saving_files_button(self) -> None:
        """
        Создание кнопки сохранения файла
        :return:
        """
        save_file_lbl = Label(self.window, text='Сохранить файл')
        save_file_lbl.grid(column=0, row=3)
        save_file_button = Button(self.window,
                                  text='Сохранить',
                                  command=self.save_file_handler)
        save_file_button.grid(column=1, row=3)

    def draw_poliline_button(self):
        draw_poliline_lbl = Label(self.window, text='Нарисовать полилинию')
        draw_poliline_lbl.grid(column=0, row=2)
        save_file_button = Button(self.window,
                                  text='Нарисовать',
                                  command=self.draw)
        save_file_button.grid(column=1, row=2)

    def draw(self):
        morpho = DXFFileWorker(self.window, self.doc, self.filename)
        morpho.make_polyline()
        messagebox.showinfo('Отрисовка полилинии', f'Полилиния нарисована.')

    def choose_morpho_to_draw(self):
        pass


class DXFFileWorker:

    def __init__(self, interface, doc, filename):
        self.interface = interface
        self.doc = doc
        self.modelspace = self.doc.modelspace()
        self.filename = filename

    def make_polyline(self):
        """
        Функция создает полилинию
        :return:
        """
        self.doc.layers.add(name='Mylines', color=7, linetype='CONTINUOUS')
        points = [(0, 0), (3, 0), (6, 3), (6, 6)]
        self.modelspace.add_lwpolyline(points, dxfattribs={"layer": "MyLines"})




