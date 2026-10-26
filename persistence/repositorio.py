from domain.entidades import Livro


class RepositorioLivros:
    """
    Camada de persistência simulada em memória.

    Os dados ficam no objeto do repositório durante a execução do processo.
    Para persistência após reiniciar a aplicação, esta classe pode ser
    substituída por uma implementação com SQLite ou outro banco de dados.
    """

    def __init__(self):
        self._livros = {
            1: Livro(1, "O Hobbit", "Fantasia", 45.00, 1),
            2: Livro(2, "1984", "Ficção", 30.00, 5),
            3: Livro(3, "Senhor dos Anéis", "Fantasia", 60.00, 2),
            4: Livro(4, "Orgulho e Preconceito", "Romance", 35.00, 4),
        }
        self._favoritos = set()

    def listar_livros(self):
        return list(self._livros.values())

    def buscar_por_id(self, livro_id):
        return self._livros.get(livro_id)

    def adicionar_favorito(self, livro_id):
        if livro_id in self._livros:
            self._favoritos.add(livro_id)

    def remover_favorito(self, livro_id):
        self._favoritos.discard(livro_id)

    def listar_ids_favoritos(self):
        return set(self._favoritos)
