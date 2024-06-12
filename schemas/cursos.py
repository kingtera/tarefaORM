from pydantic import BaseModel

class Curso(BaseModel):
    nome: str
    email_secretaria: str
    ano_fundacao: int
    turmas_formadas: int
    horas_totais: int
    campus: str