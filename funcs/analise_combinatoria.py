class AnaliseCombinatoria:
    def fatorial(self, n):
        if ((not n.isnumeric()) and n != None):
            raise ValueError("insira os valores")
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        return fatorial

    def combinacao(self, n = 0, k = 0):
        # Quantidade de combinações que podemos fazer com 'k'
        # elementos de um conjunto com 'n' elementos.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        #   k   -   quantidade elementos retirados do conjunto
        return self.fatorial(n)/(self.fatorial(k)*self.fatorial(n-k))
    
    def combinacao_com_repeticao(self, n = 0, k = 0):
        # Quantidade de combinações que podemos fazer com 'k'
        # elementos de um conjunto com 'n' quando a ordem
        # dos elementos nao importa: ABC != CBA.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        #   k   -   quantidade elementos retirados do conjunto
        if (n == 0 or k == 0):
            raise ValueError("insira os valores")
        return self.fatorial(n+k-1)/(self.fatorial(k)*self.fatorial(n-1))

    def arranjo_simples(self, n = 0, k = 0):
        # Quantidade de permutacoes que podemos fazer com 'k'
        # elementos de um conjunto com 'n' elementos.
        # Arranjo simples eh quando cada elemento de 'n' so pode ser
        # usado uma vez.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        #   k   -   quantidade elementos retirados do conjunto
        return self.fatorial(n)/(self.fatorial(n-k))

    def arranjo_com_repeticao(self, n = 0, k = 0):
        # Quantidade de permutacoes que podemos fazer com 'k'
        # elementos de um conjunto com 'n' elementos.
        # Arranjo com repeticao eh quando cada elemento de 'n'
        # pode se repetir.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        #   k   -   quantidade elementos retirados do conjunto
        return self.fatorial(n)/(self.fatorial(n-k))

    def permutacao_simples(self, n = 0):
        # Quantas vezes eh possivel permutar os elementos de lugar
        # para conseguir um novo grupo.
        # Em uma permutacao simples os valores nao se repetem.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        return self.fatorial(n)

    def permutacao_circular(self, n = 0):
        # Quantas vezes eh possivel permutar os elementos em uma ordem
        # ciclica para conseguir um novo grupo.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        return self.fatorial(n-1)

    def permutacao_com_repeticao(self, n = 0, lista = []):
        # Quantas vezes eh possivel permutar os elementos de lugar
        # para conseguir um novo grupo.
        # Em uma permutacao com repeticao alguns valores aparecem
        # mais de uma vez.
        # ENTRADAS:
        #   n   -   total elementos no conjunto
        #   lista - quantidade dos elementos repetidos
        mult_fatoriais = 1
        for value in lista:
            mult_fatoriais *= self.fatorial(value)
        
        return self.fatorial(n)/mult_fatoriais