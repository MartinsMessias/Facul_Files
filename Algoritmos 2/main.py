"""
    ALGORITMOS II - Trabalho 1

"""

import os               # Usado apenas para a função de limpar a tela
from time import sleep  # Usado para deixar um delay entre o menu

produtos = []  # Lista onde são salvos os dados de produtos
ht = 38 * '#'
hs = 8 * '.'


#################################################################
#   FUNÇÃO PARA VERIFICAR SE UM PRODUTO JÁ CONSTA NO CADASTRO   #
#   E CASO SIM, ATUALIZA SEUS DADOS, CASO NÃO, FAZ O CADASTRO   #
#################################################################

def cadastrarProduto():

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(f"\n{ht}\n{'[C A D A S T R A R   P R O D U T O]':^38}\n{ht}\n")

        code = int(input(f'[CÓDIGO DO PRODUTO]{hs}[ '))

        for i in produtos:
            if code == i[0]:
                print('\nJá existe um produto com este código!!!')
                r = str(input('\nDeseja atualizar as informações dele? [s/n]: ')).lower()
                if r == 'n':
                    menu()
                if r == 's':
                    produtos.remove(i)

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

        return menu()


#############################################################
#   FUNÇÃO PARA VERIFICAR SE UM PRODUTO EXISTE NO CADASTRO  #
#   E REALIZA A SUA VENDA CASO ENCONTRE                     #
#############################################################

def realizarVenda():

    os.system('cls' if os.name == 'nt' else 'clear')    # Limpa tela
    print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")
    preco = 0
    busca = buscarProduto(int(input(f'\n[CÓDIGO DO PRODUTO]{hs}[ ')))
    sp = lambda v: v * ' '

    while True:

        items = 0

        for produto in produtos:
            if busca:
                qtd = int(input(f"[QUANTIDADE{sp(7)}]{hs}[ "))
                produto[4] -= qtd  # Retirada de produtos do estoque
                preco += (produto[2] * qtd)
                print(f'\n[SUBTOTAL{sp(9)}]{hs}[ R$ {preco:.2f}')
                items += 1
                break

        r = str(input('\nDeseja adicionar outro item? [S/n]: ')).lower()
        if r == 's':
            busca = buscarProduto(int(input(f'\n[CÓDIGO DO PRODUTO]{hs}[ ')))
        else:
            break

        if items > 0:  # Somente se a quantidade de items for maior que 0 pergunta o valor pago

            vlp = float(input(f"\n[VALOR PAGO{sp(7)}]{hs}[ R$ "))

            print('[TROCO{3}]{0}[ R$ {1:.2f}\n\n[TOTAL{3}]{0}[ R$ {2:.2f}'
                  .format(hs, abs(vlp - preco), preco, sp(12)))

    r = input('\nDeseja iniciar nova venda? [S/n]: ').lower()
    if r == 's':
        realizarVenda()

    return menu()


##########################################
# FUNÇÃO QUE BUSCA O PRODUTO PELO CÓDIGO #
##########################################

def buscarProduto(codprod):

    sp = lambda v: v * ' '

    for produto in produtos:
        if codprod == produto[0] and produto[3] < produto[4]:
            print('[PRODUTO{3}]{0}[ {1}\n[EM ESTOQUE       ]{0}[ {5}\n[PREÇO{4}]{0}[ R$ {2:.2f}'
                  .format(hs, produto[1], produto[2], sp(10), sp(12), produto[4]))

            return True

    print(f"\n{'NENHUM PRODUTO FOI ENCONTRADO OU':^38}\n"
          f"\n{'ESTÁ ABAIXO DA QTD DE ESTOQUE MÍNIMO':^38}\n")

    return False


#####################
#   MENU PRINCIPAL  #
#####################

def menu():

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
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


menu()  # Chama o menu e inicia o programa
