from sqlalchemy.exc import IntegrityError
from flask_openapi3 import Tag
from datetime import datetime

from src.model import Session, Cliente
from src.model.cliente import cliente_blueprint
from src.schemas import ClienteSchema, ClienteViewSchema, ErrorSchema, apresentar_cliente_detalhado


incluir_cliente_tag = Tag(name="Incluir Cliente", description="Operação que inclui um Cliente no banco de dados")
@cliente_blueprint.post('/incluir_cliente', tags=[incluir_cliente_tag],
                responses={"201": ClienteViewSchema, "400": ErrorSchema})
def incluir_cliente(body: ClienteSchema):

    cpf = body.cpf
    email = body.email
    nome = body.nome
    data_nascimento = body.data_nascimento
    
    if data_nascimento:
        try:
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        except ValueError as e:
            return {"error": "Data inválida" + " [" + str(e) + "]"}, 400
    else:
        data_nascimento = None

    session = Session()
    cliente = Cliente(
        cpf=cpf, 
        email=email, 
        nome=nome, 
        data_nascimento=data_nascimento
    )

    try:
        cliente_cpf = session.query(Cliente).filter(Cliente.cpf == cpf).first()
        if cliente_cpf:
            return {"error": "Já existe cliente com o mesmo CPF cadastrado"}, 400

        cliente_email = session.query(Cliente).filter(Cliente.email == email).first()
        if cliente_email:
            return {"error": "Já existe cliente com o mesmo email cadastrado"}, 400

        session.add(cliente)
        session.commit()
        return apresentar_cliente_detalhado(cliente), 201
    except IntegrityError:
        session.rollback()
        return {"error": "Cliente já cadastrado"}, 400
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()