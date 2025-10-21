"""
Arquivo Principal do Projeto
============================

Este arquivo integra todos os módulos do projeto e serve como ponto de entrada.
Responsável: [NOME DO MEMBRO - para ser preenchido na branch individual]

Data: 21 de Outubro de 2025
Projeto: Atividade Assíncrona Git/GitHub - Sala5Grupo5
"""

import sys
import os

# Adicionar o diretório src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.apresentacao import InfoGrupo
    from src.relatorio import GeradorRelatorio
    from src.calculadora import Calculadora
except ImportError:
    print("Erro: Não foi possível importar todos os módulos.")
    print("Verifique se todos os ficheiros estão no directório src/")
    sys.exit(1)

class ProjectoGrupo:
    
    def __init__(self):
        self.grupo = InfoGrupo()
        self.relatorio = GeradorRelatorio()
        self.calculadora = Calculadora()
        
    def menu_principal(self):
        while True:
            print("\n" + "=" * 50)
            print("PROJECTO ACTIVIDADE ASSÍNCRONA EM GRUPO")
            print("Sala5Grupo5 - Git/GitHub")
            print("=" * 50)
            print("1. Apresentação do Grupo")
            print("2. Relatórios do Projecto")
            print("3. Calculadora")
            print("4. Demonstração Completa")
            print("5. Sobre o Projecto")
            print("0. Sair")
            print("=" * 50)
            
            try:
                opcao = input("Escolha uma opção (0-5): ")
                
                if opcao == '0':
                    print("\nObrigado por usar o nosso projecto!")
                    print("Desenvolvido pelo Sala5Grupo5")
                    break
                elif opcao == '1':
                    self.modulo_apresentacao()
                elif opcao == '2':
                    self.modulo_relatorio()
                elif opcao == '3':
                    self.modulo_calculadora()
                elif opcao == '4':
                    self.demonstracao_completa()
                elif opcao == '5':
                    self.sobre_projecto()
                else:
                    print("Opção inválida! Escolha um número de 0 a 5.")
                    
            except KeyboardInterrupt:
                print("\n\nPrograma interrompido pelo utilizador.")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")
    
    def modulo_apresentacao(self):
        print("\n--- MÓDULO DE APRESENTAÇÃO ---")
        self.grupo.apresentar_grupo()
        input("\nPressione Enter para continuar...")
    
    def modulo_relatorio(self):
        print("\n--- MÓDULO DE RELATÓRIOS ---")
        
        if not self.relatorio.actividades:
            self.relatorio.adicionar_actividade("Criação do repositório", "Equipa", "Concluída")
            self.relatorio.adicionar_actividade("Desenvolvimento dos módulos", "Todos os membros", "Em andamento")
            self.relatorio.adicionar_actividade("Testes e integração", "Equipa", "Em andamento")
        
        while True:
            print("\n1. Ver relatório na consola")
            print("2. Gerar relatório em ficheiro")
            print("3. Ver estatísticas")
            print("4. Adicionar actividade")
            print("0. Voltar ao menu principal")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '0':
                break
            elif opcao == '1':
                self.relatorio.gerar_relatorio_consola()
            elif opcao == '2':
                self.relatorio.gerar_relatorio_ficheiro()
            elif opcao == '3':
                self.relatorio.estatisticas()
            elif opcao == '4':
                desc = input("Descrição da actividade: ")
                resp = input("Responsável: ")
                estado = input("Estado (Em andamento/Concluída): ")
                self.relatorio.adicionar_actividade(desc, resp, estado)
            else:
                print("Opção inválida!")
    
    def modulo_calculadora(self):
        print("\n--- MÓDULO CALCULADORA ---")
        print("1. Usar calculadora interactiva")
        print("2. Demonstração rápida")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            self.calculadora.calculadora_interactiva()
        elif opcao == '2':
            print("\n=== DEMONSTRAÇÃO DA CALCULADORA ===")
            print(f"5 + 3 = {self.calculadora.adicionar(5, 3)}")
            print(f"10 - 4 = {self.calculadora.subtrair(10, 4)}")
            print(f"6 × 7 = {self.calculadora.multiplicar(6, 7)}")
            print(f"20 ÷ 4 = {self.calculadora.dividir(20, 4)}")
            print(f"2^10 = {self.calculadora.potencia(2, 10)}")
            print(f"√16 = {self.calculadora.raiz_quadrada(16)}")
            self.calculadora.mostrar_historico()
            input("\nPressione Enter para continuar...")
    
    def demonstracao_completa(self):
        print("\n" + "=" * 60)
        print("DEMONSTRAÇÃO COMPLETA DO PROJECTO")
        print("=" * 60)
        
        print("\n1. APRESENTAÇÃO DO GRUPO:")
        self.grupo.apresentar_grupo()
        
        print("\n2. RELATÓRIO DO PROJECTO:")
        if not self.relatorio.actividades:
            self.relatorio.adicionar_actividade("Setup inicial do projecto", "Equipa", "Concluída")
            self.relatorio.adicionar_actividade("Desenvolvimento módulo apresentação", "Membro 1", "Concluída")
            self.relatorio.adicionar_actividade("Desenvolvimento módulo relatório", "Membro 2", "Concluída")
            self.relatorio.adicionar_actividade("Desenvolvimento calculadora", "Membro 3", "Concluída")
            self.relatorio.adicionar_actividade("Integração e testes", "Membro 4", "Em andamento")
        
        self.relatorio.gerar_relatorio_consola()
        self.relatorio.estatisticas()
        
        print("\n3. CALCULADORA:")
        print("Operações de exemplo:")
        print(f"100 + 50 = {self.calculadora.adicionar(100, 50)}")
        print(f"200 - 75 = {self.calculadora.subtrair(200, 75)}")
        print(f"12 × 8 = {self.calculadora.multiplicar(12, 8)}")
        print(f"144 ÷ 12 = {self.calculadora.dividir(144, 12)}")
        
        print("\n" + "=" * 60)
        print("DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        input("\nPressione Enter para continuar...")
    
    def sobre_projecto(self):
        print("\n" + "=" * 50)
        print("SOBRE O PROJECTO")
        print("=" * 50)
        print("Projecto: Actividade Assíncrona em Grupo")
        print("Objectivo: Aprender Git/GitHub colaborativo")
        print("Grupo: Sala5Grupo5")
        print("Data: Outubro 2025")
        print()
        print("ESTRUTURA DO PROJECTO:")
        print("├── src/")
        print("│   ├── apresentacao.py  (Informações do grupo)")
        print("│   ├── relatorio.py     (Geração de relatórios)")
        print("│   └── calculadora.py   (Operações matemáticas)")
        print("├── main.py              (Ficheiro principal)")
        print("└── README.md            (Documentação)")
        print()
        print("FUNCIONALIDADES:")
        print("• Gestão de informações do grupo")
        print("• Geração de relatórios de actividades")
        print("• Calculadora com operações básicas")
        print("• Interface integrada e amigável")
        print()
        print("TECNOLOGIAS UTILIZADAS:")
        print("• Python 3.x")
        print("• Git/GitHub para controlo de versões")
        print("• Programação orientada a objectos")
        print("=" * 50)
        input("\nPressione Enter para continuar...")

def main():
    try:
        projecto = ProjectoGrupo()
        projecto.menu_principal()
    except Exception as e:
        print(f"Erro crítico: {e}")
        print("O programa será encerrado.")

if __name__ == "__main__":
    main()