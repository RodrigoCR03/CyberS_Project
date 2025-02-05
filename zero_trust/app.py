from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("zero_trust")

app = FastAPI(title="Módulo de Zero Trust e Microsegmentação")

# Modelo Pydantic para o pedido de acesso
class AccessRequest(BaseModel):
    risk_score: int

@app.post("/access/", summary="Verifica o acesso com base no scoring de risco")
def check_access(request: AccessRequest):
    try:
        if request.risk_score > 5:
            logger.info("Acesso negado (risk_score=%d).", request.risk_score)
            return {"access": "denied", "message": "Risco elevado detectado."}
        logger.info("Acesso concedido (risk_score=%d).", request.risk_score)
        return {"access": "granted", "message": "Acesso concedido."}
    except Exception as e:
        logger.error("Erro na verificação de acesso: %s", e)
        raise HTTPException(status_code=500, detail="Erro na verificação de acesso.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
