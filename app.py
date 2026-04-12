from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from flask import redirect

from src.model.cliente import cliente_blueprint
from src.model.assinatura import assinatura_blueprint

# rotas de Cliente
import src.route.route_cliente.incluir_cliente
import src.route.route_cliente.listar_clientes
import src.route.route_cliente.detalhar_cliente
import src.route.route_cliente.excluir_cliente
import src.route.route_cliente.atualizar_cliente

# rotas de Assinatura
import src.route.route_assinatura.incluir_assinatura
import src.route.route_assinatura.listar_assinaturas
import src.route.route_assinatura.detalhar_assinatura
import src.route.route_assinatura.excluir_assinatura


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