class Auxiliares:
    def format_number(self, value):
        # Formata as casas decimais de um numero.
        # Arredonda para duas casas decimais e se as casas forem 0
        # transforma em inteiro
        # ENTRADA:
        #   value   - int ou double
        return ('%.2f' % value).rstrip('0').rstrip('.')

    def to_percent(self, value):
        # Multiplica por 100 e adiciona o simbolo de porcentagem.
        return self.format_number(value*100)+'%'