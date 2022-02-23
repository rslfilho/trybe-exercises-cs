from abc import ABC, abstractmethod


class TaxStrategy(ABC):
    @classmethod
    @abstractmethod
    def calc(cls, valor):
        raise NotImplementedError


class ISS(TaxStrategy):
    @classmethod
    def calc(cls, valor):
        return valor * 0.1


class ICMS(TaxStrategy):
    @classmethod
    def calc(cls, valor):
        return valor * 0.06


class PIS(TaxStrategy):
    @classmethod
    def calc(cls, valor):
        return valor * 0.0065


class COFINS(TaxStrategy):
    @classmethod
    def calc(cls, valor):
        return valor * 0.03


class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_imposto(self, tax):
        return tax.calc(self.valor)


orcamento = Orcamento(1000)
print(f"ISS: {orcamento.calcular_imposto(ISS)}")
print(f"ICMS: {orcamento.calcular_imposto(ICMS)}")
print(f"PIS: {orcamento.calcular_imposto(PIS)}")
print(f"COFINS: {orcamento.calcular_imposto(COFINS)}")
