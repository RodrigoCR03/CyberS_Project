class DummyModel:
    def __init__(self):
        # Inicialização do modelo (substituível por um modelo real)
        pass

    def predict(self, data: dict) -> str:
        """
        Simula a deteção de anomalias.  
        Se a chave 'anomaly' for True, retorna "Alto risco"; caso contrário, "Baixo risco".
        """
        if data.get("anomaly", False):
            return "Alto risco"
        return "Baixo risco"
