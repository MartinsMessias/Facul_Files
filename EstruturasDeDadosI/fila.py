class No:
    """Esta classe representa um nó de uma estrutura duplamente encadeada."""

    def __init__(self, dado=0, proximo_No=None):
        self.dado = dado
        self.proximo = proximo_No

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""

        # Cria um novo No com o dado a ser armazenado.
        novo_No = No(novo_dado)

        # Insere em uma fila vazia.
        if self.primeiro is None:
            self.primeiro = novo_No
            self.ultimo = novo_No
        else:
            # Faz com que o novo No seja o último da fila.
            self.ultimo.proximo = novo_No

            # Faz com que o último da fila referencie o novo No.
            self.ultimo = novo_No

    def remove(self):
        """Remove o último elemento da fila."""

        assert self.primeiro is not None, "Impossível remover elemento de fila vazia."

        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None

# Cria uma fila vazia.
fila = Fila()
print("Fila vazia: ", fila)

# Insere elementos na fila.
for i in range(5):
    fila.insere(i)
    print("Insere o valor {0} final da fila: {1}".format(i, fila))

# Remove elementos da fila.
while fila.primeiro is not None:
    fila.remove()
    print("Removendo elemento que está no começo da fila: ", fila)