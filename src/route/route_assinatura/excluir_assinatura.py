from flask_openapi3 import Tag
from sqlalchemy.exc import SQLAlchemyError

from src.model import Session, Assinatura
from src.model.assinatura import assinatura_blueprint
from src.schemas import AssinaturaBuscaSchema, AssinaturaDelSchema, ErrorSchema


excluir_assinatura_tag = Tag(name="Excluir Assinatura", description="Operação que exclui uma Assinatura de id equivalente ao passado na requisição")
@assinatura_blueprint.delete('/excluir_assinatura', tags=[excluir_assinatura_tag],
                responses={"200": AssinaturaDelSchema, "400": ErrorSchema, "404": ErrorSchema, "500": ErrorSchema})
def excluir_assinatura(query: AssinaturaBuscaSchema):

    assinatura_id = query.id

    session = Session()

    try:
        linhas_afetadas = session.query(Assinatura).filter(Assinatura.id == assinatura_id).delete()

        if linhas_afetadas == 0:
            return {"error": "Assinatura não encontrada"}, 404

        session.commit()

        return {"message": "Sucesso ao excluir Assinatura", "id": assinatura_id}, 200

    except SQLAlchemyError:
        session.rollback()
        return {"error": "Erro interno ao excluir assinatura"}, 500
    finally:
        session.close()
