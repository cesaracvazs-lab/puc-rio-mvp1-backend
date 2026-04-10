from datetime import date
from decimal import Decimal
from typing import List

from pydantic import BaseModel

from src.model.assinatura import Assinatura


# TODO revisar e validar schemas
class AssinaturaSchema(BaseModel):
	"""Define como uma nova assinatura a ser inserida deve ser representada."""

	nome: str = "Premium"
	valor_mensal: Decimal = Decimal("99.99")


class AssinaturaBuscaSchema(BaseModel):
	"""Define como deve ser a estrutura que representa a busca por id."""

	id: int = 1


class AssinaturaResumoSchema(BaseModel):
	"""Define a estrutura simplificada de assinatura para listagens."""

	id: int = 1
	nome: str = "Premium"
	valor_mensal: Decimal = Decimal("99.99")


class ListagemAssinaturasSchema(BaseModel):
	"""Define como uma listagem de assinaturas será retornada."""

	assinaturas: List[AssinaturaResumoSchema]


class AssinaturaViewSchema(BaseModel):
	"""Define como uma assinatura será retornada em detalhes."""

	id: int = 1
	nome: str = "Premium"
	valor_mensal: Decimal = Decimal("99.99")
	data_cadastro: str = "09/04/2026"


class AssinaturaDelSchema(BaseModel):
	"""Define como deve ser a estrutura do dado retornado após remoção."""

	mesage: str
	id: int


def _formata_data(valor: date) -> str:
	return valor.strftime("%d/%m/%Y")


def apresentar_lista_assinaturas(assinaturas: List[Assinatura]):
	"""Retorna uma representação da listagem de assinaturas."""

	result = []
	for assinatura in assinaturas:
		result.append({
			"id": assinatura.id,
			"nome": assinatura.nome,
			"valor_mensal": assinatura.valor_mensal,
		})

	return {"assinaturas": result}


def apresentar_detalhar_assinatura(assinatura: Assinatura):
	"""Retorna uma representação detalhada da assinatura."""

	return {
		"id": assinatura.id,
		"nome": assinatura.nome,
		"valor_mensal": assinatura.valor_mensal,
		"data_cadastro": _formata_data(assinatura.data_cadastro),
	}
