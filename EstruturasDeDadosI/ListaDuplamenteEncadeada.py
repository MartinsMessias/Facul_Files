class No:
    dado = anterior = proximo = None

    def __init__(self, dado=None):
        self.dado = dado

    def __repr__(self):
        return '%s \u21c4 %s' % (self.dado, self.proximo)


class ListaDuplamenteEncadeada:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0


    def __repr__(self):
        return 'None \u21c4 '+str(self.primeiro)


    def __iter__(self):
        n = self.primeiro
        while n is not None:
            yield n.dado
            n = n.proximo


    def inserir_fim(self, novo_dado):

        novo_no = No(novo_dado)
        novo_no.proximo = None

        if self.primeiro is None:
            novo_no.anterior = None
            self.primeiro = novo_no
            return
        ultimo = self.primeiro
        while ultimo.proximo is not None:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_no
        novo_no.anterior = ultimo
        self.tamanho += 1

        return
        
    # MESSIAS MARTINS #
    
    def inserir_inicio(self, dado):
        novo = No(dado)
        novo.proximo = self.primeiro
        self.primeiro = novo
        self.tamanho += 1

    def remover_primeiro(self):
        if self.primeiro is None:
            print('Erro! - Lista vazia')
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1


    def remover_ultimo(self):
        if self.primeiro is not None:
            anterior = x = self.primeiro
            while x.proximo is not None:
                anterior = x
                x = x.proximo
            if anterior == x:
                self.primeiro = None
            else:
                anterior.proximo = None
            self.tamanho -= 1
        else:
            print('Lista vazia!\n')
						
						
	   # MESSIAS MARTINS #
