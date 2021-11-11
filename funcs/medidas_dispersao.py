from funcs.auxiliares import Auxiliares
from statistics import *

class MedidasDispersao:
    # Recebe um vetor com os dados de uma amostra e gera:
    # Medidas de variabilidade:
    #  - variancia
    #  - desvio padrao
    #  - coeficiente de variabilidade

    def __variancia(self, dados):
        # Variancia dos valores.
        # ENTRADAS:
        #   dados   - vetor com todos os valores de mesmo atributo
        return variance(dados)

    def __desvio_padrao_amostral(self, dados):
        # Raiz da variancia.
        # ENTRADAS:
        #   dados   - vetor com todos os valores de mesmo atributo
        return stdev(dados)

    def __coeficiente_variabilidade(self, dados):
        # Um coeficiente que nos permite comparar a variabilidade entre
        # atributos/grandezas diferentes.
        # ENTRADAS:
        #   dados   - vetor com todos os valores de mesmo atributo
        dp = self.__desvio_padrao_amostral(dados)
        media = mean(dados)
        return dp/media

    def __format_number(self, value):
        aux = Auxiliares()

        return aux.format_number(value)

    def builder(self, dados):
        v = self.__variancia(dados)
        dpa = self.__desvio_padrao_amostral(dados)
        cv = self.__coeficiente_variabilidade(dados)

        v = self.__format_number(v)
        dpa = self.__format_number(dpa)
        cv = self.__format_number(cv)

        print("Variância: {0}".format(v))
        print("Desvio Padrão: {0}".format(dpa))
        print("Coeficiente de Variabilidade: {0}".format(cv))