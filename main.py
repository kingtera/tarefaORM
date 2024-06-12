from fastapi import FastAPI
# from typing import Optional
from routers.cursos import router as router_cursos
from models.database import engine
# from models.cursos import Cursos
from models.cursos import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_cursos)