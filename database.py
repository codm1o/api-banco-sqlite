import sqlite3
from datetime import datetime

# Função para conectar ou criar o banco
def connect_db():
    return sqlite3.connect('usuarios.db')

# Função para criar a tabela
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT,
            criado_em TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir usuário
def insert_user(nome, idade, email):
    conn = connect_db()
    cursor = conn.cursor()
    criado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO usuarios (nome, idade, email, criado_em)
        VALUES (?, ?, ?, ?)
    ''', (nome, idade, email, criado_em))
    conn.commit()
    conn.close()

# Função para listar usuários
def fetch_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    conn.close()
    return users

# Função para deletar usuário
def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
