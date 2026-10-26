from persistence.repositorio import carregar_livros_db

def listar_catalogo():
    """Serviço que recupera os livros do repositório."""
    return carregar_livros_db()

def adicionar_aos_favoritos(livro_id):
    """Nova Feature: Lógica de negócio para adicionar um livro à lista de desejos."""
    livros = carregar_livros_db()
    livro_encontrado = next((l for l in livros if l.id == livro_id), None)
    if livro_encontrado:
        return f"Livro '{livro_encontrado.titulo}' adicionado aos favoritos com sucesso!"
    return "Livro não encontrado."