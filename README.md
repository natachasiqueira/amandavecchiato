# Amanda Vecchiato — Site de Assessoria

Projeto web desenvolvido em Flask com HTML/CSS/JS para apresentar serviços de assessoria de casamentos, eventos corporativos e artísticos, com foco em UX elegante, responsiva e acessível.

## Como rodar

1. Crie e ative um ambiente virtual (opcional)
2. Instale dependências:

```
pip install -r requirements.txt
```

3. Configure variáveis de ambiente (opcional):

```
SECRET_KEY=uma_chave_segura
WHATSAPP_NUMBER=5511999999999
```

4. Execute localmente:

```
python -m flask --app app run
```

## Estrutura

- Backend Flask: app/__init__.py, app/routes.py
- Templates: app/templates/ (base.html, index.html, trabalhos.html, contato.html)
- Estilos: app/static/css/style.css
- JavaScript: app/static/js/main.js

## Links do WhatsApp — como funcionam

O site gera automaticamente um link de WhatsApp no formato:

```
https://wa.me/SEU_NUMERO?text=MENSAGEM_URL_ENCODED
```

- O número vem da variável de ambiente `WHATSAPP_NUMBER` (ex.: `5511951989535`).
- A mensagem é personalizada conforme a origem de quem clicou, usando o parâmetro `utm_source` na URL do site.

### Onde isso é feito

- Função de geração: app/routes.py (`gerar_link_whatsapp`)
- Injeção do link nos templates: app/routes.py (`inject_whatsapp_link`)
- Uso no frontend (exemplo): botão “Fale comigo” em app/templates/index.html

### Personalização por origem

O site reconhece `utm_source` e muda a mensagem automaticamente:

- `utm_source=instagram` → “Olá! Vi seu trabalho no Instagram e gostaria de mais informações.”
- `utm_source=facebook` → “Olá! Vi sua página no Facebook e gostaria de mais informações.”
- `utm_source=google` → “Olá! Encontrei seu site pelo Google e gostaria de mais informações.”
- Sem `utm_source` → mensagem padrão: “Olá! Vi seu trabalho no site e gostaria de mais informações.”

### Como usar nos perfis (recomendado)

Use links para o seu site com o parâmetro de origem, para que o botão/CTA “Fale comigo” gere o WhatsApp correto:

- Instagram (bio):
  - `https://SEU-DOMINIO/?utm_source=instagram`
- Facebook (sobre/contato ou post fixo):
  - `https://SEU-DOMINIO/?utm_source=facebook`
- Google (perfil empresarial ou campanha):
  - `https://SEU-DOMINIO/?utm_source=google`

Assim, você NÃO precisa manter links diferentes de WhatsApp manualmente; basta apontar para o site com a origem correta, e o site monta o link do WhatsApp sozinho.

### Alternativa: link direto para o WhatsApp

Se preferir, você pode usar diretamente um link do WhatsApp em cada plataforma, com mensagens específicas. Exemplo:

- Instagram:
  - `https://wa.me/5511951989535?text=Ol%C3%A1!%20Vi%20seu%20trabalho%20no%20Instagram%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.`
- Facebook:
  - `https://wa.me/5511951989535?text=Ol%C3%A1!%20Vi%20sua%20p%C3%A1gina%20no%20Facebook%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.`

Essa opção exige que você edite manualmente os textos, enquanto a abordagem via site com `utm_source` automatiza tudo.

## Dicas de configuração

- Troque `WHATSAPP_NUMBER` para o seu número real (com DDI + DDD).
- Se usar hospedagem, mantenha `SECRET_KEY` segura.
- Para campanhas, use UTM (utm_source, utm_medium, utm_campaign) no link do site para segmentar origens.

## Acessibilidade e UX

- Navegação responsiva e foco em legibilidade.
- Lightbox com fechamento por clique fora, botão “fechar” e tecla Esc.
