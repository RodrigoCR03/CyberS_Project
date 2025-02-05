from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import uvicorn
import logging
from database.database import SessionLocal, engine
from database import models

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("threat_intelligence")

# Criação das tabelas na base de dados, se ainda não existirem
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Módulo de Threat Intelligence")

# Modelo Pydantic para validação dos dados de ameaça
class ThreatSchema(BaseModel):
    indicator: str
    description: str = None

    class Config:
        orm_mode = True

@app.post("/threats/", summary="Adiciona um novo indicador de ameaça")
def add_threat(threat: ThreatSchema):
    db: Session = SessionLocal()
    try:
        db_threat = models.Threat(**threat.dict())
        db.add(db_threat)
        db.commit()
        db.refresh(db_threat)
        logger.info("Indicador adicionado: %s", db_threat.indicator)
        return db_threat
    except Exception as e:
        logger.error("Erro ao adicionar indicador: %s", e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao adicionar indicador.")
    finally:
        db.close()

@app.get("/threats/", summary="Lista todos os indicadores de ameaça")
def get_threats():
    db: Session = SessionLocal()
    try:
        threats = db.query(models.Threat).all()
        logger.info("Indicadores recuperados com sucesso.")
        return threats
    except Exception as e:
        logger.error("Erro ao recuperar indicadores: %s", e)
        raise HTTPException(status_code=500, detail="Erro ao recuperar indicadores.")
    finally:
        db.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
