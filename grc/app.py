from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("grc")

app = FastAPI(title="Módulo GRC")

# Modelo Pydantic para dados da organização
class Organization(BaseModel):
    name: str
    compliance: bool

@app.post("/compliance/", summary="Verifica a conformidade de uma organização")
def check_compliance(org: Organization):
    try:
        if org.compliance:
            logger.info("Organização '%s' em conformidade.", org.name)
            return {"compliant": True, "message": "Conformidade verificada."}
        else:
            logger.info("Organização '%s' não está em conformidade.", org.name)
            return {"compliant": False, "message": "Organização não está em conformidade."}
    except Exception as e:
        logger.error("Erro na verificação de conformidade: %s", e)
        raise HTTPException(status_code=500, detail="Erro na verificação de conformidade.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
