# bot/send_images.py

import os
from telegram import Update
from telegram.ext import ContextTypes

async def send_images_to_telegram(images_path, update: Update):
    """
    Send the generated images to the user via Telegram.
    """
    for filename in os.listdir(images_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(images_path, filename)
            with open(file_path, 'rb') as file:
                await update.message.reply_photo(photo=file)
                print(f"Sent {filename} successfully")
