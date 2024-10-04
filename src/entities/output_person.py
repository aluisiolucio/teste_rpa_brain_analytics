from dataclasses import dataclass
from typing import Optional

@dataclass
class OutputPerson:
    name: Optional[str]
    cpf: Optional[str]
    birth_date: Optional[str]
    registration_status: Optional[str]
    registration_date: Optional[str]
    message: Optional[str]
