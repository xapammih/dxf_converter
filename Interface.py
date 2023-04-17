from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import ezdxf


class ProgrammInterface:
    """
    Класс для создания интерфейса приложения на Tkinter
    """

    def __init__(self):
        self.window = Tk()
        self.doc = ezdxf.new('R2000')
        self.filename = ''
        self.tab_control = ttk.Notebook(self.window)
        self.tab1 = None
        self.tab2 = None
        self.current_morpho = None
        self.choose_morpho_combobox = None

    def main_menu(self) -> None:
        """
        Создаем окно и запускаем программу
        :return:
        """
        self.window.title('DXF converter programm')
        self.window.geometry('600x500')
        self.making_tabs()
        self.tab_control.pack(expand=1, fill='both')
        self.create_dxf_file_button()
        self.draw_poliline_button()
        self.saving_files_button()
        self.choose_morpho_to_draw()
        self.get_morpho_data_button()

        self.window.mainloop()

    def making_tabs(self):
        """
        Функция, создающая вкладки
        :return:
        """
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Меню')
        self.tab_control.add(self.tab2, text='Вторая')

    def create_dxf_file_button_handler(self) -> None:
        """
        Функция-обработчик создания dxf файла
        :return:
        """
        self.doc = ezdxf.new('R2000')
        messagebox.showinfo('Создание файла', f'Файл создан!')

    def create_dxf_file_button(self) -> None:
        """
        Создание кнопки создания dxf файла
        :return:
        """
        create_file_lbl = Label(self.tab1, text='Создать файл', padx=5, pady=5)
        create_file_lbl.grid(column=0, row=1)
        create_dxf_file_button = Button(self.tab1,
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
        save_file_lbl = Label(self.tab1, text='Сохранить файл', padx=5, pady=5)
        save_file_lbl.grid(column=0, row=3)
        save_file_button = Button(self.tab1,
                                  text='Сохранить',
                                  command=self.save_file_handler)
        save_file_button.grid(column=1, row=3)

    def draw_poliline_button(self):
        """
        Создание кнопки отрисовки полилинии
        :return:
        """
        draw_poliline_lbl = Label(self.tab2, text='Нарисовать полилинию', padx=5, pady=5)
        draw_poliline_lbl.grid(column=0, row=1)
        save_file_button = Button(self.tab2,
                                  text='Нарисовать',
                                  command=self.draw)
        save_file_button.grid(column=1, row=1)

    def draw(self):
        """
        Отрисовка полилинии
        :return:
        """
        morpho = DXFFileWorker(self.window, self.doc, self.filename, self.current_morpho)
        morpho.make_polyline()
        messagebox.showinfo('Отрисовка полилинии', f'Полилиния нарисована.')

    def get_value(self):
        self.current_morpho = self.choose_morpho_combobox.get()

    def choose_morpho_to_draw(self):
        values = (1, 2, 3, 4, 5)
        morpho_draw_selector = Combobox(self.tab2, values=values)
        self.choose_morpho_combobox = morpho_draw_selector
        morpho_draw_selector_label = Label(self.tab2, text='Выберите морфоствор для отрисовки', padx=5, pady=5)
        morpho_draw_selector_label.grid(column=0, row=0)
        morpho_draw_selector.grid(column=1, row=0)

    def get_morpho_data_button(self):
        get_morpho_data = Button(self.tab2, text='Записать', command=self.get_value)
        get_morpho_data.grid(column=2, row=0)


class DXFFileWorker:

    def __init__(self, interface, doc, filename, cur_morpho):
        self.interface = interface
        self.doc = doc
        self.modelspace = self.doc.modelspace()
        self.filename = filename
        self.cur_morpho = cur_morpho

    def make_polyline(self):
        """
        Функция создает полилинию
        :return:
        """
        shift_constant = int(self.cur_morpho) * 10
        self.doc.layers.add(name='Морфостворы', color=7, linetype='CONTINUOUS')
        points = [(0, 0), (3, 0), (6, 3), (6, 6)]
        points_with_koeff = [(x + shift_constant, y + shift_constant) for x, y in points]
        self.modelspace.add_lwpolyline(points_with_koeff, dxfattribs={"layer": "Морфостворы"})




