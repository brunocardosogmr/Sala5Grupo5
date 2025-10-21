class InfoGrupo:
    
    def __init__(self):
        self.nome_grupo = "Sala5Grupo5"
        self.membros = []
        self.projecto = "Actividade Assíncrona em Grupo - Git/GitHub"
        
    def adicionar_membro(self, nome, especialidade=""):
        membro = {
            "nome": nome,
            "especialidade": especialidade
        }
        self.membros.append(membro)
        print(f"Membro {nome} adicionado ao grupo!")
    
    def apresentar_grupo(self):
        print("=" * 50)
        print(f"GRUPO: {self.nome_grupo}")
        print(f"PROJECTO: {self.projecto}")
        print("=" * 50)
        
        if self.membros:
            print("MEMBROS DO GRUPO:")
            for i, membro in enumerate(self.membros, 1):
                print(f"{i}. Nome: {membro['nome']}")
                if membro['especialidade']:
                    print(f"   Especialidade: {membro['especialidade']}")
                print()
        else:
            print("Nenhum membro adicionado ainda.")
            print("Cada membro deve editar este ficheiro na sua branch!")
        
        print("=" * 50)

def main():
    grupo = InfoGrupo()
    grupo.adicionar_membro("Filipe Braga", "Programação")
    # Cada membro deve descomentar e preencher uma linha abaixo na sua branch 
    # grupo.adicionar_membro("Nome Membro x", "Programação")
    
    grupo.apresentar_grupo()

if __name__ == "__main__":
    main()