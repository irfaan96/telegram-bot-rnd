import logging, os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info('Handling start command')
    
    logging.info('Sending message to user')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    logging.info('Starting bot')

    application = ApplicationBuilder().token(os.getenv('API_TOKEN')).build()
    logging.info('Bot started')
    
    logging.info('Adding handlers')
    start_handler = CommandHandler('start', start)

    logging.info('Adding handlers to application')
    application.add_handler(start_handler)
    
    logging.info('Running polling')
    application.run_polling()