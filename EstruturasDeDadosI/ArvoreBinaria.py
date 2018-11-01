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

# By Messias Martins

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
    print('Árvore atual em ordem: ', end='')
    try:
        em_ordem(arvore)
        print('\nRAIZ: ', arvore.chave)
    except AttributeError:
        print('Árvore inexistente')

    print('\n' + '_' * 50)
    p = input('\nINSERIR\t - [i/I]\nREMOVER\t - [r/R]\nSAIR\t - [s/S]\n>>> ').lower()

    if p == 's':
        break
    elif p == 'r':
        arvore = remover(arvore, int(input('Valor a ser removido: ')))
        pass
    elif p == 'i':
        arvore = insere(arvore, int(input('\nValor a ser inserido: ')))
