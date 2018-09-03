class No:
    """Esta classe representa um No de uma estrutura encadeada."""

    def __init__(self, dado=0, No_anterior=None):
        self.dado = dado
        self.anterior = No_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)


class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da pilha."""

        # Cria um novo No com o dado a ser armazenado.
        novo_No = No(novo_dado)

        # Faz com que o novo No seja o topo da pilha.
        novo_No.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo No.
        self.topo = novo_No

    def remove(self):
        """Remove o elemento que está no topo da pilha."""

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior


# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.
for i in range(5):
    pilha.insere(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

# Remove elementos na pilha.
while pilha.topo is not None:
    pilha.remove()
    print("Removendo elemento que está no topo da pilha: ", pilha)
