# Arquivo: main.py
# Importante: Crie um arquivo .python-version com "3.12.4" na raiz do seu repositório no Render
# para garantir compatibilidade com python-telegram-bot==20.6

import os
import asyncio
import aiohttp # Nova importação para fazer requisições HTTP
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import telegram.ext
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# --- Configurações ---
BOT_TOKEN = "8440160263:AAHU1gp6F_kZN9OQp1KLC3_Yz0oY8Krsgs4" # Ou use os.environ.get("BOT_TOKEN")

# URL base do seu serviço no Render (Render a define automaticamente)
WEBHOOK_URL_BASE = os.environ.get("RENDER_EXTERNAL_URL")
if not WEBHOOK_URL_BASE:
    # Para desenvolvimento local, você precisaria de um túnel (ngrok, etc.)
    WEBHOOK_URL_BASE = "https://seu-servico-webhook.onrender.com" # Substitua pelo seu URL real no Render

# Caminho do webhook (ajuda a isolar seu bot)
WEBHOOK_URL_PATH = f"/{BOT_TOKEN}/"
WEBHOOK_URL = f"{WEBHOOK_URL_BASE}{WEBHOOK_URL_PATH}"
SELF_PING_URL = WEBHOOK_URL # URL para o próprio serviço se "pingar"

# Porta que o Render espera que o serviço escute
PORT = int(os.environ.get('PORT', 8000)) # 8000 é uma porta comum, Render usa $PORT

# Intervalo de keep-alive em segundos (ex: 600 = 10 minutos)
KEEP_ALIVE_INTERVAL = int(os.environ.get('KEEP_ALIVE_INTERVAL', 600))

# --- Handlers (funções do bot) ---
# Etapa 1: Boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ Ver o que o Painel faz", callback_data="ver_painel")],
        [InlineKeyboardButton("2️⃣ Saber o preço", callback_data="saber_preco")],
        [InlineKeyboardButton("3️⃣ Falar com o suporte", callback_data="suporte")],
        [InlineKeyboardButton("4️⃣ Sair", callback_data="sair")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    
    # Determina se é um comando /start ou uma callback query
    if update.message:
        # Vindo do comando /start
        await update.message.reply_text(
            "💻 Seja bem-vindo ao BOT OFICIAL do *PAINEL DO SOMBRA V4.7*\n\n"
            "⚠️ Aqui não é lugar pra curiosos. Se você chegou até aqui, é porque quer poder, anonimato e controle.\n\n"
            "👇 Me diga o que você quer:",
            reply_markup=markup,
            parse_mode="Markdown"
        )
    elif update.callback_query:
        # Vindo de um botão "Voltar pro início"
        await update.callback_query.answer() # Importante para fechar o "botão carregando"
        await update.callback_query.edit_message_text(
            "💻 Seja bem-vindo ao BOT OFICIAL do *PAINEL DO SOMBRA V4.7*\n\n"
            "⚠️ Aqui não é lugar pra curiosos. Se você chegou até aqui, é porque quer poder, anonimato e controle.\n\n"
            "👇 Me diga o que você quer:",
            reply_markup=markup,
            parse_mode="Markdown"
        )

# Etapa 2: Apresentação do produto
async def ver_painel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Importante para fechar o "botão carregando"
    keyboard = [
        [InlineKeyboardButton("1️⃣ Quero saber o valor direto", callback_data="saber_preco")],
        [InlineKeyboardButton("2️⃣ Voltar", callback_data="start")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🧠 O Painel do Sombra V4.7 não é brinquedo.\n"
        "Ele é um painel privado com funções exclusivas pra quem quer hackear o sistema sem ser rastreado.\n\n"
        "⚙️ O que ele faz:\n"
        "✅ Gerador de dados e CCs\n"
        "✅ Validador automático\n"
        "✅ Acesso a consultas privadas\n"
        "✅ Integração com sites de venda\n"
        "✅ Segurança de IP com camadas de proteção\n\n"
        "⚡ Atualizações mensais\n"
        "🔒 Suporte 24h\n"
        "🔥 Versão atual: V4.7",
        reply_markup=markup
    )

# Etapa 3: Preço e escassez
async def saber_preco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Importante para fechar o "botão carregando"
    keyboard = [
        [InlineKeyboardButton("1️⃣ Quero comprar agora", callback_data="comprar")],
        [InlineKeyboardButton("2️⃣ Falar com suporte antes", callback_data="suporte")],
        [InlineKeyboardButton("3️⃣ Voltar pro início", callback_data="start")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "💥 OFERTA LIMITADA:\n\n"
        "O Painel do Sombra V4.7 está sendo liberado por:\n"
        "📦 R$ 35 (acesso vitalício)\n\n"
        "🚫 Após as 20 cópias vendidas dessa versão, ele será fechado novamente.\n\n"
        "✅ Pagamento via Pix ou Cripto\n\n"
        "Deseja garantir sua cópia agora?",
        reply_markup=markup
    )

# Etapa 4: Link de pagamento direto
async def comprar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Importante para fechar o "botão carregando"
    # Não precisa de teclado aqui, é uma mensagem final
    await query.edit_message_text(
        "🧾 Para efetuar o pagamento, acesse o link abaixo:\n"
        "👉 https://pay.sunize.com.br/gbKjfVgy \n\n"
        "⚠️ Após o pagamento, o acesso será liberado automaticamente."
    )

# Suporte (WhatsApp)
async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Importante para fechar o "botão carregando"
    # Não precisa de teclado aqui, é uma mensagem final
    await query.edit_message_text(
        "📞 Para falar com o suporte, clique no link abaixo:\n"
        "👉 https://wa.me/553591418188/?text=duvida/painel"
    )

# Manipulador de todos os botões
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data == "start":
        # Reenvia a mensagem de boas-vindas
        await start(update, context)
    elif data == "ver_painel":
        await ver_painel(update, context)
    elif data == "saber_preco":
        await saber_preco(update, context)
    elif data == "comprar":
        await comprar(update, context)
    elif data == "suporte":
        await suporte(update, context)
    elif data == "sair":
        query = update.callback_query
        await query.answer() # Importante
        await query.edit_message_text("👋 Até logo!")

# --- Função de Keep-Alive ---
async def keep_alive_task():
    """Tarefa assíncrona que envia um ping para si mesma a cada intervalo."""
    await asyncio.sleep(10) # Pequeno atraso inicial para garantir que o servidor esteja pronto
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # Faz uma requisição GET simples para o próprio endpoint do webhook
                async with session.get(SELF_PING_URL, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                    logging.info(f"[Keep-Alive] Ping enviado para {SELF_PING_URL}. Status: {resp.status}")
            except Exception as e:
                logging.error(f"[Keep-Alive] Erro ao enviar ping: {e}")
            
            # Aguarda o intervalo definido antes do próximo ping
            await asyncio.sleep(KEEP_ALIVE_INTERVAL)

# --- Configuração e Inicialização do Webhook ---
async def set_webhook_on_start(application: telegram.ext.Application):
    """Configura o webhook quando o bot inicia."""
    success = await application.bot.set_webhook(WEBHOOK_URL)
    if success:
        print(f"✅ Webhook configurado com sucesso em {WEBHOOK_URL}")
        # Inicia a tarefa de keep-alive após o webhook ser configurado
        asyncio.create_task(keep_alive_task())
    else:
        print(f"❌ Falha ao configurar o webhook em {WEBHOOK_URL}")

def main():
    """Configura e inicia o bot em modo webhook."""
    # Configuração básica de logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    # Cria a aplicação
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Registra os handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Configura o webhook após a inicialização
    application.post_init = set_webhook_on_start

    # Inicia o servidor web para receber os webhooks
    print(f"🚀 Iniciando servidor webhook na porta {PORT}...")
    application.run_webhook(
        listen="0.0.0.0",         # Escuta em todas as interfaces de rede
        port=PORT,                # Usa a porta definida pelo Render
        url_path=WEBHOOK_URL_PATH, # Caminho da URL do webhook
        webhook_url=WEBHOOK_URL   # URL completa do webhook
    )

if __name__ == '__main__':
    main()
    
