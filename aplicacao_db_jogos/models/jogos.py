from models.base import Base
from sqlalchemy import Column, Integer, String, Float

class Jogos(Base):

    # Nome da tabela
    __tablename__ = "Jogos"

    # Colunas
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    plataforma = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)