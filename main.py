from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8440160263:AAHU1gp6F_kZN9OQp1KLC3_Yz0oY8Krsgs4"  # Recomendado colocar como variável de ambiente depois

user_states = {}

# Telas do funil
def tela_1():
    return ("💻 Seja bem-vindo ao BOT OFICIAL do PAINEL DO SOMBRA V4.7\n\n"
            "⚠️ Aqui não é lugar pra curiosos. Se você chegou até aqui, é porque quer poder, anonimato e controle.\n\n"
            "👇 Me diga o que você quer:")

def tela_2():
    return ("🧠 O Painel do Sombra V4.7 não é brinquedo.\n"
            "Ele é um painel privado com funções exclusivas pra quem quer hackear o sistema sem ser rastreado.\n\n"
            "⚙️ O que ele faz:\n\n"
            "• Gerador de dados e CCs\n"
            "• Validador automático\n"
            "• Acesso a consultas privadas\n"
            "• Integração com sites de venda\n"
            "• Segurança de IP com camadas de proteção\n\n"
            "⚡ Atualizações mensais\n🔒 Suporte 24h\n🔥 Versão atual: V4.7\n\n"
            "Deseja ver mais ou seguir?")

def tela_4():
    return ("💥 OFERTA LIMITADA:\n\n"
            "O Painel do Sombra V4.7 está sendo liberado por:\n"
            "📦 R$ 35 (acesso vitalício)\n\n"
            "🚫 Após as 20 cópias vendidas dessa versão, ele será fechado novamente.\n\n"
            "✅ Pagamento via Pix ou Cripto\n\n"
            "Deseja garantir sua cópia agora?")

def tela_5():
    return ("🧾 Para efetuar o pagamento via Pix, acesse esse link:\n"
            "https://pay.sunize.com.br/gbKjfVgy\n\n"
            "🛡️ Em até 15 minutos, você recebe o acesso completo + tutorial.")

# Bot logic
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_states[update.effective_chat.id] = 1
    reply_markup = ReplyKeyboardMarkup([["1️⃣", "2️⃣"], ["3️⃣", "4️⃣"]], resize_keyboard=True)
    await update.message.reply_text(tela_1(), reply_markup=reply_markup)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.effective_chat.id

    if chat_id not in user_states:
        user_states[chat_id] = 1

    if user_states[chat_id] == 1:
        if text.startswith("1"):
            user_states[chat_id] = 2
            reply_markup = ReplyKeyboardMarkup([["1️⃣", "2️⃣"], ["3️⃣"]], resize_keyboard=True)
            await update.message.reply_text(tela_2(), reply_markup=reply_markup)
        elif text.startswith("2"):
            user_states[chat_id] = 4
            reply_markup = ReplyKeyboardMarkup([["1️⃣", "2️⃣"], ["3️⃣"]], resize_keyboard=True)
            await update.message.reply_text(tela_4(), reply_markup=reply_markup)
        elif text.startswith("3"):
            await update.message.reply_text("📞 Suporte: https://wa.me/553591418188/?text=duvida/painel")
        elif text.startswith("4"):
            await update.message.reply_text("👋 Até mais!")
    elif user_states[chat_id] == 2:
        if text.startswith("1") or text.startswith("2"):
            await update.message.reply_text("👁️‍🗨️ Em breve novas atualizações.")
    elif user_states[chat_id] == 4:
        if text.startswith("1") or text.startswith("2"):
            await update.message.reply_text(tela_5())

# Executar o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.run_polling()
