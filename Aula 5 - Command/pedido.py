from abc import ABCMeta, abstractmethod
from datetime import date

class Pedido:

	def __init__(self, cliente, valor):
		self.__cliente = cliente
		self.__valor = valor
		self.__status = 'NOVO'
		self.__data_finalizacao = None

	def paga(self):
		self.__status = 'PAGO'

	def finaliza(self):
		self.__data_finalizacao = date.today()
		self.__status = 'ENTREGUE'

	@property
	def cliente(self):
		return self.__cliente

	@property
	def cliente(self):
		return self.__cliente

	@property
	def status(self):
		return self.__status

	@property
	def data_finalizacao(self):
		return self.__data_finalizacao


class Comando:

	__metaclass__ = ABCMeta

	@abstractmethod
	def executa(self):
		pass

class ConcluiPedido(Comando):

	def __init__(self, pedido):
		self.__pedido = pedido

	def executa(self):
		self.__pedido.finaliza()

class PagaPedido(Comando):

	def __init__(self, pedido):
		self.__pedido = pedido

	def executa(self):
		self.__pedido.paga()

class FilaDeTrabalho:

	def __init__(self):
		self.__comandos = []

	def adiciona(self, comando):
		self.__comandos.append(comando)

	def processa(self):
		for comando in self.__comandos:
			comando.executa()

if __name__ == '__main__':

	pedido1 = Pedido('Flávio', 200)
	pedido2 = Pedido('Almeida', 400)

	fila_de_trabalho = FilaDeTrabalho()

	comando1 = ConcluiPedido(pedido1)
	comando2 = PagaPedido(pedido1)
	comando3 = ConcluiPedido(pedido2)

	print(pedido1.status)
	print(pedido2.status)
	fila_de_trabalho.adiciona(comando1)
	fila_de_trabalho.adiciona(comando2)
	fila_de_trabalho.adiciona(comando3)

	fila_de_trabalho.processa()
	print(pedido1.status)
	print(pedido2.status)