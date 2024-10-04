# Automação de Consulta de Situação Cadastral na Receita Federal

Este projeto é um **teste técnico** para um freelancer em `Python`, desenvolvido para automatizar consultas de situação cadastral no site da Receita Federal, utilizando o `Selenium` para interagir com o site e a biblioteca `openpyxl` para manipular planilhas Excel.

## Funcionalidades

- Leitura de uma planilha Excel de entrada com os dados (CPF e Data de Nascimento) a serem consultados.
- Preenchimento automático dos campos no formulário da Receita Federal via Selenium.
- Tratamento do hCaptcha utilizando Selenium.
- Extração das informações do resultado da consulta e geração de um relatório em Excel.

## Pré-requisitos

- Python 3.12+
- Google Chrome
- ChromeDriver (gerenciado automaticamente pela biblioteca `webdriver_manager`)

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/aluisiolucio/teste_rpa_brain_analytics.git
    cd teste_rpa_brain_analytics
    ```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate  # Windows
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Estrutura do Projeto

```
src
├── bot/
│   ├── driver.py             # Configuração do WebDriver (Chrome)
│   ├── form_filler.py        # Funções para preencher o formulário e hCaptcha
│   ├── error_handler.py      # Tratamento de erros durante a consulta
│   ├── person_processor.py   # Processamento de cada consulta de CPF
├── data/
│   ├── input_reader.py       # Leitura dos dados de entrada do Excel
│   ├── output_writer.py      # Criação do relatório Excel
├── entities/
│   ├── input_person.py       # Classe para representar os dados de entrada
│   ├── output_person.py      # Classe para representar os dados de saída
├── main.py                   # Arquivo principal que roda a automação
├── requirements.txt          # Dependências do projeto
└── cpfDataNascimento.xlsx    # Dados de entrada
```

## Como Usar

1. **Execute o script principal**:

   Após verificar se o arquivo de entrada `cpfDataNascimento.xlsx` está presente, execute o script principal:

   ```bash
   python main.py
   ```

3. **Acompanhe o progresso**:

   O progresso será exibido diretamente no terminal em formato de barra de progresso, conforme as consultas forem realizadas.

4. **Resultados**:

   O relatório será salvo na pasta `reports/`, com o nome no formato `RelatorioReceitafederal_YYYYMMDD_HHMMSS.xlsx`.

## Personalização

Caso queira rodar a automação mostrando o navegador, basta comentar a linha do modo headless no arquivo `bot/driver.py`:

```python
# chrome_options.add_argument("--headless=new")
```

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Selenium**: Para automação do navegador.
- **openpyxl**: Para leitura e gravação de arquivos Excel.
- **webdriver_manager**: Para gerenciar a versão do ChromeDriver.

## Contribuições

Sinta-se à vontade para contribuir com melhorias e otimizações! Sugestões e pull requests são bem-vindos.

## Licença

Este projeto está licenciado sob os termos da MIT License.
