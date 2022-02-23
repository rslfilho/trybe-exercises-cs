class Hospede:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Quarto:
    def __init__(self, numero, andar, qtd_hospedes, preco):
        self.numero = numero
        self.andar = andar
        self.qtd_hospedes = qtd_hospedes
        self.preco = preco
        self.reservado = False


class Reserva:
    def __init__(self, quarto, hospede):
        self.quarto = quarto
        self.hospede = hospede


class Hotel:
    def __init__(self, nome, quartos, reservas):
        self.quartos = quartos
        self.reservas = reservas

    def quartos_disponiveis(self, qtde):
        disponiveis = [
            quarto
            for quarto in self.quartos
            if quarto.qtd_hospedes >= qtde and quarto.reservado is False
        ]
        return disponiveis.sort()

    def check_in(self, *hospedes):
        try:
            quarto = self.quartos_disponiveis(len(hospedes))[0]
        except (IndexError):
            raise IndexError('Não há quartos disponíveis')
        else:
            quarto.reservado = True
            for hospede in hospedes:
                self.reservas.append(Reserva(quarto, hospede))

    def check_out(self, quarto):
        quarto.reservado = False
        self.reservas = [
            reserva
            for reserva in self.reservas
            if reserva.quarto != quarto
        ]
