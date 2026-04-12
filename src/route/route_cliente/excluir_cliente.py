from flask_openapi3 import Tag
from sqlalchemy.exc import SQLAlchemyError

from src.model import Session, Cliente
from src.model.cliente import cliente_blueprint
from src.schemas import ClienteBuscaPorIdSchema, ClienteExcluirSchema, ErrorSchema


excluir_cliente_tag = Tag(name="Excluir Cliente", description="Operação que exclui um Cliente de id equivalente ao passado na requisição")
@cliente_blueprint.delete('/excluir_cliente', tags=[excluir_cliente_tag],
                responses={"200": ClienteExcluirSchema, "400": ErrorSchema, "404": ErrorSchema, "500": ErrorSchema})
def excluir_cliente(query: ClienteBuscaPorIdSchema):

    cliente_id = query.id

    session = Session()

    try:
        linhas_afetadas = session.query(Cliente).filter(Cliente.id == cliente_id).delete()

        if linhas_afetadas == 0:
            return {"error": "Cliente não encontrado"}, 404

        session.commit()

        return {"message": "Sucesso ao excluir Cliente", "id": cliente_id}, 200

    except SQLAlchemyError:
        session.rollback()
        return {"error": "Erro interno ao excluir cliente"}, 500
    finally:
        session.close()
    