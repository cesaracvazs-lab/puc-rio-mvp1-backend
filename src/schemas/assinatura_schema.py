from datetime import date
from decimal import Decimal
from typing import List

from pydantic import BaseModel

from src.model.assinatura import Assinatura


class AssinaturaBuscaPorIdSchema(BaseModel):
	"""Define as entradas esperadas na busca de uma assinatura por id."""

	id: int = 1


class AssinaturaListadoSchema(BaseModel):
	"""Define o modelo de assinatura listada na resposta de listar_assinaturas."""

	id: int = 1
	nome: str = "Premium"
	valor_mensal: Decimal = Decimal("99.99")


class AssinaturaListarSchema(BaseModel):
	"""Define a resposta de listar_assinaturas."""

	assinaturas: List[AssinaturaListadoSchema]


class AssinaturaDetalharSchema(BaseModel):
	"""Define o modelo de uma assinatura na resposta de detalhar_assinatura."""

	id: int = 1
	nome: str = "Premium"
	valor_mensal: Decimal = Decimal("99.99")
	data_cadastro: str = "09/04/2026"


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


def apresentar_assinatura_detalhada(assinatura: Assinatura):
	"""Retorna uma representação detalhada da assinatura."""

	return {
		"id": assinatura.id,
		"nome": assinatura.nome,
		"valor_mensal": assinatura.valor_mensal,
		"data_cadastro": _formata_data(assinatura.data_cadastro),
	}
