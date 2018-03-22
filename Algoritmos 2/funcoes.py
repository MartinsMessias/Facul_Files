"""
    FUNÇÕES DO PROGRAMA
"""

from os import system, name  # Usado apenas para limpar a tela
from time import sleep       # Usado para deixar um delay entre os menus

produtos = []   # Lista onde serão salvos os dados de produtos
ht = 38 * '#'
limpatela = system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows


def cadastrarProduto():

    while True:
        print(f"\n{ht}\n{'[C A D A S T R A R   P R O D U T O]':^38}\n{ht}\n")

        code = int(input('[Código do produto\t]: '))

        if code in produtos:
            print('Já existe um produto com este código!!!\n')
            r = str(input('Deseja atualizar as informações? [s/n]')).lower()
            if r == 'n': break

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

        sleep(0.5)

        r = str(input('\nDeseja cadastrar novo produto? [S/n]: ')).lower()
        if r == 's':
            limpatela
            continue
        else:
            break


def realizarVenda():

    print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")

    codprod = int(input('[Código do produto]--[  '))
    if codprod in produtos:
        local = produtos.index(codprod)
        print(f"[Produto]{12 * '-'}[  {produtos[local + 1]}")
        print(f"[Valor  ]{12 * '-'}[  R$ {produtos[local + 2]}")
    input('\n\tEnter para continuar ')
    limpatela
