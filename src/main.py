from bot.driver import get_chrome_driver
from bot.person_processor import process_person
from bot.form_filler import new_query
from entities.input_person import InputPerson
from data.input_reader import load_input_data
from data.output_writer import create_output_workbook, save_report


def display_progress_bar(completed, total, bar_length=50):
    progress = int(bar_length * completed / total)
    bar = '=' * progress + ' ' * (bar_length - progress)
    print(f'\r[{bar}] {completed}/{total} linhas processadas', end='')


def main():
    driver = get_chrome_driver()
    driver.get('https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp')

    wb_input, sheet_input = load_input_data('cpfDataNascimento.xlsx')
    wb_output, sheet_output = create_output_workbook()
    
    total_rows = sheet_input.max_row - 1 
    try:
        print('Iniciando processamento...')
        for index, row in enumerate(sheet_input.iter_rows(min_row=2, values_only=True), start=1):
            display_progress_bar(index, total_rows)

            input_person = InputPerson(row)
            process_person(driver, input_person, sheet_output)
            new_query(driver)

        print('\nProcessamento concluído')
        print('Salvando relatório...')
        save_report(wb_output)
        
        print('Relatório salvo com sucesso!')
    finally:
        driver.quit()
        wb_input.close()
        wb_output.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print(e)
