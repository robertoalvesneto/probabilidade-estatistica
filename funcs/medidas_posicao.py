from funcs.auxiliares import Auxiliares
from statistics import *

class MedidasPosicao:
    # Recebe um vetor com os dados de uma amostra e gera:
    # Medidas de posicao:
    #  - media
    #  - mediana
    #  - moda
    
    def __media(self, dados):
        # Media aritmetica dos valores.
        # ENTRADAS:
        #   dados   - vetor com todos os valores de mesmo atributo
        return mean(dados)

    def __mediana(self, dados):
        # Valor central.
        # ENTRADAS:
        #   dados   - vetor com todos os valores de mesmo atributo
        return median(dados)

    def __moda(self, dados):
        # Valor que mais se repete.
        # ENTRADAS:
        #   dados   - vetor com todos os valores de mesmo atributo
        return mode(dados)

    def __format_number(self, value):
        aux = Auxiliares()

        return aux.format_number(value)

    def builder(self, dados):
        media = self.__media(dados)
        mediana = self.__mediana(dados)
        moda = self.__moda(dados)

        media = self.__format_number(media)
        mediana = self.__format_number(mediana)
        moda = self.__format_number(moda)

        print("Media: {0}".format(media))
        print("Mediana: {0}".format(mediana))
        print("Moda: {0}".format(moda))