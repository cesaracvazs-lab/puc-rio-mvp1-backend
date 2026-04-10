from flask_openapi3 import Tag

from model import Session, Assinatura
from model.assinatura import assinatura_blueprint
from schemas import AssinaturaBuscaSchema, AssinaturaViewSchema, ErrorSchema, apresentar_detalhar_assinatura as apresentar_assinatura_detalhada


detalhar_assinatura_tag = Tag(name="Detalhar Assinatura", description="Operação que detalha uma Assinatura de id equivalente ao passado na requisição")
@assinatura_blueprint.get('/detalhar_assinatura', tags=[detalhar_assinatura_tag],
                responses={"200": AssinaturaViewSchema, "400": ErrorSchema, "404": ErrorSchema})
def detalhar_assinatura(query: AssinaturaBuscaSchema):
    assinatura_id = query.id

    session = Session()
    try:
        assinatura = session.query(Assinatura).filter(Assinatura.id == assinatura_id).first()

        if not assinatura:
            return {"message": "Assinatura não encontrada"}, 404

        return apresentar_assinatura_detalhada(assinatura), 200
    finally:
        session.close()