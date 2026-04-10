from flask_openapi3 import Tag

from src.model import Session, Cliente
from src.model.cliente import cliente_blueprint
from src.schemas import ClienteBuscaPorIdSchema, ClienteViewSchema, ErrorSchema, apresentar_cliente_detalhado


detalhar_cliente_tag = Tag(name="Detalhar Cliente", description="Operação que detalha um Cliente de id equivalente ao passado na requisição")
@cliente_blueprint.get('/detalhar_cliente', tags=[detalhar_cliente_tag],
                responses={"200": ClienteViewSchema, "400": ErrorSchema, "404": ErrorSchema})
def detalhar_cliente(query: ClienteBuscaPorIdSchema):
    cliente_id = query.id

    session = Session()
    try:
        cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()

        if not cliente:
            return {"error": "Cliente não encontrado"}, 404

        return apresentar_cliente_detalhado(cliente), 200
    finally:
        session.close()