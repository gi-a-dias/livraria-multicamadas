from domain.entidades import Livro

def carregar_livros_db():
    """Simula o banco de dados retornando instâncias de Livro."""
    return [
        Livro(1, "O Hobbit", "Fantasia", 45.0, 1),
        Livro(2, "1984", "Ficção", 30.0, 5),
        Livro(3, "Senhor dos Anéis", "Fantasia", 60.0, 2)
    ]