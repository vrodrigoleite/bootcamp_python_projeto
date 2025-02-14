# A única responsabilidade é mapear a estrutura do modelo (é agnóstico ao banco de dados)
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ProductModel(Base):
    __tablename__ = "products"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())