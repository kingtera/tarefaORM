from fastapi import APIRouter, Depends
from schemas.cursos import Curso
from models.database  import get_db
from models.cursos    import Cursos
from sqlalchemy.orm   import Session
from datetime import datetime


router = APIRouter()

@router.get("/cursos")
async def root():
    return {"mensagem": "Dentro de cursos"}

@router.post("/cursos")
async def criar_curso(curso: Curso, db: Session = Depends(get_db)):
    novo_curso = Cursos(**curso.model_dump())

    ano_atual = datetime.now().year
    if novo_curso.ano_fundacao < 1800 or novo_curso.ano_fundacao > ano_atual:
        print("valor errado")
        raise ValueError('Ano de fundacao deve ser entre 1800 e o ano atual')
    
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return { "mensagem": "Curso criado com sucesso",
             "curso": novo_curso 
    }