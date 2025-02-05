from fastapi import FastAPI, Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import uvicorn
import logging
from pydantic import BaseModel

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gateway")

app = FastAPI(title="CyberNova API Gateway")

# Definição de um token fixo para demonstração (em produção, utilizar um sistema robusto de gestão de tokens)
API_KEY = "secrettoken123"
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token inválido ou em falta."
        )

# Endereços dos microserviços
SERVICES = {
    "ai_ml": "http://ai_ml:8001",
    "threat_intelligence": "http://threat_intelligence:8002",
    "zero_trust": "http://zero_trust:8003",
    "soar": "http://soar:8004",
    "grc": "http://grc:8005",
    "training": "http://training:8006",
}

@app.get("/", summary="Endpoint raiz do Gateway", dependencies=[Depends(verify_token)])
async def root():
    return {"message": "Bem-vindo ao CyberNova API Gateway"}

# Modelo de entrada para o endpoint de predição
class PredictionRequest(BaseModel):
    anomaly: bool = False

@app.post("/predict", summary="Realiza predições via módulo de IA/ML", dependencies=[Depends(verify_token)])
async def predict(data: PredictionRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{SERVICES['ai_ml']}/predict", json=data.dict())
            response.raise_for_status()
            logger.info("Pedido de predição encaminhado com sucesso.")
            return response.json()
    except httpx.HTTPError as e:
        logger.error("Erro ao contactar o serviço de IA/ML: %s", e)
        raise HTTPException(status_code=502, detail="Gateway inválido: impossível contactar o serviço de IA/ML.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
