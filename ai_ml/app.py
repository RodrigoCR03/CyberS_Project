from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging
from model.dummy_model import DummyModel

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai_ml")

app = FastAPI(title="Módulo de IA e Machine Learning")

# Instanciação do modelo
model = DummyModel()

# Modelo de entrada para a predição
class PredictionRequest(BaseModel):
    anomaly: bool = False

@app.post("/predict", summary="Realiza predições de risco com base nos dados fornecidos")
async def predict(data: PredictionRequest):
    try:
        result = model.predict(data.dict())
        logger.info("Predição efetuada com sucesso.")
        return {"result": result}
    except Exception as e:
        logger.error("Erro durante a predição: %s", e)
        raise HTTPException(status_code=500, detail="Erro na predição.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
