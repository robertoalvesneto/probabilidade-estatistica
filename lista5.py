from math import inf
from funcs.estatistica import Estatistica, VariavelAleatoriaContinua

e = Estatistica()
vac = VariavelAleatoriaContinua()

'''
1. O tempo de vida (em horas) de um transistor é uma variável aleatória T com distribuição
exponencial. O tempo médio de vida do transistor é de 500 horas.
a) Calcule a probabilidade de o transistor durar mais do que 500 horas.
'''
print("1)")
value = vac.distribuicao_exponencial(vlambda=1/500, intervalo=[500, inf])
value = e.to_percent(value=value)
print("a) {0}".format(value))

#b) Calcule a probabilidade de o transistor durar entre 300 e 1000 horas.
value = vac.distribuicao_exponencial(vlambda=1/500, intervalo=[300, 1000])
value = e.to_percent(value=value)
print("b) {0}".format(value))


print("\n")
'''
2. Uma fábrica de monitores determinou que a vida média dos seus LCDs é de 800 horas de uso
contínuo, seguindo uma distribuição exponencial. Qual a probabilidade de que a fábrica tenha
de substituir um monitor gratuitamente, se ela oferece uma garantia de 300 horas de uso?
'''
value = vac.distribuicao_exponencial(vlambda=1/800, intervalo=[0, 300])
value = e.to_percent(value=value)
print("2) {0}".format(value))