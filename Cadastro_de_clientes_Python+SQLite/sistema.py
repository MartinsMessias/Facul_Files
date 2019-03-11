#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

'''
| CADASTRO DE CLIENTES | Trabalho 1

[Github] https://github.com/MartinsMessias
'''

# Módulos necessários
import sqlite3
from cores import Azul, CorNull, INBlue, INRed, URed, FAIWhite
from os import system
from time import sleep



# Diminuindo tamanho dos nomes das cores
Az = Azul  # Az
Re = URed  # Vermelho sublinhado
CN = CorNull  # Tirar cor
INB = INBlue  # Az intenso negrito
INR = INRed  # Vermelho intenso negrito
FDb = FAIWhite  # Fundo branco

# Conectando-se ao banco de dados...
conn = sqlite3.connect(':memory:') # Use 'clientes.db' caso queira dados persistentes

# Definindo cursor...
cursor = conn.cursor()

# Criando tabela se ainda não existe
cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR NOT NULL,
                cpf VARCHAR(14) NOT NULL,
                telefone varchar(20));""")


# Funções do programa
def funcoesOp(opcao):
    
    if opcao == 1:
        nome = str(input('{}\n[ NOME ]: {}'.format(INR, CN))).strip()
        cpf = str(input('{}\n[ CPF  ]: {}'.format(INR, CN))).strip()
        telefone = str(input('{}\n[ TEL  ]: {}'.format(INR, CN))).strip()

        # Inserindo dados na tabela

        info = [(nome, cpf, telefone)]

        cursor.executemany("""
                INSERT INTO clientes (nome, cpf, telefone)
                VALUES (?,?,?)""", info)
        conn.commit()

        print('\n{}[ DADOS INSERIDOS COM SUCESSO ]{}'.format(INR, CN))

        retornaMenu()

    elif opcao == 2:
        if verificaDB() == True:
            alteraInfo()
            retornaMenu()

    elif opcao == 3:
        if verificaDB() == True:
            cpf = input('{}\nDigite o CPF: {}'.format(INR, CN)).strip()
            consultaInfo(cpf)
            retornaMenu()

    elif opcao == 4:
        if verificaDB() == True:
            cursor.execute("""SELECT * FROM clientes;""")
            ordenaLista(cursor.fetchall())
            retornaMenu()

    elif opcao == 5:
        if verificaDB() == True:
            excluiCli()

    elif opcao == 0:
        print('\n{}Saíndo...{}'.format(INR, CN))

        # Fechando conexão com banco de dados
        conn.close()
        exit()

    else:
        print('Opção Inválida!!!')
        menuPrincipal()


def menuPrincipal():
    # Menu principal

    system('clear')

    print(INB, 10 * '=', '|- : ', INR, 'MENU PRINCIPAL', CN, INB, ' : -|', 10 * '=', '\n', CN, Az,
          '''

        [1] - Adicionar novo
        [2] - Alterar informações
        [3] - Cosultar informações
        [4] - Consultar todos
        [5] - Excluir
        [0] - Sair
        
''', INB, 50 * '=', CN, '\n')

    opcao = int(input('{}[OPÇÃO]: {}'.format(INR, CN)))
    funcoesOp(opcao)


def retornaMenu():
    op = str(input('\n\t{2}[  OPÇÕES  ]\n\n\t'
                   '{0}ALTERAR INFOMAÇÕES{1}  {2}[1]\n\t'
                   '{0}EXCLUIR CADASTRO{1}    {2}[2]\n\n\t'
                   '{0}Para voltar ao menu pressione {2}[ENTER]\n\t--: {1}'.format(INB, CN, INR))).strip()
    system('clear')

    if op == '1': 
        alteraInfo()
    if op == '2':
        excluiCli()
    else:
        menuPrincipal()


def ordenaLista(line):
    print('\n' + INB + 3 * '=' + INR + '[ LISTA DE CADASTROS ]' + INB + 15 * '=' + CN + '\n')

    for linha in line:
        sleep(0.3)
        id, nome, cpf, telefone = linha

        print(44 * '{}_{}'.format(Re, CN))
        print(INR, ' [ ID   ]-', Az, '-[', id, ']')
        print(INR, ' [ NOME ]-', INB, '-[', nome)
        print(INR, ' [ CPF  ]-', INB, '-[', cpf, )
        print(INR, ' [ TEL  ]-', INB, '-[', telefone, CN)
        print(44 * '{}_{}'.format(Re, CN))


def consultaInfo(cpf):
    info = [(cpf)]

    # Lendo os dados do banco de dados
    cursor.execute("""
                    SELECT * FROM clientes
                    WHERE cpf = ?""", info)
    conn.commit()

    ordenaLista(cursor.fetchall())


def alteraInfo():
    cpf = input('{}\nDigite o CPF: {}'.format(INR, CN)).strip()
    consultaInfo(cpf)

    print(INR, '''\n
                [Nome    ][1]
                [CPF     ][2]
                [Telefone][3]

            Escolha uma ou mais opções pelo número\n\t Ex: 1 2 3
            \n''', CN)

    info = str(input('\t{}[OPÇÃO]: {}'.format(INR, CN))).strip()
    info = list(info)

    if '1' in info:
        nome = str(input('\n{}[Novo nome]:{} '.format(INB, CN))).strip()
        cursor.execute("""UPDATE clientes SET nome = ? WHERE cpf = ?""", (nome, cpf))
        conn.commit()

    if '2' in info:
        cpfnovo = str(input('\n{}[Novo CPF]:{} '.format(INB, CN))).strip()
        cursor.execute("""UPDATE clientes SET cpf = ? WHERE cpf = ?""", (cpfnovo, cpf))
        conn.commit()
        cpf = cpfnovo

    if '3' in info:
        telefone = str(input('\n{}[Novo telefone]:{} '.format(INB, CN))).strip()
        cursor.execute("""UPDATE clientes SET telefone = ? WHERE cpf = ?""", (telefone, cpf))
        conn.commit()

    consultaInfo(cpf)
    print(INR, '\n[ ATUALIZADO COM SUCESSO ]', CN)


def excluiCli():
    cpf = input('{}\nDigite o CPF: {}'.format(INR, CN)).strip()
    consultaInfo(cpf)

    id = input('{}\nDigite o ID do cliente a ser excluido: {}'.format(INR, CN)).strip()
    test = input('{}\nTens certeza que deseja excluir? (S/n): {}'.format(INR, CN)).strip().lower()

    if test == 's':
        # excluindo um registro da tabela
        cursor.execute("""DELETE FROM clientes WHERE id = ?""", (id))
        conn.commit()

        print('\n{}[ REMOVIDO COM SUCESSO ]{}'.format(INR, CN))

    retornaMenu()


def verificaDB():
    cursor.execute("""SELECT id FROM clientes;""")
    lista = cursor.fetchall()

    i = 0
    
    for linha in lista:
        i += 1
    
    if i <= 0:
        print('\n\t{}[ BANCO DE DADOS ESTÁ VÁZIO ]{}'.format(INR, CN))
        input('Para voltar ao menu pressione {0}[ENTER]{1}'.format(INB, CN))
        
        menuPrincipal()
    
    return True
