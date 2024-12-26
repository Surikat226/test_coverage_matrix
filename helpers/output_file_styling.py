from dataclasses import dataclass
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.worksheet.hyperlink import Hyperlink


@dataclass
class ExcelStyling:
    output_file_path: str

    @property
    def wb(self):
        wb = load_workbook(self.output_file_path)
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

        self.wb.save(self.output_file_path)

    def add_hyperlinks_to_indexes(self, indexes_list: list[str]):
        link = Hyperlink()
        pass

    def color_cell(self, color):
        pass