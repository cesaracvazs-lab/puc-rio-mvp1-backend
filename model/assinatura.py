from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL, DATE
from flask_openapi3 import APIBlueprint
from decimal import Decimal
from datetime import date

from model import Base


assinatura_blueprint = APIBlueprint('assinatura', __name__)

class Assinatura(Base):
    __tablename__ = 'assinatura'
    
    # TODO documentação
    """
    Cria um Produto

    Arguments:
        nome: nome do produto.
        quantidade: quantidade que se espera comprar daquele produto
        valor: valor esperado para o produto
        data_insercao: data de quando o produto foi inserido à base
    """

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    nome = Column(VARCHAR(200), unique=True, nullable=False)
    valor_mensal = Column('valor_mensal', DECIMAL(10,2), nullable=False)
    data_cadastro = Column('data_cadastro', DATE, nullable=False)

    def __init__(self, nome:str, valor_mensal:Decimal):
        self.nome = nome
        self.valor_mensal = valor_mensal
        self.data_cadastro = date.today()