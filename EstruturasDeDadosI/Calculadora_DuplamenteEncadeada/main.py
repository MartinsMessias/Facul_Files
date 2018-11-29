from Calculadora import *

print(f"{'-'*30}\n\tC A L C U L A D O R A\n{'-'*30}")

while True:
    num_1 = input('N1: ')
    num_2 = input('N2: ')

    proc_ = Calculadora(num_1, num_2)

    op = input('\nSomar\t[SM]\nSubtrair\t[SB]\nDividir\t[DV]\nMultiplicar\t[MT]\n>>> ')

    if op == 'sm':
        if num_1.isdecimal() and num_2.isdecimal():
            mostrar(proc_.somar())
        else:
            proc_.somar()
    elif op == 'sb':
        pass
        # proc_.subtrair()
    elif op == 'dv':
        pass
        # proc_.dividir()
    elif op == 'mt':
        proc_.multiplicar()

    op_f = input('\n\nRepetir? (S/n): ').lower()
    if op_f != 's':
        break

