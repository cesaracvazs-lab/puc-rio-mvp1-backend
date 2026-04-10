from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError

from model import Session
from logger import logger
from schemas import *

from model.cliente import cliente_blueprint
from model.assinatura import assinatura_blueprint

import route.route_cliente.incluir_cliente
import route.route_cliente.listar_clientes
import route.route_cliente.detalhar_cliente
import route.route_cliente.excluir_cliente

import route.route_assinatura.incluir_assinatura
import route.route_assinatura.listar_assinaturas
import route.route_assinatura.detalhar_assinatura
import route.route_assinatura.excluir_assinatura


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
app.json.sort_keys = False
CORS(app)

#Blueprint das rotas implementadas
app.register_api(cliente_blueprint)
app.register_api(assinatura_blueprint)


@app.route('/', methods=['GET'])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')