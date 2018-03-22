from funcoes import *  # Módulo das funçoes do programa


while True:
    system('cls' if name == 'nt' else 'clear')  # Limpa a tela em GNU/Linux e Windows

    print(f"{ht}\n{'[ M E N U   P R I N C I P A L ]':^38}\n{ht}\n")
    resp = int(input('\n'
                     '\t[1] - Cadastrar produto\n'
                     '\t[2] - Realizar venda\n\n'
                     '\t[0] - Sair\n\n{}\n::'
                     .format(ht)))

    if resp == 1:
        cadastrarProduto()
    elif resp == 2:
        realizarVenda()
    elif resp == 0:
        break
    else:
        print('Opção inválida')
        continue
