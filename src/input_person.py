class InputPerson:
    def __init__(self, row: tuple):
        self.cpf, self.birth_date = row
    
    def formatted_cpf(self) -> str | None:
        if self.cpf:
            return self.cpf.replace('.', '').replace('-', '')

        return None
    
    def formatted_birth_date(self) -> str | None:
        if self.birth_date:
            if isinstance(self.birth_date, str):
                return self.birth_date

            return self.birth_date.strftime('%d/%m/%Y')
        
        return None
