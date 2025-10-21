from datetime import datetime
import os

class GeradorRelatorio:
    
    def __init__(self):
        self.data_criacao = datetime.now()
        self.actividades = []
        
    def adicionar_actividade(self, descricao, responsavel, estado="Em andamento"):
        actividade = {
            "descricao": descricao,
            "responsavel": responsavel,
            "estado": estado,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.actividades.append(actividade)
        print(f"Actividade '{descricao}' adicionada ao relatório.")
    
    def gerar_relatorio_consola(self):
        print("\n" + "=" * 60)
        print("RELATÓRIO DE ACTIVIDADES DO PROJECTO")
        print("=" * 60)
        print(f"Data de Geração: {self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Projecto: Actividade Assíncrona Git/GitHub")
        print("-" * 60)
        
        if self.actividades:
            for i, actividade in enumerate(self.actividades, 1):
                print(f"{i}. {actividade['descricao']}")
                print(f"   Responsável: {actividade['responsavel']}")
                print(f"   Estado: {actividade['estado']}")
                print(f"   Data: {actividade['data']}")
                print()
        else:
            print("Nenhuma actividade registada ainda.")
            print("Adicione actividades usando adicionar_actividade()")
        
        print("=" * 60)
    
    def gerar_relatorio_ficheiro(self, nome_ficheiro="relatorio_projecto.txt"):
        try:
            with open(nome_ficheiro, 'w', encoding='utf-8') as f:
                f.write("RELATÓRIO DE ACTIVIDADES DO PROJECTO\n")
                f.write("=" * 60 + "\n")
                f.write(f"Data de Geração: {self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write(f"Projecto: Actividade Assíncrona Git/GitHub\n")
                f.write("-" * 60 + "\n\n")
                
                if self.actividades:
                    for i, actividade in enumerate(self.actividades, 1):
                        f.write(f"{i}. {actividade['descricao']}\n")
                        f.write(f"   Responsável: {actividade['responsavel']}\n")
                        f.write(f"   Estado: {actividade['estado']}\n")
                        f.write(f"   Data: {actividade['data']}\n\n")
                else:
                    f.write("Nenhuma actividade registada ainda.\n")
                
                f.write("=" * 60 + "\n")
            
            print(f"Relatório gerado com sucesso: {nome_ficheiro}")
        except Exception as e:
            print(f"Erro ao gerar relatório: {e}")
    
    def estatisticas(self):
        total = len(self.actividades)
        concluidas = len([a for a in self.actividades if a['estado'].lower() == 'concluída'])
        em_andamento = len([a for a in self.actividades if a['estado'].lower() == 'em andamento'])
        
        print("\nESTATÍSTICAS DO PROJECTO:")
        print(f"Total de actividades: {total}")
        print(f"Actividades concluídas: {concluidas}")
        print(f"Actividades em andamento: {em_andamento}")
        
        if total > 0:
            percentagem = (concluidas / total) * 100
            print(f"Percentagem de conclusão: {percentagem:.1f}%")

def executar_modulo():
    relatorio = GeradorRelatorio()
    
    relatorio.adicionar_actividade("Criar repositório GitHub", "Membro 1", "Concluída")
    relatorio.adicionar_actividade("Criar ficheiro de apresentação", "Membro 2", "Em andamento")
    relatorio.adicionar_actividade("Desenvolver calculadora", "Membro 3", "Em andamento")
    relatorio.adicionar_actividade("Criar documentação", "Membro 4", "Em andamento")
    
    relatorio.gerar_relatorio_consola()
    relatorio.estatisticas()
    relatorio.gerar_relatorio_ficheiro()
    return relatorio

def main():
    executar_modulo()

if __name__ == "__main__":
    main()