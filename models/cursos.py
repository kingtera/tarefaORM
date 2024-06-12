from sqlalchemy import String, Integer, Column, TIMESTAMP, text
from .database import Base

class Cursos(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email_secretaria = Column(String(50), nullable=False)
    ano_fundacao = Column(Integer, nullable=False)
    turmas_formadas = Column(Integer, nullable=False)
    horas_totais = Column(Integer, nullable=False)
    campus = Column(String(50), nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))