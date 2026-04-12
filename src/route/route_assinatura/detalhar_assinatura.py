from flask_openapi3 import Tag

from src.model import Session, Assinatura
from src.model.assinatura import assinatura_blueprint
from src.schemas import AssinaturaBuscaPorIdSchema, AssinaturaDetalharSchema, ErrorSchema, apresentar_assinatura_detalhada


detalhar_assinatura_tag = Tag(name="Detalhar Assinatura", description="Operação que detalha uma Assinatura de id equivalente ao passado na requisição")
@assinatura_blueprint.get('/detalhar_assinatura', tags=[detalhar_assinatura_tag],
                responses={"200": AssinaturaDetalharSchema, "400": ErrorSchema, "404": ErrorSchema})
def detalhar_assinatura(query: AssinaturaBuscaPorIdSchema):
    assinatura_id = query.id

    session = Session()
    try:
        assinatura = session.query(Assinatura).filter(Assinatura.id == assinatura_id).first()

        if not assinatura:
            return {"error": "Assinatura nao encontrada"}, 404

        return apresentar_assinatura_detalhada(assinatura), 200
    finally:
        session.close()