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
        
            

with open(input("Digite o nome do arquivo (exemplo: num.1000.1.in): "), 'r') as arquivo:
    linhas = arquivo.readlines()
    vetor = [int(linha.strip()) for linha in linhas]

antesSelection = time.time()
selection_sort(vetor)
depoisSelection = time.time()
totalSelection = (depoisSelection - antesSelection)*1000
print("tempo do selection sort: %0.2f ms" % totalSelection)

insertion_sort(vetor)
antesInsertion = time.time()
selection_sort(vetor)
depoisInsertion = time.time()
totalInsertion= (depoisInsertion - antesInsertion)*1000
print("tempo do insertion sort: %0.2f ms" % totalInsertion)

