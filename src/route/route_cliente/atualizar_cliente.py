from datetime import date, datetime, timedelta

from flask_openapi3 import Tag

from src.model import Session, Cliente, Assinatura
from src.model.cliente import cliente_blueprint
from src.enum.estado_assinatura import EstadoAssinatura
from src.schemas import ClienteAtualizarSchema, ClienteDetalharSchema, ErrorSchema, apresentar_cliente_detalhado


atualizar_cliente_tag = Tag(name="Atualizar Cliente", description="Operação que atualiza campos de um Cliente")
@cliente_blueprint.patch('/atualizar_cliente', tags=[atualizar_cliente_tag],
                responses={"200": ClienteDetalharSchema, "400": ErrorSchema, "404": ErrorSchema})
def atualizar_cliente(body: ClienteAtualizarSchema):    

    session = Session()
    try:
        cliente = session.query(Cliente).filter(Cliente.id == body.id).first()

        if not cliente:
            return {"error": "Cliente não encontrado"}, 404

        campos_enviados = body.model_fields_set

        if 'nome' in campos_enviados and body.nome:
            cliente.nome = body.nome

        if 'email' in campos_enviados and body.email:
            cliente.email = body.email

        if 'assinatura_id' in campos_enviados and body.assinatura_id is not None:
            assinatura = session.query(Assinatura).filter(Assinatura.id == body.assinatura_id).first()
            if not assinatura:
                return {"error": "Assinatura não encontrada"}, 404

            cliente.assinatura_id = body.assinatura_id
            cliente.estado_assinatura = EstadoAssinatura.ATIVO
            cliente.ultima_atualizacao_assinatura = datetime.now()
            cliente.data_vigencia_assinatura = date.today() + timedelta(days=365)

        if 'data_nascimento' in campos_enviados:
            if body.data_nascimento:
                try:
                    cliente.data_nascimento = datetime.strptime(body.data_nascimento, '%d/%m/%Y').date()
                except ValueError as e:
                    return {"error": "Data de nascimento inválida" + " [" + str(e) + "]"}, 400
            else:
                cliente.data_nascimento = None

        if len(campos_enviados - {'id'}) == 0:
            return {"error": "Nenhum campo permitido para atualização foi enviado"}, 400

        session.commit()

        return apresentar_cliente_detalhado(cliente), 200

    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()