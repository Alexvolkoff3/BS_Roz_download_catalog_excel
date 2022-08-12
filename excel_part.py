from io import BytesIO
from urllib.request import urlopen

import xlsxwriter
from main import array


def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\Users\setup\Desktop\Itstep\requests Roz\data.xlsx')
    page = book.add_worksheet('products')

    cell_format = book.add_format()
    cell_format.set_text_wrap()
    cell_format.set_align('left')
    cell_format.set_align('top')
    cell_format.set_border(1)
    page.set_default_row(60)
    row = 1
    column = 0

    data = ('Продавець', 'Наявність', 'Назва', 'Ціна', 'Фото', 'Посилання')
    page.write_row('A1', data, cell_format)

    page.autofilter('A1:F1')

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 40)
    page.set_column("D:D", 20)
    page.set_column("E:E", 20)
    page.set_column("F:F", 40)

    for item in parametr():
        page.write(row, column, item[0], cell_format)
        page.write(row, column + 1, item[1], cell_format)
        page.write(row, column + 2, item[2], cell_format)
        page.write(row, column + 3, item[3], cell_format)
        image_data = BytesIO(urlopen(item[4]).read())
        page.insert_image(row, column + 4, item[4], {'image_data': image_data,
                                                     # 'x_offset': 0,
                                                     # 'y_offset': 0,
                                                     'x_scale': 0.09,
                                                     'y_scale': 0.08,
                                                     # 'object_position': 1
                                                     })
        page.write(row, column + 5, item[5], cell_format)
        row += 1

    book.close()


writer(array)
