
# Livraria - Arquitetura Multicamadas (Lab 7.3)

Evolução da aplicação da livraria estruturada em **pelo menos 4 camadas** bem definidas, garantindo a separação de responsabilidades e a adição de uma nova funcionalidade de negócio.

## 🏛️ As 4 Camadas da Arquitetura
1. **Camada de Apresentação (Presentation / UI):** Rotas do Flask e templates HTML (`app.py` e `templates/`).
2. **Camada de Aplicação / Serviços (Application Service):** Orquestração dos fluxos de negócio e novas features (`services/livraria_service.py`).
3. **Camada de Domínio (Domain):** Entidades puras e estruturas de dados do negócio (`domain/entidades.py`).
4. **Camada de Acesso a Dados (Persistence):** Módulo responsável por simular e recuperar os dados do repositório (`persistence/repositorio.py`).

## 🚀 Novas Funcionalidades
- Gerenciamento de Lista de Desejos / Favoritos integrada ao catálogo.

## 🛠️ Como Executar
1. Certifique-se de ativar o ambiente virtual do projeto.
2. Instale as dependências:
   ```bash
   pip install flask
