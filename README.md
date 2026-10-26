# Livraria — Arquitetura Multicamadas (Exercício 7.3)

Projeto Flask didático que demonstra a separação de responsabilidades em quatro camadas e adiciona a funcionalidade de lista de favoritos.

## Camadas

1. **Apresentação (`presentation/`)** — rotas HTTP, leitura dos parâmetros da requisição e renderização dos templates.
2. **Aplicação/Serviços (`services/`)** — regras e casos de uso: listar e filtrar o catálogo, buscar livros e gerenciar favoritos.
3. **Domínio (`domain/`)** — entidade `Livro` e validações essenciais dos dados.
4. **Persistência (`persistence/`)** — acesso aos livros e favoritos. A implementação atual é em memória e pode ser substituída por banco de dados sem mudar as rotas.

`app.py` é o ponto de entrada e configura o Flask; não contém regras de negócio.

## Funcionalidades

- Listar o catálogo.
- Filtrar livros por gênero, ignorando diferenças entre maiúsculas e minúsculas.
- Adicionar e remover livros dos favoritos.
- Exibir a lista de favoritos.
- Informar quando um livro não existe.

## Como executar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

Ative o ambiente virtual:

- Windows: `.venv\\Scripts\\activate`
- Linux/macOS: `source .venv/bin/activate`

Instale as dependências e execute:

```bash
pip install -r requirements.txt
python app.py
```

Abra `http://127.0.0.1:5000`.

## Testes

```bash
python -m unittest discover -s tests
```

## Observação sobre persistência

Para manter o exercício simples, livros e favoritos são armazenados em memória. Os favoritos permanecem durante a execução atual, mas são reiniciados quando o processo da aplicação é reiniciado. A camada `persistence` é o local apropriado para trocar essa simulação por SQLite ou outro banco.

## Fluxo de uma requisição

Exemplo ao adicionar um livro aos favoritos:

`POST /favoritos/1` → `presentation/routes.py` → `LivrariaService` → `RepositorioLivros` → resposta por redirecionamento para a página do catálogo.

Isso demonstra que a rota não acessa os dados diretamente nem implementa a regra de negócio.
