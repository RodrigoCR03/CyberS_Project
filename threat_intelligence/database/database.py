from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Utilização de SQLite para demonstração (substituir por PostgreSQL para produção)
SQLALCHEMY_DATABASE_URL = "sqlite:///./threat_intelligence.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
