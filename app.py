from flask import Flask
from presentation.routes import livraria_bp


def create_app():
    """Factory da aplicação Flask."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "chave-local-para-desenvolvimento"
    app.register_blueprint(livraria_bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
