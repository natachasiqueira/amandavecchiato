from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Carrega variáveis de ambiente
    load_dotenv()
    
    app = Flask(__name__)
    
    # Configuração da chave secreta
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key_padrao')
    
    # Importar e registrar as rotas
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app

# Instância global para ser usada por servidores WSGI como Gunicorn
app = create_app()
