from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.worksheet.hyperlink import Hyperlink


def align_cells_horizontally(filename: str, alignment: str = 'left'):
    wb = load_workbook(filename)
    ws = wb.active
    alignment = Alignment(horizontal=alignment)
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = alignment

    wb.save(filename)

def add_hyperlink_to_cell(filename: str, cell):
    pass