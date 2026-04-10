from flask_openapi3 import Tag

from model import Session, Assinatura
from model.assinatura import assinatura_blueprint
from schemas import ListagemAssinaturasSchema, ErrorSchema, apresentar_lista_assinaturas


listar_assinatura_tag = Tag(name="Listar Assinaturas", description="Operações que lista todas as assinaturas cadastradas no banco de dados")
@assinatura_blueprint.get('/listar_assinaturas', tags=[listar_assinatura_tag],
                responses={"200": ListagemAssinaturasSchema, "404": ErrorSchema})
def listar_assinaturas():

    session = Session()
    try:
        lista_assinaturas = session.query(Assinatura).all()
        if not lista_assinaturas:
            return {"message": "Não há assinaturas cadastradas"}, 404

        return apresentar_lista_assinaturas(lista_assinaturas), 200
    finally:
        session.close()