from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8440160263:AAHU1gp6F_kZN9OQp1KLC3_Yz0oY8Krsgs4"
user_states = {}

def tela_1():
    return (
        "💻 Seja bem-vindo ao nosso Assistente Virtual!\n\n"
        "👇 Escolha uma das opções abaixo para continuar:"
    )

def tela_2():
    return (
        "📦 Nosso sistema oferece soluções avançadas:\n"
        "• Gerador de relatórios automáticos\n"
        "• Validador de dados\n"
        "• Integração com plataformas\n"
        "• Suporte em tempo real\n\n"
        "Deseja saber mais ou avançar?"
    )

def tela_4():
    return (
        "🔥 Promoção Especial:\n\n"
        "Acesso vitalício ao sistema por apenas:\n"
        "💰 R$ 35,00\n\n"
        "✅ Pagamento via Pix ou Cripto\n"
        "Deseja adquirir agora?"
    )

def tela_5():
    return (
        "🧾 Para pagamento, acesse:\n"
        "https://example.com/pagamento\n\n"
        "📧 Você receberá o acesso completo em até 15 minutos."
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_states[chat_id] = 1
    keyboard = [["1️⃣", "2️⃣"], ["3️⃣", "4️⃣"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(tela_1(), reply_markup=reply_markup)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    text = message.text or ""
    chat_id = update.effective_chat.id
    state = user_states.get(chat_id, 1)

    if state == 1:
        if text.startswith("1"):
            user_states[chat_id] = 2
            keyboard = [["1️⃣", "2️⃣"], ["3️⃣"]]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await message.reply_text(tela_2(), reply_markup=reply_markup)

        elif text.startswith("2"):
            user_states[chat_id] = 4
            keyboard = [["1️⃣", "2️⃣"], ["3️⃣"]]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await message.reply_text(tela_4(), reply_markup=reply_markup)

        elif text.startswith("3"):
            await message.reply_text("📞 Suporte: https://wa.me/seusuporte")

        elif text.startswith("4"):
            await message.reply_text("👋 Até mais!")

    elif state == 2:
        if text.startswith("1") or text.startswith("2"):
            await message.reply_text("🔧 Em breve, novas funcionalidades!")

    elif state == 4:
        if text.startswith("1") or text.startswith("2"):
            await message.reply_text(tela_5())

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.run_polling()
