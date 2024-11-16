# main.py

import os
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from bot.utils import cleanup_generated_files, parse_input
from bot.image_generator import generate_latex_code, compile_latex
from bot.send_images import send_images_to_telegram

# Set up logging (optional)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def echo(update: Update, context):
    # Parse input message to extract heading and content
    heading, content = parse_input(update.message.text)
    print(f"Heading: {heading}")
    print(f"Content: {content}")

    # Generate LaTeX code
    latex_code = generate_latex_code(heading, content)

    # Compile LaTeX to PDF and images
    compile_latex(latex_code, heading)

    # Extract the folder name from the current date and heading
    current_date = datetime.now().strftime("%d-%m-%Y")
    folder_name = f"[{current_date}] {heading}"
    
    # Set up image path and send images back to the user (via Telegram)
    images_path = os.path.join("./", folder_name, "images")
    await send_images_to_telegram(images_path, update)

    # Cleanup the generated files
    cleanup_generated_files(folder_name)

    # Respond to user that the process is done
    await update.message.reply_text("Done")

def execute_main():
    # Telegram bot token from environment variable
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

    # Create the Telegram bot application
    print("Telegram Token", TELEGRAM_TOKEN)
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Add a message handler that triggers the 'echo' function on text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the application
    app.run_polling()

if __name__ == "__main__":
    execute_main()
