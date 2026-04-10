from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL
from decimal import Decimal

from src.model import Base


class ProgramaFidelidade(Base):
    __tablename__ = 'programa_fidelidade'
    
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
    nome = Column(VARCHAR(200), nullable=False)
    meses_assinatura_ativa = Column('meses_assinatura_ativa', INTEGER, nullable=False)
    porcentagem_desconto = Column('porcentagem_desconto', DECIMAL(5,2), nullable=False)

    def __init__(self, nome:str, meses_assinatura_ativa:int, porcentagem_desconto:Decimal):
        self.nome = nome
        self.meses_assinatura_ativa = meses_assinatura_ativa
        self.porcentagem_desconto = porcentagem_desconto