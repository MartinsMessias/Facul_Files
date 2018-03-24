"""
    FUNÇÕES DO PROGRAMA
"""

from os import system, name  # Usado apenas para limpar a tela
from time import sleep  # Usado para deixar um delay entre os menus

produtos = []  # Lista onde serão salvos os dados de produtos
ht = 38 * '#'
hs = 8 * '-'
limpatela = system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows

'''
    FUNÇÃO PARA VERIFICAR SE UM PRODUTO JÁ CONSTA NO CADASTRO
    E CASO ESTEJA, ATUALIZA SEUS DADOS, CASO NÃO, FAZ O CADASTRO 
'''


def cadastrarProduto():

    while True:
        print(f"\n{ht}\n{'[C A D A S T R A R   P R O D U T O]':^38}\n{ht}\n")

        code = int(input(f'[CÓDIGO DO PRODUTO]{hs}[ '))

        for x in range(len(produtos)):
            if code in produtos[x]:
                print('\nJá existe um produto com este código!!!')
                r = str(input('\nDeseja atualizar as informações dele? [s/n]: ')).lower()

                #####################################################################
                # FALTA TERMINAR AQUI ONDE DEVE ATUALIZAR AS INFORMAÇÕES DO PRODUTO #
                # CASO JÁ EXISTA UM E O USUÁRIO DESEJE CADASTRAR NOVAMENTE          #
                #####################################################################

                if r == 'n':
                    break

        nome = str(input(f'[NOME DO PRODUTO  ]{hs}[ '))
        valor = float(input(f'[VALOR DE VENDA   ]{hs}[ R$ '))
        estoqMin = int(input(f'[ESTOQUE MÍNIMO   ]{hs}[ '))
        estoqAtual = int(input(f'[ESTOQUE ATUAL    ]{hs}[ '))
        produtos.append([code, nome, valor, estoqMin, estoqAtual])

        print(f"\n{'[  PRODUTO CADASTRADO COM SUCESSO  ]':^35}\n")

        sleep(0.5)

        r = str(input('\nDeseja cadastrar novo produto? [S/n]: ')).lower()

        if r == 's':
            limpatela
            continue
        else:
            break


'''
    FUNÇÃO PARA VERIFICAR SE UM PRODUTO EXISTE NO CADASTRO
    E REALIZA A SUA VENDA CASO ENCONTRE
'''


def realizarVenda():

    limpatela
    print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")
    preco = 0

    while True:

        for x in range(len(produtos)):

            busca = buscarProduto(int(input(f'\n[CÓDIGO DO PRODUTO]{hs}[ ')))
            if busca == True:
                qtd = int(input(f"[QUANTIDADE{7 * ' '}]{hs}[ "))
                produtos[x][3] -= qtd           # Retirada de produtos do estoque
                preco += (produtos[x][2] * qtd)
                print(f'\n[TOTAL PARCIAL    ]{hs}[ R$ {preco}')


            r = str(input('\n||\bDeseja adicionar outro item? [S/n]: ')).lower()
            if r == 's':
                continue
            else:
                vlp = float(input(f"\n[VALOR PAGO{7*' '}]{hs}[ R$ "))
                print('[TROCO{3}]{0}[ R$ {1}\n[TOTAL{3}]{0}[ R$ {2}'
                      .format(hs, abs(vlp - preco), preco, 12 * ' '))

            r = input('\nDeseja iniciar nova venda? [S/n]: ').lower()
            if r == 's':
                realizarVenda()
            else:
                return 0



# FUNÇÃO QUE BUSCA O PRODUTO PELO CÓDIGO

def buscarProduto(codprod):

    e = False
    for x in range(len(produtos)):

        if codprod == produtos[x][0]:
            e = True  # Caso o produto esteja no cadastro e == True

            print('[PRODUTO{3}]{0}[ {1}\n[VALOR{4}]{0}[ R$ {2}'
                  .format(hs, produtos[x][1], produtos[x][2], 10 * ' ', 12 * ' '))
            return e


    print(f"\n{'PRODUTO NÃO ENCONTRADO':^38}\n")
    return e