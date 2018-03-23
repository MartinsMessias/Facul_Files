"""
    FUNÇÕES DO PROGRAMA
"""

from os import system, name  # Usado apenas para limpar a tela
from time import sleep  # Usado para deixar um delay entre os menus

produtos = []  # Lista onde serão salvos os dados de produtos
ht = 38 * '#'
limpatela = system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows

'''
    FUNÇÃO PARA VERIFICAR SE UM PRODUTO JÁ CONSTA NO CADASTRO
    E CASO ESTEJA, ATUALIZA SEUS DADOS, CASO NÃO, FAZ O CADASTRO 
'''


def cadastrarProduto():

    while True:
        print(f"\n{ht}\n{'[C A D A S T R A R   P R O D U T O]':^38}\n{ht}\n")

        code = int(input('[Código do produto\t]: '))

        for x in range(len(produtos)):
            if code in produtos:
                print('Já existe um produto com este código!!!\n')
                r = str(input('Deseja atualizar as informações? [s/n]')).lower()

                '''
                 FALTA TERMINAR AQUI ONDE DEVE ATUALIZAR AS INFORMAÇÕES DO PRODUTO
                 CASO JÁ EXISTA UM E O USUÁRIO DESEJE CADASTRAR NOVAMENTE
                '''
                if r == 'n':
                    break

        nome = str(input('[Nome do produto\t]: '))
        valor = float(input('[Valor de venda\t\t]$ '))
        estoqMin = int(input('[Estoque min\t\t]: '))
        estoqAtual = int(input('[Estoque atual\t\t]: '))
        produtos.append([code, nome, valor, estoqMin, estoqAtual])

        print(f"\n{'PRODUTO CADASTRADO COM SUCESSO':^38}\n")

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

    while True:
        listadecompra = list()
        preco = 0

        print(f"\n{ht}\n{'[R E A L I Z A R   V E N D A]':^38}\n{ht}\n")

        for x in range(len(produtos)):

            if buscarProduto(int(input('\n[Código do produto]-----[  '))):

                qtd = int(input(f"[Quantidade]{12*'-'}[  "))

                produtos[x][3] -= qtd  # Retirada de produtos do estoque

                listadecompra.append(produtos[x][2] * qtd)
                print('Lista ', listadecompra)

                preco = (sum(listadecompra))
                print('Preço ', preco)

            else:
                r = str(input('\n\tDeseja adicionar outro item? [S/n]: ')).lower()
                if r == 's':
                    continue
                else:
                    limpatela
                    break

            vlp = float(input(f"\n[Valor pago]{12*'-'}[  R$ "))

            print('[Troco     ]{0}[  R$ {1}\n[Total     ]{0}[  R$ {2}'
                  .format(12 * '-', abs(vlp - preco), preco))

        r = input('\n\tDeseja iniciar nova venda? [S/n]: ').lower()
        if r == 's':
            limpatela
            continue

        break


'''
    FUNÇÃO QUE BUSCA O PRODUTO PELO CÓDIGO
'''


def buscarProduto(codprod):
    e = False

    for x in range(len(produtos)):

        if codprod == produtos[x][0]:
            e = True  # Caso o produto esteja no cadastro e == True

            print('[Produto   ]{0}[  {1}\n[Valor     ]{0}[  R$ {2}'
                  .format(12 * '-', produtos[x][1], produtos[x][2]))
            return e

    if not e:  # Caso não receba True quer dizer que o produto não foi encontrado
        print(f"\n{'PRODUTO NÃO ENCONTRADO':^38}\n")
        return e
