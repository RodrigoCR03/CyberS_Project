# CyberS_Project# CyberNova

## Visão Geral

O **CyberNova** é uma plataforma modular de cibersegurança concebida para oferecer uma solução robusta e escalável, destinada a proteger as infraestruturas e os colaboradores das empresas contra ameaças maliciosas. A solução integra diversos módulos que abrangem funcionalidades críticas, tais como:

- **Inteligência Artificial e Machine Learning (IA/ML):** Para deteção de anomalias e avaliação de riscos.
- **Threat Intelligence Colaborativa:** Para centralização e partilha de indicadores de ameaças.
- **Zero Trust e Microsegmentação:** Para avaliação e controlo do acesso com base em scoring de risco.
- **Orquestração e Automatização de Resposta (SOAR):** Para criação e execução de workflows de resposta a incidentes.
- **Governance, Risk & Compliance (GRC):** Para verificação da conformidade das organizações com normas e regulamentações.
- **Formação e Gamificação:** Para sensibilização e formação dos colaboradores face a ciberameaças.

Cada módulo foi desenvolvido como um microserviço autónomo, utilizando o framework [FastAPI](https://fastapi.tiangolo.com/), e a integração entre os mesmos é gerida através de um API Gateway. A orquestração de todos os serviços é realizada via [Docker Compose](https://docs.docker.com/compose/), o que facilita a escalabilidade e a manutenção da solução.

## Arquitetura do Projeto

A plataforma **CyberNova** adota uma arquitetura baseada em microserviços, onde cada módulo é implementado de forma autónoma e comunica com os restantes através de chamadas REST. A estrutura do projeto encontra-se organizada da seguinte forma:

```
cybernova/
├── docker-compose.yml
├── gateway/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── ai_ml/
│   ├── Dockerfile
│   ├── app.py
│   ├── model/
│   │   └── dummy_model.py
│   └── requirements.txt
├── threat_intelligence/
│   ├── Dockerfile
│   ├── app.py
│   ├── database/
│   │   ├── database.py
│   │   └── models.py
│   └── requirements.txt
├── zero_trust/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── soar/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── grc/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── training/
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
```

### Componentes Principais

1. **Gateway:**  
   - Atua como ponto de entrada único para os utilizadores e sistemas.
   - Implementa um mecanismo simples de autenticação (baseado num token fixo) para proteger os endpoints.
   - Encaminha os pedidos para os restantes microserviços.

2. **Módulo IA/ML:**  
   - Realiza predições baseadas em dados de entrada para determinar o nível de risco (exemplo _dummy_ que pode ser substituído por um modelo real).
  
3. **Threat Intelligence:**  
   - Armazena e disponibiliza indicadores de ameaça utilizando uma base de dados (neste exemplo, SQLite, mas recomendada a utilização de PostgreSQL ou similar para produção).
  
4. **Zero Trust:**  
   - Implementa uma verificação de acesso baseada em um "risk score", negando ou concedendo acesso conforme o nível de risco.
  
5. **SOAR:**  
   - Permite a criação e execução de workflows de resposta a incidentes.
  
6. **GRC:**  
   - Verifica a conformidade de uma organização com normas e regulamentos, de forma simples e direta.
  
7. **Formação e Gamificação:**  
   - Disponibiliza desafios de formação (por exemplo, simulações de phishing) para sensibilização dos colaboradores.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework para criação de APIs assíncronas e de alta performance.
- **[Docker](https://docs.docker.com/):** Para containerização dos microserviços.
- **[Docker Compose](https://docs.docker.com/compose/):** Para orquestração e gestão dos containers.
- **[SQLAlchemy](https://docs.sqlalchemy.org/):** ORM para a gestão de bases de dados.
- **[uvicorn](https://www.uvicorn.org/):** Servidor ASGI para executar as aplicações FastAPI.
- **Logging e Monitorização:** Utilização do módulo `logging` do Python para registar eventos e erros (sugere-se integração com soluções centralizadas para ambientes de produção).

## Instalação e Execução

### Pré-requisitos

- **Docker:** Certifique-se que o Docker se encontra instalado no seu sistema.  
  [Instalação do Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** Necessário para orquestração dos microserviços.  
  [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

### Instruções de Execução

1. **Clone o Repositório:**

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd cybernova
   ```

2. **Construção e Arranque dos Serviços:**

   Execute o comando abaixo na pasta raiz do projeto (onde se encontra o ficheiro `docker-compose.yml`):

   ```bash
   docker-compose up --build
   ```

3. **Acesso aos Endpoints:**

   - **API Gateway:** Disponível em `http://localhost:8000`
   - **Módulo IA/ML:** `http://localhost:8001`
   - **Threat Intelligence:** `http://localhost:8002`
   - **Zero Trust:** `http://localhost:8003`
   - **SOAR:** `http://localhost:8004`
   - **GRC:** `http://localhost:8005`
   - **Formação:** `http://localhost:8006`

## Melhorias Futuras

- **Autenticação e Autorização Avançadas:**  
  Integrar métodos robustos de autenticação, como JWT ou OAuth2.
  
- **Logging Centralizado e Monitorização:**  
  Implementar soluções centralizadas para recolha e análise de logs (ex.: ELK Stack, Prometheus, Grafana).

- **Utilização de Base de Dados Robusta:**  
  Substituir o SQLite por um SGBD mais robusto (ex.: PostgreSQL) para ambientes de produção.

## Licença

Este projeto é disponibilizado sob a [Licença MIT](https://opensource.org/licenses/MIT).
