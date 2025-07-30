class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.cabeca is None

    def obter_tamanho(self):
        return self.tamanho

    def _obter_no_na_posicao(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            return None

        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        return atual

    def obter_valor(self, posicao):
        if self.esta_vazia():
            raise IndexError("A lista está vazia. Não é possível obter valor.")
        
        no = self._obter_no_na_posicao(posicao)
        if no is None:
            raise IndexError(f"Posição {posicao} fora dos limites da lista.")
        return no.valor

    def modificar_valor(self, posicao, novo_valor):
        if self.esta_vazia():
            raise IndexError("A lista está vazia. Não é possível modificar valor.")
            
        no = self._obter_no_na_posicao(posicao)
        if no is None:
            raise IndexError(f"Posição {posicao} fora dos limites da lista.")
        no.valor = novo_valor

    def inserir(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho + 1:
            raise IndexError(f"Posição {posicao} inválida para inserção. A posição deve estar entre 1 e {self.tamanho + 1}.")

        novo_no = No(valor)

        if posicao == 1:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            no_anterior = self._obter_no_na_posicao(posicao - 1)
            novo_no.proximo = no_anterior.proximo
            no_anterior.proximo = novo_no
        
        self.tamanho += 1

    def remover(self, posicao):
        if self.esta_vazia():
            raise IndexError("Não é possível remover elementos.")
        
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError(f"Posição {posicao} fora dos limites da lista.")

        valor_removido = None
        if posicao == 1:
            valor_removido = self.cabeca.valor
            self.cabeca = self.cabeca.proximo
        else:
            no_anterior = self._obter_no_na_posicao(posicao - 1)
            no_removido = no_anterior.proximo
            valor_removido = no_removido.valor
            no_anterior.proximo = no_removido.proximo

        self.tamanho -= 1
        return valor_removido

    def imprimir_lista(self):
        if self.esta_vazia():
            print("Lista vazia")
            return

        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(f"[{', '.join(elementos)}]")


def mostrar_menu():

    print("\n== MENU ==")
    print("1. Inserir elemento")
    print("2. Remover elemento")
    print("3. Modificar valor de uma posição")
    print("4. Buscar valor de uma posição")
    print("5. Ver lista completa")
    print("6. Ver tamanho da lista")
    print("7. Verificar se lista está vazia")
    print("0. Sair")
    print()
    print()

def main():
    lista = LinkedList()

    while True:
        ver_menu = input("\nDeseja ver o menu de opções? (s/n): ").strip().lower()
        if ver_menu in ['s', 'sim']:
            mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pos = int(input("Posição para inserir (inicia em 1): "))
            valor = int(input("Valor: "))
            lista.inserir(pos, valor)
            print("Valor inserido na lista")
        
        elif opcao == '2':
            pos = int(input("Posição para remover (inicia em 1): "))
            try:
                lista.remover(pos)
                print("Removido com sucesso.")
            except Exception as e:
                print("Erro:", e)
        
        elif opcao == '3':
            pos = int(input("Posição para modificar (inicia em 1): "))
            novo = int(input("Novo valor: "))
            if lista.modificar_valor(pos, novo) == -1:
                print("Posição inválida.")
            else:
                print("Modificado com sucesso.")
        
        elif opcao == '4':
            pos = int(input("Posição para ver (inicia em 1): "))
            valor = lista.obter_valor(pos)
            if valor == -1:
                print("Posição inválida.")
            else:
                print(f"Valor na posição {pos}: {valor}")
        
        elif opcao == '5':
            lista.imprimir_lista()
        
        elif opcao == '6':
            print("Tamanho da lista:", lista.obter_tamanho())

        elif opcao == '7':
            print("Lista vazia?", lista.esta_vazia())
        
        
        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()