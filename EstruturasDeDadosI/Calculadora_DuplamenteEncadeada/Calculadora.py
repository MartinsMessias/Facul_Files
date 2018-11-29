# Importando as funções...
from CalcFun import *

class Calculadora(object):

    def __init__(self, v1, v2):

        self.n1 = v1.replace(',', '.')
        self.n2 = v2.replace(',', '.')

        self.n1_tipo = retorna_tipo(self.n1)
        self.n2_tipo = retorna_tipo(self.n2)

        self.n1_fat = fatiar_pra_lista(self.n1)
        self.n2_fat = fatiar_pra_lista(self.n2)

    """
	____________________________________________
    FUNÇÃO PARA SOMAR DUAS LISTAS DUPLAMENTE ENC
	____________________________________________
	"""

    def somar(self):

        if self.n1_tipo == 'Float' or self.n2_tipo == 'Float':
            return self.somar_float()

        atual_n1 = self.n1_fat.primeiro
        atual_n2 = self.n2_fat.primeiro

        resposta = ListaDuplamenteEncadeada()
        sobe = 0
        soma = 0

        while atual_n1 or atual_n2:

            if atual_n1 and atual_n2:
                soma = str(int(atual_n1.dado) + int(atual_n2.dado) + sobe)

                atual_n1 = atual_n1.proximo
                atual_n2 = atual_n2.proximo

            elif atual_n1 and atual_n2 is None:

                soma = str(int(atual_n1.dado) + sobe)

                atual_n1 = atual_n1.proximo

            elif atual_n1 is None and atual_n2:

                soma = str(int(atual_n2.dado) + sobe)

                atual_n2 = atual_n2.proximo

            if int(soma) >= 10:
                sobe = int(soma[-2])
                resposta.inserir_inicio(soma[-1])
            else:
                resposta.inserir_inicio(soma)

        if sobe > 0:
            resposta.inserir_inicio(str(sobe))

        return resposta

    def somar_float(self):

        global rsp1, rsp2

        a1, a2 = dividir_(self.n1_fat, '.')
        b1, b2 = dividir_(self.n2_fat, '.')

        a1 = lista_para_str(a1)
        a2 = lista_para_str(a2)
        b1 = lista_para_str(b1)
        b2 = lista_para_str(b2)

        if a2 == '0' and tamanho_str(a1) > tamanho_str(b1):
            b1 = b1 + '0'
        if b2 == '0' and tamanho_str(b1) > tamanho_str(a1):
            a1 = a1 + '0'

        gb_1 = False

        if a1 and a2:
            if b1 and not b2:
                rsp1 = Calculadora(a2, b1)
                rsp2 = Calculadora(a1, b2)
                gb_1 = True
            else:
                rsp1 = Calculadora(a1, b1)
                rsp2 = Calculadora(a2, b2)
        elif a1 and not a2:
            rsp1 = Calculadora(a1, b2)
            rsp2 = Calculadora(a2, b1)
            gb_1 = True

        rsp1 = rsp1.somar()
        rsp2 = rsp2.somar()

        t1 = lista_para_str(rsp1)
        t2 = lista_para_str(rsp2)

        if int(t2) > 10 and gb_1:
            print(t1 + '.' + t2)
            return

        if 5 <= int(t2) <= 11:
            soma = int(t2) + int(str(int(t1) / 10)[0])
            t1 = str(soma)
            t2 = str(int(t1) / 10)[2]

            if str(int(t1) / 10)[0] == '0':
                print(t1)
                return

        if gb_1:
            print(t1 + '.' + t2)
        else:
            print(t2 + '.' + t1)
        return

    """
	__________________________________________________
    FUNÇÃO PARA MULTIPLICAR DUAS LISTAS DUPLAMENTE ENC
	__________________________________________________
	"""

    def multiplicar(self):

        self.n1_fat = fatiar_pra_lista(self.n1)
        self.n2_fat = fatiar_pra_lista(self.n2)

        resposta = ListaDuplamenteEncadeada()

        if int(self.n1) < 10 or int(self.n2) < 10:

            for atual_n2 in self.n1_fat:
                for atual_n1 in self.n2_fat:
                    resposta.inserir_inicio(str(int(atual_n1) * int(atual_n2)))

            return mostrar(resposta)

        else:
            pass

    """
	________________________________________________
    FUNÇÃO PARA SUBTRAIR DUAS LISTAS DUPLAMENTE ENC
	_______________________________________________
	"""

    def subtrair(self):

        self.n1_fat = fatiar_pra_lista(self.n1)
        self.n2_fat = fatiar_pra_lista(self.n2)

        if int(self.n1) == int(self.n2):
            print('0')
            return

        resposta = ListaDuplamenteEncadeada()

        atual_n1 = self.n1_fat.primeiro
        atual_n2 = self.n2_fat.primeiro

        empresta = 0

        while atual_n1 or atual_n2:

            if atual_n1 and atual_n2:

                if int(atual_n1.dado) < int(atual_n2.dado):
                    subt = str(int('1' + atual_n1.dado) - int(atual_n2.dado))

                resposta.inserir_inicio(str(int(atual_n1.dado) - int(atual_n2.dado)))

                atual_n1 = atual_n1.proximo
                atual_n2 = atual_n2.proximo

            elif atual_n1 and atual_n2 is None:
                resposta.inserir_inicio(str(int(atual_n1.dado)))

                atual_n1 = atual_n1.proximo

            elif atual_n1 is None and atual_n2:

                resposta.inserir_inicio(str(int(atual_n2.dado)))

                atual_n2 = atual_n2.proximo

        return mostrar(resposta)

