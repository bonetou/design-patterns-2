class Impressao:

    def visita_adicao(self, adicao):
        print('(', end=" ")
        adicao.expressao_esquerda.aceita(self)
        #visita expressao esquerda
        print('+', end=" ")
        adicao.expressao_direita.aceita(self)
        #visita expressao direita
        print(')', end=" ")

    def visita_subtracao(self, subtracao):
        print('(', end=" ")
        subtracao.expressao_esquerda.aceita(self)
        print('-', end=" ")
        subtracao.expressao_direita.aceita(self)
        print(')', end=" ")
    
    def visita_numero(self, numero):
        print(numero.avalia(), end=" ")