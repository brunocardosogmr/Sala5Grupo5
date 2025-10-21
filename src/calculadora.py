import math

class Calculadora:
    
    def __init__(self):
        self.historico = []
        self.ultimo_resultado = 0
    
    def adicionar(self, a, b):
        resultado = a + b
        operacao = f"{a} + {b} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def subtrair(self, a, b):
        resultado = a - b
        operacao = f"{a} - {b} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        operacao = f"{a} × {b} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def dividir(self, a, b):
        if b == 0:
            print("Erro: Divisão por zero não é permitida!")
            return None
        
        resultado = a / b
        operacao = f"{a} ÷ {b} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def potencia(self, base, expoente):
        resultado = base ** expoente
        operacao = f"{base}^{expoente} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def raiz_quadrada(self, numero):
        if numero < 0:
            print("Erro: Não é possível calcular raiz quadrada de número negativo!")
            return None
        
        resultado = math.sqrt(numero)
        operacao = f"√{numero} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def percentagem(self, valor, percentagem):
        resultado = (valor * percentagem) / 100
        operacao = f"{percentagem}% de {valor} = {resultado}"
        self.historico.append(operacao)
        self.ultimo_resultado = resultado
        return resultado
    
    def mostrar_historico(self):
        print("\nHISTÓRICO DE OPERAÇÕES:")
        print("-" * 30)
        if self.historico:
            for i, operacao in enumerate(self.historico, 1):
                print(f"{i}. {operacao}")
        else:
            print("Nenhuma operação realizada ainda.")
        print("-" * 30)
    
    def limpar_historico(self):
        self.historico.clear()
        self.ultimo_resultado = 0
        print("Histórico limpo!")
    
    def calculadora_interactiva(self):
        print("=== CALCULADORA INTERACTIVA ===")
        print("Comandos disponíveis:")
        print("1 - Adição")
        print("2 - Subtracção") 
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Raiz Quadrada")
        print("7 - Percentagem")
        print("h - Mostrar histórico")
        print("c - Limpar histórico")
        print("q - Sair")
        print("=" * 30)
        
        while True:
            try:
                opcao = input("\nEscolha uma opção: ").lower()
                
                if opcao == 'q':
                    print("Obrigado por usar a calculadora!")
                    break
                elif opcao == 'h':
                    self.mostrar_historico()
                elif opcao == 'c':
                    self.limpar_historico()
                elif opcao == '1':
                    a = float(input("Primeiro número: "))
                    b = float(input("Segundo número: "))
                    resultado = self.adicionar(a, b)
                    print(f"Resultado: {resultado}")
                elif opcao == '2':
                    a = float(input("Primeiro número: "))
                    b = float(input("Segundo número: "))
                    resultado = self.subtrair(a, b)
                    print(f"Resultado: {resultado}")
                elif opcao == '3':
                    a = float(input("Primeiro número: "))
                    b = float(input("Segundo número: "))
                    resultado = self.multiplicar(a, b)
                    print(f"Resultado: {resultado}")
                elif opcao == '4':
                    a = float(input("Primeiro número: "))
                    b = float(input("Segundo número: "))
                    resultado = self.dividir(a, b)
                    if resultado is not None:
                        print(f"Resultado: {resultado}")
                elif opcao == '5':
                    base = float(input("Base: "))
                    exp = float(input("Expoente: "))
                    resultado = self.potencia(base, exp)
                    print(f"Resultado: {resultado}")
                elif opcao == '6':
                    num = float(input("Número: "))
                    resultado = self.raiz_quadrada(num)
                    if resultado is not None:
                        print(f"Resultado: {resultado}")
                elif opcao == '7':
                    valor = float(input("Valor: "))
                    perc = float(input("Percentagem: "))
                    resultado = self.percentagem(valor, perc)
                    print(f"Resultado: {resultado}")
                else:
                    print("Opção inválida! Tente novamente.")
                    
            except ValueError:
                print("Erro: Por favor, insira um número válido!")
            except Exception as e:
                print(f"Erro inesperado: {e}")

def main():
    calc = Calculadora()
    
    print("=== TESTE DA CALCULADORA ===")
    print(f"10 + 5 = {calc.adicionar(10, 5)}")
    print(f"10 - 3 = {calc.subtrair(10, 3)}")
    print(f"4 × 7 = {calc.multiplicar(4, 7)}")
    print(f"15 ÷ 3 = {calc.dividir(15, 3)}")
    print(f"2^8 = {calc.potencia(2, 8)}")
    print(f"√25 = {calc.raiz_quadrada(25)}")
    print(f"20% de 150 = {calc.percentagem(150, 20)}")
    
    calc.mostrar_historico()

if __name__ == "__main__":
    main()