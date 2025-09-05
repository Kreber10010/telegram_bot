from telegram import Bot

BOT_TOKEN = "8431098641:AAFHkabBirjMG6MINm9xz5M5WxLuETrb3iM"
CHAT_ID = "6525617413"

bot = Bot(token=BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Teste de mensagem 🚀")