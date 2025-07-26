class Lista_seq:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.tamanho = 0
        self.vetor = [0] * tamanho_max

    def vazia(self):
        return self.tamanho == 0

    def cheia(self):
        return self.tamanho == self.tamanho_max

    def tamanho_lista(self):
        return self.tamanho

    def elemento(self, posicao: int):
        if 1 <= posicao <= self.tamanho:
            return self.vetor[posicao - 1]
        else:
            return -1

    def modificar(self, posicao: int, dado: int):
        if 1 <= posicao <= self.tamanho:
            self.vetor[posicao - 1] = dado
            return True
        else:
            return False

    def posicao(self, dado: int):
        for i in range(self.tamanho):
            if self.vetor[i] == dado:
                return i + 1
        return -1

    def inserir(self, posicao: int, dado: int):
        if self.cheia() or posicao < 1 or posicao > self.tamanho + 1:
            return False

        indice = posicao - 1
        for i in range(self.tamanho, indice, -1):
            self.vetor[i] = self.vetor[i - 1]

        self.vetor[indice] = dado
        self.tamanho += 1
        return True

    def remover(self, posicao: int):
        if self.vazia():
            raise Exception("Lista vazia")
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida")

        indice = posicao - 1
        for i in range(indice, self.tamanho - 1):
            self.vetor[i] = self.vetor[i + 1]

        self.tamanho -= 1

def mostrar_menu():

    print("\n== MENU ==")
    print("1. Inserir elemento")
    print("2. Remover elemento")
    print("3. Modificar valor")
    print("4. Ver elemento em posição")
    print("5. Buscar posição de um valor")
    print("6. Ver lista completa")
    print("7. Ver tamanho da lista")
    print("8. Verificar se lista está vazia")
    print("9. Verificar se lista está cheia")
    print("0. Sair")
    print()
    print()

def main():
    tamanho = int(input("Digite o tamanho máximo da lista: "))
    lista = Lista_seq(tamanho)

    while True:
        ver_menu = input("\nDeseja ver o menu de opções? (s/n): ").strip().lower()
        if ver_menu in ['s', 'sim']:
            mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pos = int(input("Posição para inserir (inicia em 1): "))
            valor = int(input("Valor: "))
            if lista.inserir(pos, valor):
                print("Inserido com sucesso.")
            else:
                print("Erro ao inserir.")
        
        elif opcao == '2':
            pos = int(input("Posição para remover (inicia em 1): "))
            try:
                lista.remover(pos - 1)
                print("Removido com sucesso.")
            except Exception as e:
                print("Erro:", e)
        
        elif opcao == '3':
            pos = int(input("Posição para modificar (inicia em 1): "))
            novo = int(input("Novo valor: "))
            if lista.modificar(pos, novo) == -1:
                print("Posição inválida.")
            else:
                print("Modificado com sucesso.")
        
        elif opcao == '4':
            pos = int(input("Posição para ver (inicia em 1): "))
            valor = lista.elemento(pos)
            if valor == -1:
                print("Posição inválida.")
            else:
                print(f"Valor na posição {pos}: {valor}")
        
        elif opcao == '5':
            valor = int(input("Valor para buscar: "))
            pos = lista.posicao(valor)
            if pos == -1:
                print("Valor não encontrado.")
            else:
                print(f"Valor encontrado na posição {pos}")
        
        elif opcao == '6':
            print("Lista atual:")
            print([lista.elemento(i) for i in range(1, lista.tamanho_lista() + 1)])
        
        elif opcao == '7':
            print("Tamanho da lista:", lista.tamanho_lista())

        elif opcao == '8':
            print("Lista vazia?", lista.vazia())
        
        elif opcao == '9':
            print("Lista cheia?", lista.cheia())
        
        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()