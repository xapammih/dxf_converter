import ezdxf
import os


def create_dxf_file():
    doc = ezdxf.new('R12')
    doc.saveas('dxf_files/Test_file.dxf')


def main():
    create_dxf_file()


if __name__ == '__main__':
    main()
