import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad

from math import sqrt, pow, e

from funcs.analise_combinatoria import AnaliseCombinatoria

class Estatistica:
    # Recebe um vetor com os dados de uma amostra e gera:
    # Correlacao de probabilidade de eventos:
    #  - independencia
    #  - complementar
    #  - mutuamente exclusivo
    #  - condicional

    def __init__(self):
        self.ac = AnaliseCombinatoria()

    def evento_independente(self, eventoA, eventoB):
        # Probabilidade de A e B acontecerem sendo que um nao depende do
        # outro.
        # ENTRADA:
        #   eventoA     - probabilidade de A
        #   eventoB     - probabilidade de B
        return eventoA*eventoB

    def evento_complementar(self, eventoA):
        # O resto da probabilidade da amostra que não engloba o evento A
        # ENTRADA:
        #   eventoA     - probabilidade de A
        return 1 - eventoA

    def evento_mutuamente_exclusivo(self, eventoA, eventoB):
        # Ou um evento acontece, ou o outro.
        # ENTRADA:
        #   eventoA     - probabilidade de A
        #   eventoB     - probabilidade de B
        return eventoA + eventoB

    def evento_condicional(self, intersecaoAB, eventoB):
        # Probabilidade de A ocorrer dado que B ja ocorreu.
        # FORMULA:
        #   P(A|B) = P(intersecao(A,B))/P(B)
        #
        # ENTRADA:
        #   intersecaoAB    - probabilidade da intersecao de A com B
        #   eventoB         - probabilidade de B
        return intersecaoAB/eventoB

    def probabilidade_total(self, eventosA, intersecoesAB):
        # Diz a probabilidade de um evento B acontecer sabendo que a
        # amostra esta dividida em N eventos Ai (0 <= i <= N).
        # FORMULA:
        #   P(B) = Somatorio(P(Ai)*P(B|Ai))
        #  
        # ENTRADAS:
        # dados em probabilidade
        # len(A) == len(AB)
        #   eventosA    - todos os eventos A que subdividem a amostra
        #   eventoB     - evento 'externo' que queremos saber se ocorreu
        pt = 0
        for i in range(len(eventosA)):
            pt += eventosA[i]*intersecoesAB[i]

        return pt

    def teorema_bayes(self, eventoA, eventoB, prob_total):
        # Probabilidade de um evento Ai ocorrer sabendo que B ocorreu.
        # Leva em consideração a probabilidade total.
        # ENTRADAS:
        # dados em probabilidade
        #   eventoA     - quem nos queremos saber se ocorre
        #   eventoB     - o que sabemos que ja ocorreu
        #   prob_total  - probabilidade total de ter ocorrido B
        numerador = self.evento_independente(eventoA, eventoB)

        return self.evento_condicional(numerador, prob_total)

    # Medidas de dispersao e posicao com base em eventos e probabilidade.
    def media(self, e, p):
        return e*p
    
    def variancia(self, e, p):
        return self.media(e*e, p) - pow(self.media(e, p), 2)
    
    def desvio_padrao(self, e, p):
        return sqrt(self.variancia(e, p))
    # Fim medidas.

    def distribuicao_binominal(self, n=0, k=0, p=0):
        # A probabilidade de um evento ocorrer sucessivas vezes sendo que a
        # ocorrencia de uma vez não interfere na ocorrencia nas demais e o
        # fenomeno pode ser dividido entre 'sim' e nao', sucesso e falha.
        # ENTRADA:
        # n     - ocorrencias que queremos que aconteca
        # k     - tentativas
        # p     - probabilidade individual de cada tentativa
        return self.ac.combinacao(n=n, k=k)*pow(p,k)*pow((1-p), (n-k))

    def distribuicao_hipergeometrica(self, N = 0, n = 0, r = 0, k = 0):
        resp = 0
        for i in range(k, r+1):
            numerador = self.ac.combinacao(n=r, k=i)*self.ac.combinacao(n=(N-r), k=(n-i))
            denominador = self.ac.combinacao(n=N, k=n)

            resp += numerador/denominador
        return resp

    def distribuicao_poisson(self, vlambda, k):
        # Numero de ocorrencias de um evento aleatorio dentro de um determinado
        # intervalo de tempo.
        # ENTRADA:
        # vlambda       - media de ocorrencias em um intervalo de tempo
        # k             - numero de ocorrencias que queremos saber a
        #                 probabilidade de ocorrer nesse mesmo intervalo
        return (pow(e,-vlambda)*pow(vlambda,k))/(self.ac.fatorial(k))

class VariavelAleatoriaContinua:

    def fdpValida(self, func, intervalo):
        # Verifica se a funcao eh continua em um dado intervelo, isso eh
        # necessario uma vez que a variavel pode assumir qualquer valor naquele
        # intervalo.
        integral = quad(func, intervalo[0], intervalo[1])
        print(integral)

        if integral[0] == 1:
            return True
        
        return False

    # Medidas de dispersao e posicao com base na funcao e intervalo:
    def media(self, func, intervalo):
        return quad(lambda x: x*func(x), intervalo[0], intervalo[1])
    
    def variancia(self, func, intervalo):
        parte1 = quad(func, intervalo[0], intervalo[1])
        parte2 = pow(quad(func, intervalo[0], intervalo[1]), 2)
        return parte1 - parte2

    def desvio_padrao(self, func, intervalo):
        return sqrt(self.variancia(func, intervalo))
    
    def coeficiente_variabilidade(self, func, intervalo):
        desvio_padrao = self.desvio_padrao(func, intervalo)
        media = self.media(func, intervalo)
        return (desvio_padrao/media)*100
    # Fim medidas.

    def distribuicao_exponencial(self, vlambda, intervalo):
        # Descreve as probabilidades envolvidas no intervalo que decorre para
        # que uma determinada variavel aconteca.
        # Existe uma conexao muito proxima entre a distribuicao exponencial e
        # a de Poisson.
        # ENTRADA:
        # vlambda       -   valor de lambda
        # intervalo     -   valores iniciais e finais da integracao
        return pow(e, -vlambda*intervalo[0]) - pow(e, -vlambda*intervalo[1])

    def media_variavel_exponencial(self, vlambda):
        # Media entre as ocorrencias da variavel, ou seja, media de lambda.
        # ENTRADA:
        # lambda       -    valor de lambda
        return 1/vlambda

    def variancia_variavel_exponencial(self, vlambda):
        # ENTRADA:
        # lambda       -    valor de lambda
        return 1/pow(vlambda, 2)