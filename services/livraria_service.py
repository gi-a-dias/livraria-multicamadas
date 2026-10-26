from persistence.repositorio import RepositorioLivros


class LivrariaService:
    """Coordena os casos de uso da livraria sem depender da camada web."""

    def __init__(self, repositorio=None):
        self.repositorio = repositorio or RepositorioLivros()

    def listar_catalogo(self, genero=None):
        livros = self.repositorio.listar_livros()
        if not genero:
            return livros

        termo = genero.casefold()
        return [livro for livro in livros if termo in livro.genero.casefold()]

    def buscar_livro(self, livro_id):
        livro = self.repositorio.buscar_por_id(livro_id)
        if livro is None:
            raise ValueError("Livro não encontrado.")
        return livro

    def adicionar_aos_favoritos(self, livro_id):
        livro = self.buscar_livro(livro_id)
        self.repositorio.adicionar_favorito(livro.id)
        return livro

    def remover_dos_favoritos(self, livro_id):
        self.repositorio.remover_favorito(livro_id)

    def listar_favoritos(self):
        ids = self.repositorio.listar_ids_favoritos()
        return [
            livro for livro in self.repositorio.listar_livros()
            if livro.id in ids
        ]
