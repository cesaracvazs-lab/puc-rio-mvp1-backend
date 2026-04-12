from flask_openapi3 import Tag

from src.model import Session, Cliente
from src.model.cliente import cliente_blueprint
from src.schemas import ClienteListarSchema, ErrorSchema, apresentar_lista_clientes


listar_clientes_tag = Tag(name="Listar Cliente", description="Operações que lista todos os Clientes cadastrados no banco de dados")
@cliente_blueprint.get('/listar_clientes', tags=[listar_clientes_tag],
                responses={"200": ClienteListarSchema, "404": ErrorSchema})
def listar_clientes():

    session = Session()
    try:
        lista_clientes = session.query(Cliente).all()
        if not lista_clientes:
            return {"error": "Não há clientes cadastrados"}, 404

        return apresentar_lista_clientes(lista_clientes), 200
    finally:
        session.close()