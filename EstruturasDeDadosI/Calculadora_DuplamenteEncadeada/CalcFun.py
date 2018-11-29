from ListaDuplamenteEncadeada import *


#########################################
#       FUNÇÕES DA CALCULADORA          #
#########################################

# Divide uma lista duplamente encadeada (Mesma função do split em strings).
def dividir_(lista, str):
    d = lista

    a = ListaDuplamenteEncadeada()
    b = ListaDuplamenteEncadeada()

    for c in d:
        if c != str:
            a.inserir_inicio(c)
            d.remover_primeiro()
        if c == str:
            d.remover_primeiro()
            break

    for c in d:
        b.inserir_inicio(c)
        d.remover_primeiro()

    inverter_lista(a)
    inverter_lista(b)
    return a, b


# Transforma uma lista duplamente enc em uma string

def lista_para_str(lis):
    strg = ''
    for x in lis:
        strg = strg + x
    return strg


# Fatia uma string e insere cada valor em uma posição da lista duplamente encadeada.
def fatiar_pra_lista(st):
    nova_lista = ListaDuplamenteEncadeada()
    for caracter in st:
        nova_lista.inserir_inicio(caracter)
    return nova_lista


# Retorna o tamanho de uma string (Mesma função do len())
def tamanho_str(x):
    len = 0
    for _ in x:
        len += 1
    return len

# Retorna o maior entre dois inteiros
def maior_int(v1, v2):
    mai = v1

    if v2 > v1:
        mai = v2

    return mai


# Retorna o tamanho de uma lista duplamente enc
def tamanho_lst(x):
    len = 0
    for _ in x:
        len += 1

    return len


# Mostra cada valor de uma lista duplamente encadeada.
def mostrar(x):
    for i in x:
        print(i, end='')


# Retorna o tipo da variavel
def retorna_tipo(n):
    for i in n:
        if i == '.':
            return 'Float'
        elif i == '-':
            return 'Negativo'
    return 'Inteiro'


# Retorna a posição onde esta o ponto flutuante em uma lista duplamente enc.
def posicao_do_ponto_fl(numero):
    posicao = -1
    numero = inverter_lista(numero)
    for i in numero:
        posicao += 1
        if i == '.':
            return posicao
    return 0


# Inverte a posição dos valores em uma lista duplamente enc.
def inverter_lista(l1):
    l = ListaDuplamenteEncadeada()
    for x in l1:
        l.inserir_inicio(x)
    return l


