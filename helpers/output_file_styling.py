from dataclasses import dataclass
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.worksheet.hyperlink import Hyperlink


@dataclass
class ExcelStyling:
    filename: str

    @property
    def wb(self):
        wb = load_workbook(self.filename)
        return wb

    @property
    def ws(self):
        ws = self.wb.active
        return ws

    def align_cells_horizontally(self, alignment: str = 'left'):
        alignment = Alignment(horizontal=alignment)
        for row in self.ws.iter_rows():
            for cell in row:
                cell.alignment = alignment

        self.wb.save(self.filename)

    def add_hyperlinks_to_indexes(self, indexes_list: list[str]):
        link = Hyperlink()
        pass