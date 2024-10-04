import os

from openpyxl import Workbook
from datetime import datetime

def create_output_workbook():
    wb_output = Workbook()
    sheet_output = wb_output.active
    sheet_output.title = 'Relatório Receita Federal'
    sheet_output.append(['CPF', 'Nome', 'Data de Nascimento', 'Situação Cadastral', 'Data da Inscrição', 'Mensagem'])

    return wb_output, sheet_output


def save_report(wb_output):
    current_date = datetime.now().strftime('%Y%m%d')
    current_time = datetime.now().strftime('%H%M%S')

    dir_path = 'reports'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    wb_output.save(f'{dir_path}/RelatorioReceitafederal_{current_date}_{current_time}.xlsx')
