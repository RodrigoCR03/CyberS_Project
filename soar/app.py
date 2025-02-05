from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("soar")

app = FastAPI(title="Módulo SOAR")

# Armazenamento em memória para workflows (utilizar base de dados em produção)
workflows = {}

# Modelo Pydantic para definição de workflow
class Workflow(BaseModel):
    name: str
    steps: list

@app.post("/workflow/", summary="Cria um novo workflow de resposta a incidentes")
def create_workflow(workflow: Workflow):
    try:
        workflow_id = len(workflows) + 1
        workflows[workflow_id] = workflow.dict()
        logger.info("Workflow criado com ID: %d", workflow_id)
        return {"workflow_id": workflow_id, "status": "criado"}
    except Exception as e:
        logger.error("Erro ao criar workflow: %s", e)
        raise HTTPException(status_code=500, detail="Erro ao criar workflow.")

@app.post("/workflow/{workflow_id}/execute", summary="Executa o workflow especificado")
def execute_workflow(workflow_id: int):
    try:
        workflow = workflows.get(workflow_id)
        if not workflow:
            logger.warning("Workflow não encontrado: %d", workflow_id)
            raise HTTPException(status_code=404, detail="Workflow não encontrado")
        logger.info("Executando workflow ID: %d", workflow_id)
        # Lógica dummy de execução – implementar lógica real conforme requisitos
        return {"workflow_id": workflow_id, "status": "executado"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Erro ao executar workflow: %s", e)
        raise HTTPException(status_code=500, detail="Erro ao executar workflow.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
