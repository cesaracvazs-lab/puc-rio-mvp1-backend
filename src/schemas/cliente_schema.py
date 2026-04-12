from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from src.model.cliente import Cliente


class ClienteIncluirSchema(BaseModel):
	"""Define as entradas esperadas na inclusão de um cliente em incluir_cliente."""

	nome: Optional[str] = "Nome Sobrenome"
	cpf: str = "01234567890"
	email: str = "cliente@exemplo.com"
	data_nascimento: Optional[str] = "01/01/2001"


class ClienteBuscaPorIdSchema(BaseModel):
	"""Define as entradas esperadas na busca de um cliente por id."""

	id: int = 1


class ClienteAtualizarSchema(BaseModel):
	"""Define as entradas esperadas na atualização de um cliente em atualizar_cliente."""

	id: int = 1
	nome: Optional[str] = None
	email: Optional[str] = None
	data_nascimento: Optional[str] = None
	assinatura_id: Optional[int] = None


class ClienteListadoSchema(BaseModel):
	"""Define o modelo de cliente listado na resposta de listar_clientes."""

	id: int = 1
	nome: Optional[str] = "Nome Sobrenome"
	assinatura_id: Optional[int] = 1
	estado_assinatura: Optional[int] = 1


class ClienteListarSchema(BaseModel):
	"""Define a resposta de listar_clientes."""

	clientes: List[ClienteListadoSchema]


class ClienteDetalharSchema(BaseModel):
	"""Define o modelo de um cliente na resposta de detalhar_cliente."""

	id: int = 1
	cpf: str = "01234567890"
	nome: Optional[str] = "Nome Sobrenome"
	email: str = "cliente@exemplo.com"
	data_nascimento: Optional[str] = "01/01/2001"
	data_cadastro: str = "09/04/2026"
	assinatura_id: Optional[int] = 1
	estado_assinatura: Optional[int] = 1
	ultima_atualizacao_assinatura: Optional[str] = "09/04/2026 12:30:00"
	data_vigencia_assinatura: Optional[str] = "09/05/2026"


class ClienteExcluirSchema(BaseModel):
	"""Define a estrutura da resposta de excluir_cliente."""

	message: str = "Sucesso ao excluir Cliente"
	id: int


def _formata_data(valor: Optional[date]) -> Optional[str]:
	if valor is None:
		return None

	return valor.strftime("%d/%m/%Y")


def _formata_datetime(valor: Optional[datetime]) -> Optional[str]:
	if valor is None:
		return None

	return valor.strftime("%d/%m/%Y %H:%M:%S")


def apresentar_lista_clientes(clientes: List[Cliente]):
	"""Retorna uma representação da listagem de clientes."""

	result = []
	for cliente in clientes:
		result.append({
			"id": cliente.id,
			"nome": cliente.nome,
			"assinatura_id": cliente.assinatura_id,
			"estado_assinatura": cliente.estado_assinatura,
		})

	return {"clientes": result}


def apresentar_cliente_detalhado(cliente: Cliente):
	"""Retorna uma representação detalhada de um cliente."""

	return {
		"id": cliente.id,
		"cpf": cliente.cpf,
		"nome": cliente.nome,
		"email": cliente.email,
		"data_nascimento": _formata_data(cliente.data_nascimento),
		"data_cadastro": _formata_data(cliente.data_cadastro),
		"assinatura_id": cliente.assinatura_id,
		"estado_assinatura": cliente.estado_assinatura,
		"ultima_atualizacao_assinatura": _formata_datetime(cliente.ultima_atualizacao_assinatura),
		"data_vigencia_assinatura": _formata_data(cliente.data_vigencia_assinatura),
	}
