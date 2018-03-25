"""
    ALGORITMOS II - Trabalho 1

"""

import os               # Usado apenas para a função de limpar a tela
from time import sleep  # Usado para deixar um delay entre os menus

produtos = []           # Lista onde são salvos os dados de produtos
ht = 38 * '#'
hs = 8 * '.'




#################################################################
#   FUNÇÃO PARA VERIFICAR SE UM PRODUTO JÁ CONSTA NO CADASTRO   #
#   E CASO SIM, ATUALIZA SEUS DADOS, CASO NÃO, FAZ O CADASTRO   #
#################################################################

def cadastrarProduto():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows
        print(f"\n{ht}\n{'[C A D A S T R A R   P R O D U T O]':^38}\n{ht}\n")

        code = int(input(f'[CÓDIGO DO PRODUTO]{hs}[ '))
        for x in range(len(produtos)):
            if code in produtos[x]:
                print(produtos[x].index(code))
                print('\nJá existe um produto com este código!!!')
                r = str(input('\nDeseja atualizar as informações dele? [s/n]: ')).lower()

                #####################################################################
                # FALTA TERMINAR AQUI ONDE DEVE ATUALIZAR AS INFORMAÇÕES DO PRODUTO #
                # CASO JÁ EXISTA UM E O USUÁRIO DESEJE CADASTRAR NOVAMENTE          #
                #####################################################################

                if r == 'n':
                    menu()

        nome = str(input(f'[NOME DO PRODUTO  ]{hs}[ '))
        valor = float(input(f'[VALOR DE VENDA   ]{hs}[ R$ '))
        estoqMin = int(input(f'[ESTOQUE MÍNIMO   ]{hs}[ '))
        estoqAtual = int(input(f'[ESTOQUE ATUAL    ]{hs}[ '))
        produtos.append([code, nome, valor, estoqMin, estoqAtual])

        print(f"\n{'[  PRODUTO CADASTRADO COM SUCESSO  ]':^35}\n")

        sleep(0.5)

        r = str(input('\nDeseja cadastrar novo produto? [S/n]: ')).lower()

        if r == 's':
            cadastrarProduto()
        else:
            return menu()



#############################################################
#   FUNÇÃO PARA VERIFICAR SE UM PRODUTO EXISTE NO CADASTRO  #
#   E REALIZA A SUA VENDA CASO ENCONTRE                     #
#############################################################

def realizarVenda():

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")
    preco = 0
    busca = buscarProduto()

    while True:

            for x in range(len(produtos)):
                if busca:
                    qtd = int(input(f"[QUANTIDADE{7 * ' '}]{hs}[ "))
                    produtos[x][3] -= qtd           # Retirada de produtos do estoque
                    preco += (produtos[x][2] * qtd)
                    print(f'\n[SUBTOTAL         ]{hs}[ R$ {preco:.2f}')
                    continue
                if not busca:
                     break

            r = str(input('\nDeseja adicionar outro item? [S/n]: ')).lower()
            if r == 's':
                if buscarProduto():
                    continue
            else:
                continue

            vlp = float(input(f"\n[VALOR PAGO{7*' '}]{hs}[ R$ "))
            print('[TROCO{3}]{0}[ R$ {1:.2f}\n\n[TOTAL{3}]{0}[ R$ {2:.2f}'
                    .format(hs, abs(vlp - preco), preco, 12 * ' '))

            r = input('\nDeseja iniciar nova venda? [S/n]: ').lower()
            if r == 's':
                realizarVenda()
            else:
                menu()



##########################################
# FUNÇÃO QUE BUSCA O PRODUTO PELO CÓDIGO #
##########################################

def buscarProduto():

    codprod = int(input(f'\n[CÓDIGO DO PRODUTO]{hs}[ '))
    for x in range(len(produtos)):
        if codprod == produtos[x][0]:
            print('[PRODUTO{3}]{0}[ {1}\n[PREÇO{4}]{0}[ R$ {2:.2f}'
                  .format(hs, produtos[x][1], produtos[x][2], 10 * ' ', 12 * ' '))
            return True

    print(f"\n{'NENHUM PRODUTO FOI ENCONTRADO':^38}\n")
    return False




#####################
#   MENU PRINCIPAL  #
#####################

def menu():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows
        print(f"{ht}\n{'[ M E N U   P R I N C I P A L ]':^38}\n{ht}\n")
        resp = int(input('\n'
                         '\t[1] - Cadastrar produto\n'
                         '\t[2] - Realizar venda\n\n'
                         '\t[0] - Sair\n\n{}\n:: '
                         .format(ht)))
        if resp == 1:
            cadastrarProduto()
        elif resp == 2:
            realizarVenda()
        elif resp == 0:
            exit()
        else:
            print(f"{'[ OPÇÃO INVÁLIDA!!! ]':^38}")
            sleep(1)
            continue

menu()