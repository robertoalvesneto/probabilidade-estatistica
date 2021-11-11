from funcs.estatistica import Estatistica

e = Estatistica()

'''
1. As linhas telefônicas em um sistema de reservas de uma companhia aérea estão
ocupadas 40% do tempo. Suponha que os eventos em que as linhas estejam ocupadas
em sucessivas chamadas sejam independentes. Considere que aconteçam 10 chamadas
para a companhia. Seja X uma v.a. aleatória definida pelo no de chamadas que
encontram as linhas ocupadas.
a) Qual a probabilidade de que, para exatamente três chamadas às linhas estejam
ocupadas?
'''
print("1)")
value = e.distribuicao_binominal(10, 3, 0.4)
value = e.to_percent(value=value)
print("a) {0}".format(value))
#b) Qual é o número esperado de chamadas em que todas as linhas estejam ocupadas?

value = 10*0.4
print("b) {0}".format(value))


print("\n")
'''
2. A probabilidade de que um servidor atenda a uma requisição em menos de 5 segundos
é de 0,75. Assuma que as requisições são independentes.
a) Se 10 requisições são feitas, qual a probabilidade de que exatamente 9 sejam
respondidas dentro dos 5 segundos?
'''
print("2)")
value = e.distribuicao_binominal(n=10, k=9, p=0.75)
value = e.to_percent(value=value)
print("a) {0}".format(value))

#b) Se 20 requisições são feitas, qual a probabilidade de que pelo menos 16 sejam
#respondidas dentro dos 5 segundos?

v16 = e.distribuicao_binominal(n=20, k=16, p=0.75)
v17 = e.distribuicao_binominal(n=20, k=17, p=0.75)
v18 = e.distribuicao_binominal(n=20, k=18, p=0.75)
v19 = e.distribuicao_binominal(n=20, k=19, p=0.75)
v20 = e.distribuicao_binominal(n=20, k=20, p=0.75)

p_total = v16 + v17 + v18 + v19 + v20

v16 = e.to_percent(value=v16)
v17 = e.to_percent(value=v17)
v18 = e.to_percent(value=v18)
v19 = e.to_percent(value=v19)
v20 = e.to_percent(value=v20)
p_total = e.to_percent(value=p_total)

s = "b) p16 = {0}, p17 = {1}, p18 = {2}, p19 = {3}, p20 = {4}"
print(s.format(v16, v17, v18, v19, v20))
print("   p_total {0}".format(p_total))

#c) Se 20 requisições são feitas, qual o número médio de chamadas que serão
#respondidas em menos do que 5 segundos?
value = 20*0.75
print("c) {0}".format(value))


print("\n")
'''
3. Acredita-se que 20% dos moradores das proximidades de uma grande indústria
siderúrgica têm alergia aos poluentes lançados ao ar. Admitindo que este percentual
de alérgicos é real (correto), calcule a probabilidade de que pelo menos 4 moradores
tenham alergia entre 13 selecionados ao acaso.
'''
print("3)")

value = []
p_total = 0

for i in range(4, 13+1):
    aux = e.distribuicao_binominal(n=13, k=i, p=0.2)
    p_total += aux
    value.append(e.to_percent(value=aux))

p_total = e.to_percent(value=p_total)

print(value)
print("p total: {0}".format(p_total))

print("\n")
'''
4. A probabilidade de ocorrência de turbulência em um determinado percurso a ser feito
por uma aeronave é de 0,4 em um circuito diário. Seja X o número de voos com
turbulência em um total de 7 desses voos (ou seja, uma semana de trabalho). Qual a
probabilidade de que:
a) Não haja turbulência em nenhum dos 7 voos?
'''
value = e.distribuicao_binominal(n=7, k=0, p=0.4)
value = e.to_percent(value=value)
print("a) {0}".format(value))

#b) Haja turbulência em pelo menos 2 deles?
value = e.distribuicao_binominal(n=7, k=0, p=0.4)
value += e.distribuicao_binominal(n=7, k=1, p=0.4)

resp = e.evento_complementar(value)
resp = e.to_percent(resp)
print("b) {0}".format(resp))

#c) X esteja entre E(X) – DP(X) e E(X) + DP(X)?
media = e.media(e=7, p=0.4)
desvio_padrao = e.desvio_padrao(e=7, p=0.4)
print("intervalo da prob de {0} ate {1}".format(media-desvio_padrao, media+desvio_padrao))

value = e.distribuicao_binominal(n=7, k=0, p=0.4)
value += e.distribuicao_binominal(n=7, k=1, p=0.4)
value += e.distribuicao_binominal(n=7, k=2, p=0.4)
value += e.distribuicao_binominal(n=7, k=3, p=0.4)
value += e.distribuicao_binominal(n=7, k=4, p=0.4)
value += e.distribuicao_binominal(n=7, k=5, p=0.4)
value += e.distribuicao_binominal(n=7, k=6, p=0.4)
value = e.to_percent(value)
print(value)

print("\n")
'''
5. O número de falhas em parafusos de máquinas da indústria têxtil segue a distribuição
de Poisson com média de 0,1 falha por metro quadrado.
a) Qual a probabilidade de que haja duas falhas em um m2 de tecido?
'''
print("5)")

value = e.distribuicao_poisson(vlambda=0.1, k=2)
value = e.to_percent(value=value)
print("a) {0}".format(value))


#b) Qual a probabilidade de que haja uma falha em 10 m2 de tecido?
value = e.distribuicao_poisson(vlambda=1, k=1)
value = e.to_percent(value=value)
print("b) {0}".format(value))

#c) Qual a probabilidade de que não haja falhas em 20 m2 de tecido?
value = e.distribuicao_poisson(vlambda=2, k=0)
value = e.to_percent(value=value)
print("c) {0}".format(value))

#d) Qual a probabilidade de que haja no mínimo duas falhas em 10 m2 de tecido?
value = e.distribuicao_poisson(vlambda=1, k=0)
value += e.distribuicao_poisson(vlambda=1, k=1)
value = e.evento_complementar(value)
value = e.to_percent(value=value)
print("d) {0}".format(value))


print("\n")
'''
6. Em um cruzamento com tráfego intenso, a probabilidade de um carro sofrer acidente é
bastante pequena e estimada como p = 0,0001. Durante certa parte do dia, muitos carros
passam pelo cruzamento, algo como 10.000 carros. Nessas condições, qual é a
probabilidade de que 2 ou mais carros se acidem naquele período?
'''
vlambda = 10000*0.0001
value = e.distribuicao_poisson(vlambda=vlambda, k=0)
value += e.distribuicao_poisson(vlambda=vlambda, k=1)
value = e.evento_complementar(value)
value = e.to_percent(value=value)
print("6) {0}".format(value))


print("\n")
'''
7. A aplicação do fundo anticorrosivo em chapas de aço de 1m2 é feita mecanicamente e
pode produzir defeitos (pequenas bolhas na pintura) de acordo com uma variável
aleatória de Poisson de parâmetro alfa = 1 defeito por m2. Uma chapa é sorteada ao acaso
para ser inspecionada, pergunta-se a probabilidade de:
a) Encontrarmos pelo menos 1 defeito.
'''
print("7)")
value = e.distribuicao_poisson(vlambda=1, k=0)
value = e.evento_complementar(value)
value = e.to_percent(value=value)
print("a) {0}".format(value))

#b) No máximo 2 defeitos serem encontrados.
value = e.distribuicao_poisson(vlambda=1, k=0)
value += e.distribuicao_poisson(vlambda=1, k=1)
value += e.distribuicao_poisson(vlambda=1, k=2)
value = e.to_percent(value=value)
print("b) {0}".format(value))

#c) Não mais de 1 defeito ser encontrado
value = e.distribuicao_poisson(vlambda=1, k=0)
value += e.distribuicao_poisson(vlambda=1, k=1)
value = e.evento_complementar(value)
value = e.to_percent(value=value)
print("c) {0}".format(value))

print("\n")
'''
8. Seja X o número de acidentes mensais ocorridos numa determinada indústria. Se o
número médio de acidentes por mês é 3, qual a probabilidade de não ocorrer nenhum
acidente no próximo mês?
'''
value = e.distribuicao_poisson(vlambda=3, k=0)
value = e.to_percent(value=value)
print("8) {0}".format(value))
