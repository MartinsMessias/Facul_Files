class No:

    def __init__(self, valor=None, no_anterior=None):
        self.valor = valor
        self.anterior = no_anterior

    def __str__(self):
        return f'{self.valor} \u21d2 {self.anterior}'


class Pilha:

    def __init__(self):
        self.topo = None

    def __str__(self):
        return str(self.topo)

    # Método para adicionar ao topo da pilha
    def adicionar(self, novo_valor):
        novo_no = No(novo_valor)
        novo_no.anterior = self.topo
        self.topo = novo_no

    # Método para remover do topo da pilha
    def remover(self):
        assert self.topo, "Pilha vazia!!!."
        self.topo = self.topo.anterior

#######################################################################################
#                                    EXEMPLOS                                         #
#######################################################################################

pilha = Pilha()                 # Cria uma pilha vazia.
print("Pilha vazia: ", pilha)

# Insere valores do range na pilha.
for i in range(6):
    pilha.adicionar(i)
    print(f'Insere o valor {i} no topo: {pilha}')

print('_'*66)

# Remove um à um todos valores da pilha.
while pilha.topo is not None:
    pilha.remover()
    print(f'Removendo valor que está no topo: {pilha}')


# Asserção em caso de tentativa de remoção de uma pilha vazia
# pilha.remover()
# print(pilha)
