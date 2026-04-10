from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from src.model.cliente import Cliente


# TODO revisar e validar schemas
class ClienteSchema(BaseModel):
	"""Define como um novo cliente a ser inserido deve ser representado."""

	nome: Optional[str] = "Nome Sobrenome"
	cpf: str = "01234567890"
	email: str = "cliente@exemplo.com"
	data_nascimento: Optional[str] = "01/01/2001"


class ClienteBuscaPorIdSchema(BaseModel):
	"""Define como deve ser a estrutura que representa a busca por id."""

	id: int = 1


class ClienteResumoSchema(BaseModel):
	"""Define a estrutura simplificada de cliente para listagens."""

	id: int = 1
	nome: Optional[str] = "Nome Sobrenome"
	assinatura_id: Optional[int] = 1
	estado_assinatura: Optional[int] = 1


class ListagemClientesSchema(BaseModel):
	"""Define como uma listagem de clientes será retornada."""

	clientes: List[ClienteResumoSchema]


class ClienteViewSchema(BaseModel):
	"""Define como um cliente será retornado em detalhes."""

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


class ClienteDelSchema(BaseModel):
	"""Define como deve ser a estrutura do dado retornado após remoção."""

	mesage: str
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
