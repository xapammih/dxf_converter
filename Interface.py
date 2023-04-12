from tkinter import *
from tkinter.filedialog import asksaveasfile
import re
import ezdxf


class ProgrammInterface:
    """
    Класс для
    """
    window = Tk()

    def create_window(self):
        """
        Создаем окно и запускаем программу
        :return:
        """
        self.window.title('DXF converter programm')
        self.saving_files()
        self.window.mainloop()

    def change_window_size(self):
        """
        Функция, запрашивающая размер окна перед его созданием
        :return:
        """
        window_size = input('Введите размер окна в пикселях через пробел: ').split(' ')
        self.window.geometry(f'{window_size[0]}x{window_size[1]}')
        self.create_window()

    def save_file_clicked(self):
        doc = ezdxf.new('R12')
        doc.saveas('')
        f = asksaveasfile(initialfile=f'Untitled.dxf', defaultextension=".dxf",
                          filetypes=[("All Files", "*.*"), ("Dxf documents", "*.dxf")])

    def saving_files(self):

        save_file_button = Button(self.window,
                                  text='Сохранить файл',
                                  command=lambda: self.save_file_clicked())
        save_file_button.grid(column=2, row=0)


class DXFFileWorker:
    pass

