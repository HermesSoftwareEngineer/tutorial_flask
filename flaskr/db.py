from flask import current_app, g
from datetime import datetime
import sqlite3
import click

# Função para pegar/iniciar conexão com banco de dados
def get_db():
    # Caso a conexão não esteja definida
    if 'db' not in g:
        # Cria a conexão
        g.db = sqlite3.connect(
            # Configuração da pasta
            current_app.config['DATABASE'],
            # Configuração para detecção automática de tipos
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    
    # Retorna a conexão com o banco de dados
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Conexão com o banco de dados iniciada!')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)