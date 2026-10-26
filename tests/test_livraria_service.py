import unittest

from domain.entidades import Livro
from services.livraria_service import LivrariaService


class RepositorioFake:
    def __init__(self):
        self.livros = [
            Livro(1, "O Hobbit", "Fantasia", 45.0, 1),
            Livro(2, "1984", "Ficção", 30.0, 5),
        ]
        self.favoritos = set()

    def listar_livros(self):
        return list(self.livros)

    def buscar_por_id(self, livro_id):
        return next((livro for livro in self.livros if livro.id == livro_id), None)

    def adicionar_favorito(self, livro_id):
        self.favoritos.add(livro_id)

    def remover_favorito(self, livro_id):
        self.favoritos.discard(livro_id)

    def listar_ids_favoritos(self):
        return set(self.favoritos)


class LivrariaServiceTestes(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioFake()
        self.service = LivrariaService(self.repositorio)

    def test_filtra_catalogo_por_genero_sem_diferenciar_maiusculas(self):
        resultado = self.service.listar_catalogo("fantasia")
        self.assertEqual([livro.id for livro in resultado], [1])

    def test_adiciona_livro_aos_favoritos(self):
        self.service.adicionar_aos_favoritos(1)
        self.assertEqual([livro.id for livro in self.service.listar_favoritos()], [1])

    def test_livro_inexistente_gera_erro(self):
        with self.assertRaises(ValueError):
            self.service.adicionar_aos_favoritos(999)

    def test_remove_livro_dos_favoritos(self):
        self.service.adicionar_aos_favoritos(1)
        self.service.remover_dos_favoritos(1)
        self.assertEqual(self.service.listar_favoritos(), [])


if __name__ == "__main__":
    unittest.main()
