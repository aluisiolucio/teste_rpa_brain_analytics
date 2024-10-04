from openpyxl import load_workbook


def load_input_data(filename):
    wb_input = load_workbook(filename, read_only=True)

    return wb_input, wb_input.active
