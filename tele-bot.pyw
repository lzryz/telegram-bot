import logging
import io
import os
from telegram import Update
from PIL import ImageGrab
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

OWN_USER_ID = #1234

# /screenshot command
async def screenshot_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWN_USER_ID:
        return
    screenshot = ImageGrab.grab()
    bio = io.BytesIO()
    bio.name = 'screenshot.png'
    screenshot.save(bio, 'PNG')
    bio.seek(0)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=bio)

# /shutdown command
async def shutdown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWN_USER_ID:
        return
    await update.message.reply_text('A számítógép leállítása folyamatban...')
    os.system("shutdown /s /t 1")

# simple message handler to echo user messages
# async def uzenet_kezeles(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     felhasznalo_szovege = update.message.text
#     valasz = f"Ezt küldted nekem: {felhasznalo_szovege}"
#     await update.message.reply_text(valasz)

def main():
    TOKEN = 'TOKEN'
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("screenshot", screenshot_command))
    app.add_handler(CommandHandler("shutdown", shutdown_command))
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, uzenet_kezeles))

    print("running")
    app.run_polling()

if __name__ == '__main__':
    main()
