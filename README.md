# Projeto CRUD com SQLite em Python

Este projeto é uma aplicação simples de linha de comando (terminal) que realiza operações básicas de um CRUD (Create, Read, Update, Delete) usando Python e SQLite.

O objetivo é demonstrar de forma prática como:
- Criar e conectar a um banco de dados SQLite.
- Criar tabelas automaticamente se não existirem.
- Inserir, listar e deletar usuários.
- Organizar o projeto separando as funções de banco em um módulo separado (database.py).
- Interagir com o usuário através de um menu no terminal.


## Tecnologias usadas

- Python 3.x
- SQLite3 (integrado no Python, sem necessidade de instalar separado)


## Estrutura do projeto

.
└── api-banco-sqlite/
    ├── app.py
    ├── database.py
    ├── usuarios.db
    ├── README.md
    └── requirements.txt


## Funcionalidades

- Criar banco de dados e tabela de usuários.
- Inserir novos usuários com nome, idade e email.
- Listar todos os usuários cadastrados.
- Deletar usuários pelo ID.
- Armazenar a data e hora de criação de cada usuário.


## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/codm1o/api-banco-sqlite.git

2. Entre na pasta do projeto:
   cd api-banco-sqlite

3. Execute o arquivo principal:
   python app.py

4. Escolha as opções no menu para usar o sistema.

Menu de opções
Ao rodar o programa, o seguinte menu será exibido:

=== MENU PRINCIPAL ===
1 - Inserir novo usuário
2 - Listar usuários
3 - Deletar usuário
0 - Sair

Basta digitar o número da opção desejada.

 _Exemplo de uso_
    Inserir um novo usuário - Digitar 1
    Listar todos os usuários - Digitar 2
    Deletar um usuário pelo ID - Digitar 3
    Sair do sistema - Digitar 0

_(Desenvolvido por [codm1o](https://github.com/codm1o) — 2025)_




