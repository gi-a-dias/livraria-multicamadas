from flask import Flask, render_template, request
from services.livraria_service import listar_catalogo, adicionar_aos_favoritos

app = Flask(__name__)

@app.route('/')
def index():
    livros = listar_catalogo()
    return render_template('index.html', livros=livros)

@app.route('/favoritar/<int:livro_id>')
def favoritar(livro_id):
    mensagem = adicionar_aos_favoritos(livro_id)
    livros = listar_catalogo()
    return render_template('index.html', livros=livros, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)