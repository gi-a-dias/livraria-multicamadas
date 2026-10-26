from flask import Blueprint, flash, redirect, render_template, request, url_for

from services.livraria_service import LivrariaService

livraria_bp = Blueprint("livraria", __name__)
livraria_service = LivrariaService()


@livraria_bp.get("/")
def index():
    genero = request.args.get("genero", "").strip()
    livros = livraria_service.listar_catalogo(genero=genero or None)
    favoritos = livraria_service.listar_favoritos()
    ids_favoritos = {livro.id for livro in favoritos}

    return render_template(
        "index.html",
        livros=livros,
        favoritos=favoritos,
        ids_favoritos=ids_favoritos,
        genero=genero,
    )


@livraria_bp.post("/favoritos/<int:livro_id>")
def adicionar_favorito(livro_id):
    try:
        livraria_service.adicionar_aos_favoritos(livro_id)
        flash("Livro adicionado aos favoritos.", "sucesso")
    except ValueError as erro:
        flash(str(erro), "erro")
    return redirect(url_for("livraria.index", genero=request.form.get("genero", "")))


@livraria_bp.post("/favoritos/<int:livro_id>/remover")
def remover_favorito(livro_id):
    livraria_service.remover_dos_favoritos(livro_id)
    flash("Livro removido dos favoritos.", "sucesso")
    return redirect(url_for("livraria.index", genero=request.form.get("genero", "")))
