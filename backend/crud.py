from sqlalchemy.orm import Session
from schema import ProductUpdate, ProductCreate
from models import ProductModel


def get_product(db: Session, product_id: int):
    """
    Função que recebe um id e retorna somente ele
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session):
    """
    Função que retorna todos os elementos
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    """
    Função que insere um produto na base de dados
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Função que deleta um produto da base de dados.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Função que atualiza um produto no banco de dados.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    # Verifica se o produto existe
    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product