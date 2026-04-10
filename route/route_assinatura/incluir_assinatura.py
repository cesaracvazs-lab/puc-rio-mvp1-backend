from sqlalchemy.exc import IntegrityError
from flask_openapi3 import Tag

from model import Session, Assinatura
from model.assinatura import assinatura_blueprint
from schemas import AssinaturaSchema, AssinaturaViewSchema, ErrorSchema, apresentar_detalhar_assinatura


incluir_assinatura_tag = Tag(name="Incluir Assinatura", description="Operação que inclui uma Assinatura no banco de dados")
@assinatura_blueprint.post('/incluir_assinatura', tags=[incluir_assinatura_tag],
                responses={"201": AssinaturaViewSchema, "400": ErrorSchema})
def incluir_assinatura(body: AssinaturaSchema):

    session = Session()
    assinatura = Assinatura(
        nome=body.nome,
        valor_mensal=body.valor_mensal,
    )

    try:
        session.add(assinatura)
        session.commit()
        return apresentar_detalhar_assinatura(assinatura), 201
    except IntegrityError:
        session.rollback()
        return {"error": "Assinatura já cadastrada"}, 400
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()