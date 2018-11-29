from random import randint

class TabelaHash(object):

    def __init__(self):
        self.tabela = []
        self.colisoes = 0
        for i in range(10):
            self.tabela.append([])

    def hash(self, chave):
        return chave % 10

    def get(self, chave):
        h = self.hash(chave)
        for i in self.tabela[h]:
            if i[0] == chave:
                return i
            return None

    def put(self, chave, valor):
        novo = (chave, valor)
        h = self.hash(chave)
        x = self.get(chave)
        if len(self.tabela[h]) > 0:
            self.colisoes += 1
        if x:
            self.tabela[h].remove(x)
        self.tabela[h].append(novo)

    def remove(self, chave):
        v = self.get(chave)
        if v is not None:
            h = self.hash(chave)
            self.tabela[h].remove(v)


###############################################################################
tabela = TabelaHash()

for x in range(1000):
    rand = randint(0, 1000)
    tabela.put(rand, rand)

vaz = 0

for x in tabela.tabela:
    if len(x) == 0:
        vaz += 1

print(f'COLISÕES: {(tabela.colisoes/(10 - vaz))}')
print(f'VAZIOS: {vaz}')
