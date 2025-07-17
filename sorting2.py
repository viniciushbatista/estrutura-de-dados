'''
    O código faz a comparação entre o insertionsort e o selectionsort com base no tempo.

    o código pede um caminho do arquivos enviados via sigaa no caso as instancinas numericas (os arquivos .in)
    no caso basta colocar o caminho onde está o arquivo .in ou qualquer outro com os valores e verificar
    o tempo que cada um leva.

'''

import time

def selection_sort(vetor):
    i = 0
    while i < len(vetor) - 1:
        menor = i
        j = i + 1

        #busca o menor valor
        while j < len(vetor):
            if vetor[j] < vetor[menor]:
                menor = j
            j += 1
        
        if menor != i:
            temp = vetor[i]
            vetor[i] = vetor[menor]
            vetor[menor] = temp
        
        i += 1

def insertion_sort(vetor):
    i = 1
    while i < len(vetor):
        temp = vetor[i]
        j = i - 1
        trocou = False
        while j >= 0 and vetor[j] > temp:
            vetor[j + 1] = vetor[j]
            trocou = True
            j -= 1

        if trocou:
            vetor[j + 1] = temp

        i += 1

def ler_arquivo(caminho):
    with open(caminho, 'r') as arquivo:
        return [int(linha.strip()) for linha in arquivo.readlines()]

caminho_arquivo = input("Digite o caminho do arquivo: ")
vetor_original = ler_arquivo(caminho_arquivo)

vetor_selection = vetor_original.copy()
selection_antes = time.time()
selection_sort(vetor_selection)
selection_depois = time.time()
print(f"Selection Sort demorou o tempo de {(selection_depois - selection_antes) * 1000:.2f} ms")

vetor_insertion = vetor_original.copy()
insertion_antes = time.time()
insertion_sort(vetor_insertion)
insertion_depois = time.time()
print(f"Insertion Sort demorou o tempo de {(insertion_depois - insertion_antes) * 1000:.2f} ms")
