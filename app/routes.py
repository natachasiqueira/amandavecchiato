from flask import Blueprint, render_template, request, url_for
import urllib.parse
import os

bp = Blueprint('main', __name__)

def gerar_link_whatsapp(origem):
    """
    Gera o link do WhatsApp com mensagem personalizada baseada na origem (UTM).
    """
    numero_whatsapp = os.getenv('WHATSAPP_NUMBER', '5511951989535')
    
    mensagens = {
        'instagram': "Olá! Vi seu trabalho no Instagram e gostaria de mais informações.",
        'google': "Olá! Encontrei seu site pelo Google e gostaria de mais informações.",
        'facebook': "Olá! Vi sua página no Facebook e gostaria de mais informações.",
        'default': "Olá! Vi seu trabalho no site e gostaria de mais informações."
    }
    
    mensagem = mensagens.get(origem, mensagens['default'])
    mensagem_encoded = urllib.parse.quote(mensagem)
    
    return f"https://wa.me/{numero_whatsapp}?text={mensagem_encoded}"

@bp.context_processor
def inject_whatsapp_link():
    """
    Injeta a função de gerar link do WhatsApp em todos os templates.
    Captura o parâmetro 'utm_source' da URL automaticamente se presente.
    """
    origem = request.args.get('utm_source', 'default')
    link_whatsapp = gerar_link_whatsapp(origem)
    return dict(link_whatsapp=link_whatsapp)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/trabalhos')
def trabalhos():
    return render_template('trabalhos.html')

@bp.route('/contato')
def contato():
    return render_template('contato.html')
