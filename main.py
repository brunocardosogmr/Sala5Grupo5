import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.apresentacao import executar_modulo as executar_apresentacao
    from src.relatorio import executar_modulo as executar_relatorio  
    from src.calculadora import executar_modulo as executar_calculadora, Calculadora
except ImportError:
    print("Erro: Não foi possível importar todos os módulos.")
    print("Verifique se todos os ficheiros estão no directório src/")
    sys.exit(1)

class ProjectoGrupo:
    
    def __init__(self):
        pass
        
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
        executar_apresentacao()
        input("\nPressione Enter para continuar...")
    
    def modulo_relatorio(self):
        print("\n--- MÓDULO DE RELATÓRIOS ---")
        executar_relatorio()
        input("\nPressione Enter para continuar...")
    
    def modulo_calculadora(self):
        print("\n--- MÓDULO CALCULADORA ---")
        print("1. Executar demonstração do módulo")
        print("2. Usar calculadora interactiva")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            executar_calculadora()
            input("\nPressione Enter para continuar...")
        elif opcao == '2':
            calc = Calculadora()
            calc.calculadora_interactiva()
    
    def demonstracao_completa(self):
        print("\n" + "=" * 60)
        print("DEMONSTRAÇÃO COMPLETA DO PROJECTO")
        print("=" * 60)
        
        print("\n1. APRESENTAÇÃO DO GRUPO:")
        executar_apresentacao()
        
        print("\n2. RELATÓRIO DO PROJECTO:")
        executar_relatorio()
        
        print("\n3. CALCULADORA:")
        executar_calculadora()
        
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