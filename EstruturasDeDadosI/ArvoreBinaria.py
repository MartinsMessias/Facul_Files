##################################################
# > Árvore binária                               #
# Funções: Inserção, Remoção, Impressão em ordem #
##################################################
class NoArvore:

    # Construtor para criar um novo nó
    def __init__(self, chave=None):
        self.chave = chave
        self.esquerda = None
        self.direita = None


#################################################
# Função para imprimir em ordem.                #
#################################################
def em_ordem(no):
    if no is not None:
        em_ordem(no.esquerda)
        print('(' + str(no.chave) + ')', end=' ')
        em_ordem(no.direita)

#################################################
# Função para imprimir em pré-ordem.            #
#################################################
def pre_ordem(no):
    if no is not None:
        print('(' + str(no.chave) + ')', end=' ')
        pre_ordem(no.esquerda)
        pre_ordem(no.direita)

#################################################
# Função para imprimir em pós-ordem.            #
#################################################
def pos_ordem(no):
    if no is not None:
        pos_ordem(no.esquerda)
        pos_ordem(no.direita)
        print('(' + str(no.chave) + ')', end=' ')
        
#################################################
# Função para inserir um nó em uma árvore.      #
#################################################
def insere(raiz, chave):
    # Se a árvore é vazia, retorna um novo nó
    if raiz is None:
        return NoArvore(chave)
    # Caso contrário, recorre a árvore
    elif raiz.chave > chave:
        raiz.esquerda = insere(raiz.esquerda, chave)
    else:
        raiz.direita = insere(raiz.direita, chave)
    # retorna o ponteiro do nó (inalterado)
    return raiz
    
    
#################################################
# Função para buscar um valor.                  #
#################################################
def busca(raiz, chave):
    # Procura por uma chave em uma árvore binária.
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    # A chave procurada é menor que a da raiz.
    return busca(raiz.esquerda, chave)

#################################################
# Função para saber se 2 árvores são identicas. #
#################################################
def identicas(a, b):
    # 1. As duas árvores são vazias.
    if a is None and b is None:
        return True

    # 2. Nenhuma das árvores é vazia. Precisamos compará-las.
    if a is not None and b is not None:
        return ((a.chave == b.chave) and
                identicas(a.esquerda, b.esquerda) and
                identicas(a.direita, b.direita))

    # 3. Uma árvore é vazia mas a outra não.
    return False

#################################################
# Função para saber se a árvore é simétrica.    #
#################################################
def checa_simetrica(raiz):
    def simetricas(subarvore_esq, subarvore_dir):
        if not subarvore_esq and not subarvore_dir:
            return True
        elif subarvore_esq and subarvore_dir:
            return (subarvore_esq.chave == subarvore_dir.chave and
                    simetricas(subarvore_esq.esquerda, subarvore_dir.direita) and
                    simetricas(subarvore_esq.direita, subarvore_dir.esquerda))
        # Uma sub-árvore é vazia e a outra não.
        return False

    return not raiz or simetricas(raiz.esquerda, raiz.direita)

    
#################################################
# Função para saber se uma árvore é balanceada. #
#################################################
def balanceada(raiz):
    # Uma árvore binária vazia é balanceada.
    if raiz is None:
        return True

    altura_esq = altura(raiz.esquerda)
    altura_dir = altura(raiz.direita)
    # Alturas diferem em mais de uma unidade.
    if abs(altura_esq - altura_dir) > 1:
        return False

    return balanceada(raiz.esquerda) and balanceada(raiz.direita)

#################################################
# Função para saber a altura.                   #
#################################################
def altura(raiz):
    if raiz is None:
        return 0
    return max(altura(raiz.esquerda), altura(raiz.direita)) + 1


#################################################
# Função para saber qual o maior valor.         #
#################################################
def maior_valor(raiz):
    no = raiz
    while no.direita is not None:
        no = no.direita
    return no.chave

#################################################
# Função para saber qual o menor valor.         #
#################################################
def menor_valor1(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave
    

# PRA USAR NA REMOÇÃO!

#################################################
# Função para saber qual o menor valor.         #
#################################################
# Em uma árvore não vazia, retorna o nó com o
# valor de chave mínimo encontrado nessa árvore.
def menor_valor(no):
    atual = no
    # loop até encontrar a folha mais à esquerda
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

#################################################

#################################################
# Função para remover um nó da árvore.          #
#################################################
def remover(raiz, chave):
    # Caso base
    if raiz is None:
        return raiz

    # Se a chave a ser apagada é menor que a raíz
    # então a chave fica à esquerda.
    if chave < raiz.chave:
        raiz.esquerda = remover(raiz.esquerda, chave)

    # Se a chave a ser apagada é maior que a raíz
    # então a chave fica à direita.
    elif chave > raiz.chave:
        raiz.direita = remover(raiz.direita, chave)

    # Se a chave é igual à chave da raiz, então esse é
    # o nó para ser deletado
    else:

        # Nó com apenas um filho ou sem filho
        if raiz.esquerda is None:
            substituto = raiz.direita
            raiz = None
            return substituto
        elif raiz.direita is None:
            substituto = raiz.esquerda
            raiz = None
            return substituto

        # Nó com dois filhos: obter o sucessor na ordem
        # (menor da sub-árvore direita)
        temporario = menor_valor(raiz.direita)

        # Copiar o conteúdo do sucessor em ordem para este nó
        raiz.chave = temporario.chave

        # Excluir o sucessor interno
        raiz.direita = remover(raiz.direita, temporario.chave)

    return raiz


#######################################################
####################   EXECUÇÃO   #####################
#######################################################

arvore = NoArvore(int(input('\nValor raíz: ')))

while True:
    # Para evitar erro quando árvore é vazia.
    try:
      print('Árvore atual em ordem: ', end='')
      em_ordem(arvore)
      print('\nÁrvore atual em pre_ordem: ', end='')
      pre_ordem(arvore)
      print('\nÁrvore atual em pre_ordem: ', end='')
      pos_ordem(arvore)
      print('\nMenor chave: ', menor_valor1(arvore.esquerda))
      print('Maior chave: ', maior_valor(arvore.direita))
      #print('\nIdenticas :', identicas(raiz, raiz))
      print('Altura da árvore: ', altura(arvore))
      print('Balanceada: ', balanceada(arvore))
      print('Simetrica: ', checa_simetrica(arvore))
      print('\nRAIZ: ', arvore.chave)
    except AttributeError:
        print('?\n')

    print('\n' + '_' * 50)
    p = input('\nINSERIR\t - [i/I]\nBUSCAR\t - [b/B]\nREMOVER\t - [r/R]\nSAIR\t - [s/S]\n>>> ').lower()

    if p == 's':
        break
    elif p == 'r':
        arvore = remover(arvore, int(input('Valor a ser removido: ')))
    elif p == 'i':
        arvore = insere(arvore, int(input('\nValor a ser inserido: ')))
    elif p == 'b':
        chave = int(input('Buscar por: '))
        resultado = busca(arvore, chave)
        if resultado:
            print("\nBusca pela chave {}: OK!".format(chave))
        else:
            print("\nBusca pela chave {}: FALHA!".format(chave))
