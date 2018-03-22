"""
    FUNÇÕES DO PROGRAMA
"""

from os import system, name  # Usado apenas para limpar a tela
from time import sleep       # Usado para deixar um delay entre os menus

produtos = []   # Lista onde serão salvos os dados de produtos
ht = 38 * '#'


def cadastrarProduto():

    system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows

    while True:
        print(f"\n{ht}\n{'[C A D A S T R A R   P R O D U T O]':^38}\n{ht}\n")

        code = int(input('[Código do produto\t]: '))
        nome = str(input('[Nome do produto\t]: '))
        valor = float(input('[Valor de venda\t\t]$ '))
        estoqMin = int(input('[Estoque min\t\t]: '))
        estoqAtual = int(input('[Estoque atual\t\t]: '))

        produtos.append(code)
        produtos.append(nome)
        produtos.append(valor)
        produtos.append(estoqMin)
        produtos.append(estoqAtual)
        print(f"\n{'PRODUTO CADASTRADO COM SUCESSO':^38}\n")

        sleep(1)

        r = str(input('\nDeseja cadastrar novo produto? [S/n]: ')).lower()
        if r == 's':
            continue
        else:
            break

        system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows


def realizarVenda():

    system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows

    print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")

    codprod = int(input('[Código do produto]--[  '))
    if codprod in produtos:
        local = produtos.index(codprod)
        print(f"[Produto]{12 * '-'}[  {produtos[local + 1]}")
        print(f"[Valor  ]{12 * '-'}[  R$ {produtos[local + 2]}")
