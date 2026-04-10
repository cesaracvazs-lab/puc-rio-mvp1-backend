from sqlalchemy import Column, INTEGER, VARCHAR, DATE, DATETIME, ForeignKey
from flask_openapi3 import APIBlueprint
from datetime import date

from model import Base


cliente_blueprint = APIBlueprint('cliente', __name__)

# TODO validacoes de entrada
class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    cpf = Column(VARCHAR(11), unique=True, nullable=False)
    email = Column(VARCHAR(300), unique=True, nullable=False)
    nome = Column(VARCHAR(100))
    data_nascimento = Column('data_nascimento', DATE)
    assinatura_id = Column('assinatura_id', INTEGER, ForeignKey('assinatura.id'))
    estado_assinatura = Column('estado_assinatura', INTEGER)
    ultima_atualizacao_assinatura = Column('ultima_atualizacao_assinatura', DATETIME)
    data_vigencia_assinatura = Column('data_vigencia_assinatura', DATE)
    data_cadastro = Column('data_cadastro', DATE, nullable=False)

    def __init__(self, cpf:str, email:str, nome:str = None, data_nascimento:date = None):
        # TODO documentação
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        
        self.cpf = cpf
        self.email = email
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.data_cadastro = date.today()