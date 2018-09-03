from Banco import Banco


class Usuarios(object):

    def __init__(self, nome="", telefone="", email="", cpf="", usuario="", senha=""):
        self.info = {}
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.usuario = usuario
        self.senha = senha

    # Inserindo dados na tabela
    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "insert into usuarios (nome, telefone, email, cpf, usuario, senha) "
                "values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.cpf + "', '" +
                self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute(
                "update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone +
                "', email = '" + self.email + "', cpf = '" + self.cpf + "', usuario = '" + self.usuario +
                "', senha = '" + self.senha + "' where cpf = " + self.cpf + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where cpf = " + self.cpf + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, cpf):
        banco = Banco()
        self.verificaDB()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where cpf = " + cpf + "  ")

            for linha in c:
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.cpf = linha[4]
                self.usuario = linha[5]
                self.senha = linha[6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            if not self.verificaDB():
                return 'Banco de dados vazio'
            return "Ocorreu um erro na busca do usuário"

    def verificaDB(self):
        '''banco = Banco()
        c = banco.conexao.cursor()

        c.execute("SELECT cpf FROM usuarios;")

        i = 0
        for _ in c.fetchall():
            i += 1
        if i <= 0:
            return False
        return True'''
        pass

    def selectAll(self):
        banco = Banco()
        self.verificaDB()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios")

            for linha in c:
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.cpf = linha[4]
                self.usuario = linha[5]
                self.senha = linha[6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            if not self.verificaDB():
                return 'Banco de dados vazio'
            return "Ocorreu um erro na busca por usuários"
