import sys

# Aumentar o limite de recursão para evitar erros de limite em labirintos grandes
sys.setrecursionlimit(2000)

class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return not bool(self.items)

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("Desempilhar de uma pilha vazia.")
        return self.items.pop()
    
# --- Função de resolução do labirinto ---
def resolver_labirinto(labirinto):
 
    #Retorna True se o tesouro for encontrado, False caso contrário.
    
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    
    # Encontra a posição inicial do jogador (marcada com '2')
    posicao_inicial = None
    for r in range(linhas):
        for c in range(colunas):
            if labirinto[r][c] == 2:
                posicao_inicial = (r, c)
                break
        if posicao_inicial:
            break
    
    if not posicao_inicial:
        print("Posição inicial não encontrada.")
        return False
        
    pilha = Pilha()
    visitados = set() # Usamos um conjunto para rastrear posições visitadas
    
    # Insere a posição inicial na pilha e a marca como visitada
    pilha.empilhar(posicao_inicial)
    visitados.add(posicao_inicial)
    
    while not pilha.esta_vazia():
        posicao_atual = pilha.desempilhar()
        linha, coluna = posicao_atual
        
        # --- Se a posição atual for o tesouro, o caminho foi encontrado! ---
        if labirinto[linha][coluna] == 'T':
            print("Tesouro encontrado!")
            return True
            
        # --- Examine as posições adjacentes (cima, baixo, esquerda, direita) ---
        movimentos_possiveis = [(0, 1), (0, -1), (1, 0), (-1, 0)] # (linha, coluna)
        
        for dr, dc in movimentos_possiveis:
            proxima_linha, proxima_coluna = linha + dr, coluna + dc
            proxima_posicao = (proxima_linha, proxima_coluna)
            
            # --- Verifica se a próxima posição é válida ---
            if (0 <= proxima_linha < linhas and 
                0 <= proxima_coluna < colunas and
                proxima_posicao not in visitados and
                labirinto[proxima_linha][proxima_coluna] != 1): # Não é parede
                
                # Insere a nova posição na pilha e a marca como visitada
                pilha.empilhar(proxima_posicao)
                visitados.add(proxima_posicao)

    # Se a pilha esvaziar e o tesouro não tiver sido encontrado, não há caminho
    print("Caminho para o tesouro não encontrado.")
    return False

# --- Exemplo de Labirinto ---
# 0 = caminho livre, 1 = parede, 2 = inicio, 'T' = tesouro
labirinto_exemplo = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 'T', 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# Executa o algoritmo para resolver o labirinto
resolver_labirinto(labirinto_exemplo)

