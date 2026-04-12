from flask_openapi3 import Tag

from src.model import Session, Assinatura
from src.model.assinatura import assinatura_blueprint
from src.schemas import AssinaturaListarSchema, ErrorSchema, apresentar_lista_assinaturas


listar_assinatura_tag = Tag(name="Listar Assinaturas", description="Operações que lista todas as assinaturas cadastradas no banco de dados")
@assinatura_blueprint.get('/listar_assinaturas', tags=[listar_assinatura_tag],
                responses={"200": AssinaturaListarSchema, "404": ErrorSchema})
def listar_assinaturas():

    session = Session()
    try:
        lista_assinaturas = session.query(Assinatura).all()
        if not lista_assinaturas:
            return {"error": "Não ha assinaturas cadastradas"}, 404

        return apresentar_lista_assinaturas(lista_assinaturas), 200
    finally:
        session.close()