class Calculadora:
    def soma(self, numero1, numero2):
        return numero1 + numero2

    def subtracao(self, numero1, numero2):
        return numero1 - numero2

    def multiplicacao(self, numero1, numero2):
        return numero1 * numero2

    def divisao(self, numero1, numero2):
        return numero1 / numero2

    def calculo(self, operacao, numero1, numero2):
        if operacao == '+':
            return soma(numero1, numero2)
        elif operacao == '-':
            return subtracao(numero1, numero2)
        elif operacao == '*':
            return multiplicacao(numero1, numero2)
        elif operacao == '/':
            return divisao(numero1, numero2)

    def calcular(self):
        print("CALCULADORA")
        numero1 = int(input('Digite o primeiro numero: '))
        numero2 = int(input('Digite o segundo numero: '))
        operacao = input('Digite a operação [+ - * /]: ')

        resultado = calculo(operacao, numero1, numero2)
        print('Resultado: '+str(resultado))

        input('...')
