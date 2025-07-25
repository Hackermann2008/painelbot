# Arquivo: main.py
# Importante: Crie um arquivo .python-version com "3.12.4" na raiz do seu repositório no Render
# para garantir compatibilidade com python-telegram-bot==20.6

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8440160263:AAHU1gp6F_kZN9OQp1KLC3_Yz0oY8Krsgs4"

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

# Inicialização do bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    # print("Bot rodando...") # Opcional, mas não causa erro
    app.run_polling()
