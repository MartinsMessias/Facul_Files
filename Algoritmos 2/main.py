"""
    ALGORITMOS II - Trabalho 1

"""

import os               # Usado apenas para a função de limpar a tela
from time import sleep  # Usado para deixar um delay entre o menu

produtos = []  # Lista onde são salvos os dados de produtos
ht = 40 * '#'
hs = 8 * '.'
sp = lambda v: v * ' '

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
                else:
                    produtos.remove(i)  # Remove o produto na posição [i]

        nome = str(input(f'\n[NOME DO PRODUTO  ]{hs}[ ')).capitalize()
        valor = float(input(f'[VALOR DE VENDA   ]{hs}[ R$ '))
        estoqMin = int(input(f'[ESTOQUE MÍNIMO   ]{hs}[ '))
        while True:
            estoqAtual = int(input(f'[ESTOQUE ATUAL    ]{hs}[ '))
            if estoqAtual < estoqMin:
                print('\nEstoque atual abaixo do mínimo!!!\n')
                continue

            break

        produtos.append([code, nome, valor, estoqMin, estoqAtual])

        print(f"\n{'[  PRODUTO CADASTRADO COM SUCESSO  ]':^35}\n")

        sleep(0.5)

        r = str(input('\nDeseja cadastrar novo produto? [S/n]: ')).lower()

        if r == 's':
            return cadastrarProduto()

        return menu()


#############################################################
#   FUNÇÃO PARA VERIFICAR SE UM PRODUTO EXISTE NO CADASTRO  #
#   E REALIZA A SUA VENDA CASO ENCONTRE                     #
#############################################################

def realizarVenda():

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa tela
    print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")
    total = 0
    items = 0

    while True:
        code = int(input(f'\n[CÓDIGO DO PRODUTO]{hs}[ '))
        busca = buscarProduto(code)
        while True:
            for i in produtos:
                if code == i[0] and busca:
                    qtd = int(input(f"[QUANTIDADE{sp(7)}]{hs}[ "))
                    if qtd > i[4]:
                        print('\nQuantidade acima do disponível em estoque.\n')
                        continue
                    else:
                        total += (i[2] * qtd)
                        i[4] -= qtd     # Retirada de produtos do estoque
                        print(f'\n[SUBTOTAL{sp(9)}]{hs}[ R$ {total:.2f}')
                        items += 1
                        break
            break

        r = str(input('\nDeseja adicionar outro item? [S/n]: ')).lower()
        if r == 's':
            continue
        else:
            if items > 0:  # Somente se a quantidade de items for maior que 0 pergunta o valor pago
                while True:
                    vlp = float(input(f"\n[VALOR PAGO{sp(7)}]{hs}[ R$ "))
                    if vlp < total:
                        print('\nDinheiro insuficiente!!!\n')
                        continue
                    else:
                        print('[TROCO{3}]{0}[ R$ {1:.2f}\n\n[TOTAL{3}]{0}[ R$ {2:.2f}'
                              .format(hs, abs(vlp - total), total, sp(12)))
                        break
            break

    rs = input('\nDeseja iniciar nova venda? [S/n]: ').lower()
    if rs == 's':
        realizarVenda()


##########################################
# FUNÇÃO QUE BUSCA O PRODUTO PELO CÓDIGO #
##########################################

def buscarProduto(codprod):

    for produto in produtos:
        if codprod == produto[0] and produto[3] < produto[4]:
            print('[PRODUTO{3}]{0}[ {1}\n[EM ESTOQUE       ]{0}[ {5}\n[PREÇO{4}]{0}[ R$ {2:.2f}'
                  .format(hs, produto[1], produto[2], sp(10), sp(12), produto[4]))

            return True     # Retorna verdadeiro caso encontre

    print(f"\n{'NENHUM PRODUTO FOI ENCONTRADO OU':^38}\n"
          f"\n{'ESTÁ ABAIXO DA QTD DE ESTOQUE MÍNIMO':^38}\n")

    return False    # Retorna falso caso não encontre



#####################
#   MENU PRINCIPAL  #
#####################

def menu():

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')    # Limpa a tela
        print('''
   ██████╗ █████╗ ██╗██╗  ██╗ █████╗ 
  ██╔════╝██╔══██╗██║╚██╗██╔╝██╔══██╗
  ██║     ███████║██║ ╚███╔╝ ███████║
  ██║     ██╔══██║██║ ██╔██╗ ██╔══██║
  ╚██████╗██║  ██║██║██╔╝ ██╗██║  ██║
   ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝''')
        resp = int(input('{0}\n\n'
                         '\t[1] - Cadastrar produto\n'
                         '\t[2] - Realizar venda\n\n'
                         '\t[0] - Sair\n\n{0}\n:: '
                         .format(ht)))
        if resp == 1: cadastrarProduto()
        elif resp == 2: realizarVenda()
        elif resp == 0: exit()
        elif resp == 2018:
            print('\n\t[ Criadores ]\n'
                  '\nEddie Giovanne\nIgor Melo\nBruno'
                  '\nMessias Martins\nWilliam dos Santos')
            input('\n\t[ENTER]')
        else:
            print(f"{'[ OPÇÃO INVÁLIDA!!! ]':^38}")
            sleep(1)
            continue


menu()  # Inicia o programa e chama o menu
