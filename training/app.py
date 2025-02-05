from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("training")

app = FastAPI(title="Módulo de Formação e Gamificação")

# Modelo Pydantic para um desafio de formação
class Challenge(BaseModel):
    id: int
    title: str
    description: str

@app.get("/training/challenge", summary="Obtém um desafio de formação", response_model=Challenge)
def get_training_challenge():
    try:
        challenge = {
            "id": 1,
            "title": "Simulação de Phishing",
            "description": "Identifique o email suspeito e indique os sinais de alerta."
        }
        logger.info("Desafio de formação recuperado com sucesso.")
        return challenge
    except Exception as e:
        logger.error("Erro ao recuperar desafio de formação: %s", e)
        raise HTTPException(status_code=500, detail="Erro ao recuperar desafio de formação.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8006)
