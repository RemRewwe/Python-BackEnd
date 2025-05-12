# nota para si mesmo: deixar esse codigo mais "organico", compactar ele o maximo que da
# por um imput, adicionar interações complexas, conectar o codigo com a data do computador
# por um interface com front end

class Pessoa: # primeira classe
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

# classe herdeira, curioso pensar que um pedaço de codigo é herdeiro e a gente não
class Usuario(Pessoa):
    def __init__(self, nome, cpf, email):
        super().__init__(nome, cpf, email)

    def __str__(self):
        return f'Usuário: {self.nome} | CPF: {self.cpf} | Email: {self.email}'

class Livro:
    def __init__(self, nome, autor, genero):
        self.titulo = nome
        self.autor = autor
        self.isbn = genero

    def __str__(self):
        return f'Livro: {self.titulo} | Autor: {self.autor} | Genero: {self.genero}'

class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo=8):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo

    def __str__(self):
        return f'Empréstimo - {self.usuario.nome} pegou "{self.livro.titulo}" em {self.data_emprestimo}'

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def emprestar(self, usuario, livro):
        self.emprestimos.append(Emprestimo(usuario, livro))

    def mostrar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor}")

    def mostrar_usuarios(self):
        for u in self.usuarios:
            print(f"{u.nome} - {u.email}")

    def mostrar_emprestimos(self):
        for e in self.emprestimos:
            print(f"{e.usuario.nome} pegou '{e.livro.titulo}' em {e.data_emprestimo}")

if __name__ == "__main__":
    biblio = Biblioteca()

    u1 = Usuario("milho", "espiga@gmail,com", "03055987590")
    u2 = Usuario("oco", "jailson@gmail.com", "20040080067")

    l1 = Livro("Se Liga na Psicologia", "eu não chequei", "informativo")
    l2 = Livro("No Meio Fio", "eu esqueci", "suspense...eu acho")

    biblio.cadastrar_usuario(u1)
    biblio.cadastrar_usuario(u2)

    biblio.cadastrar_livro(l1)
    biblio.cadastrar_livro(l2)

    biblio.emprestar(u1, l2)

    print("\nUsuários:")
    biblio.mostrar_usuarios()

    print("\nLivros:")
    biblio.mostrar_livros()

    print("\nEmpréstimos:")
    biblio.mostrar_emprestimos()
