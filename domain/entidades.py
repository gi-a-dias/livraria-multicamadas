from dataclasses import dataclass


@dataclass(frozen=True)
class Livro:
    """Entidade de domínio que representa um livro do catálogo."""

    id: int
    titulo: str
    genero: str
    preco: float
    estoque: int

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("O identificador do livro deve ser positivo.")
        if not self.titulo.strip():
            raise ValueError("O título do livro não pode ficar vazio.")
        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if self.estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
