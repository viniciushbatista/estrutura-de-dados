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

