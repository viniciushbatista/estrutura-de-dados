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
        
            

with open(input("Digite o caminho do arquivo: "), 'r') as arquivo:
    linhas = arquivo.readlines()
    vetor = [int(linha.strip()) for linha in linhas]

antesSelection = time.time()
selection_sort(vetor)
depoisSelection = time.time()
totalSelection = (depoisSelection - antesSelection)*1000

print("tempo do selection sort inicial: %0.2f ms" % antesSelection)
print("tempo do selection sort final: %0.2f ms" % depoisSelection)
print("tempo do selection sort total: %0.2f ms" % totalSelection)
print()

insertion_sort(vetor)
antesInsertion = time.time()
selection_sort(vetor)
depoisInsertion = time.time()
totalInsertion= (depoisInsertion - antesInsertion)*1000
print("tempo do Insertion sort inicial: %0.2f ms" % antesInsertion)
print("tempo do Insertion sort final: %0.2f ms" % depoisInsertion)
print("tempo do Insertion sort total %0.2f ms" % totalInsertion)
