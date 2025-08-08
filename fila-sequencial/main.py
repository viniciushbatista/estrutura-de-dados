#CLASSE DA FILA SEQUENCIAL
class FilaSeq: 
    
    #Construtor
    def __init__(self):
        self.inicio = 0
        self.fim = -1
        self.nElementos = 0
        self.tamanhoMax = 100
        self.dados = [0] * self.tamanhoMax
    
    #Verifica se a fila está vazia
    def vazia(self):
        if self.nElementos == 0:
            return True
        else: 
            return False
      
      #Verifica se a fila está cheia  
    def cheia(self):
        if self.nElementos == self.tamanhoMax:
            return True
        else:
            return False
    
    #Retorna o tamanho da fila
    def tamanho(self):
        return self.nElementos
    
    #Retorna o ínicio da fila. Retorna -1 se a fila estiver vazia
    def primeiro(self):
        if (self.vazia()):
            return -1
        
        return self.dados[self.inicio]     
    
    #Método de inserção na fila
    def insere(self, valor: int):
        if (self.cheia()):
            return False
        
        self.fim = fim = (self.fim + 1) % self.tamanhoMax #0, 1, 2, 3, 4, ..., tamanhoMax - 1
        self.dados[self.fim] = valor
        self.nElementos += 1
        return True
    
    """
    Remove o elemento do começo da fila e 
    retorna com o valor que foi removido.
    """
    def remove(self):
        if (self.vazia()):
            return -1
        
        res = self.primeiro()
        self.inicio = (self.inicio + 1) % self.tamanhoMax
        self.nElementos -= 1
        return res



#Testes via menu
def mostrar_menu():

    print("\n== MENU ==")
    print("1. Inserir no fim da fila")
    print("2. Remover do início da fila")
    print("3. Consultar o início da fila")
    print("4. Verificar se fila está vazia")
    print("5. Verificar se fila está cheia")
    print("0. Sair")
    print()
    print()

def main():
    fila = FilaSeq()

    while True:
        ver_menu = input("\nDeseja ver o menu de opções? (s/n): ").strip().lower()
        if ver_menu in ['s', 'sim']:
            mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = int(input("insira um valor a fila: "))
            fila.insere(valor)
        
        elif opcao == '2':
            remov = fila.remove()
            print(f"valor removido: {remov}")
        
        elif opcao == '3':
           
            if fila.primeiro() == -1:
                print("A fila está vazia")
            else:
                print(f"o valor no inicio da fila é: {fila.primeiro()}")
        
        elif opcao == '4':
           if fila.vazia():
               print("A fila está vazia")
           else:
               print("A fila possui elementos")
        
        elif opcao == '5':
            print("Fila cheia?", fila.cheia())
        
        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()