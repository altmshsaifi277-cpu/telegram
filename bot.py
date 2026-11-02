import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TOKEN = "9064894809:AAF04f6nE4D5pbTpyGZa4HlbMci8QPG9n60"
UPI_ID = "altamas001@fam"
PAYEE_NAME = "Mohd Altamas"
QR_IMAGE_URL = "https://i.ibb.co/6yq4W5g/1000038297.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✨ **Welcome to Premium Content Bot** ✨\n\n"
        "🔥 Affordable plans starting at just ₹49\n"
        "✨ Content quality aisi ki dekhi nahi hogi\n"
        "✨ Only Premium Content | Daily New Uploads\n"
        "✨ Cp, Rp, Indian, Foreign, Dark everything\n"
        "✨ 10000+ Cp videos | 25000+ Rp videos | 5k+ Videos\n\n"
        "👇 **Select any plan below to get started:**"
    )

    keyboard = [
        [InlineKeyboardButton("⚡ ANIMAL FUN ⚡ ₹49/30 DAYS", callback_data="pay_49")],
        [InlineKeyboardButton("🥵 CHILD CARN PACK ⚡ ₹59/30 DAYS", callback_data="pay_59")],
        [InlineKeyboardButton("🥵 CHILD CORN 💧 ₹119/50 DAYS", callback_data="pay_119")],
        [InlineKeyboardButton("🥵 REAL INDIAN DESI POM 💯 ₹79/30 DAYS", callback_data="pay_79")],
        [InlineKeyboardButton("🥵 R@PE FULL VIDEO 🔥 ₹99/30 DAYS", callback_data="pay_99")],
        [InlineKeyboardButton("🥵 BAAP BETI ⚡ ₹59/30 DAYS", callback_data="pay_59")],
        [InlineKeyboardButton("🥵 ALL GROUP VIDEOS ❤️ ₹149/LIFETIME", callback_data="pay_149")],
        [InlineKeyboardButton("🔥 ALL GROUP FULL ACCESS 💯 ₹179/LIFETIME", callback_data="pay_179")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data_parts = query.data.split("_")
    if len(data_parts) > 1:
        amount = data_parts[1]
    else:
        amount = "49"

    upi_link = f"upi://pay?pa={UPI_ID}&pn={PAYEE_NAME}&am={amount}&cu=INR"
    
    payment_caption = (
        f"💳 **Subscription Payment Details**\n\n"
        f"💰 **Selected Amount:** ₹{amount}\n"
        f"🎯 **UPI ID:** `{UPI_ID}`\n\n"
        f"📌 **Instructions:**\n"
        f"1. Neeche diye gaye QR code ko scan karein ya [Click Here to Pay]({upi_link}) par click karein (Amount automatic aa jayega).\n"
        f"2. Payment successful hone ke baad **screenshot** yahin chat me bhejein taaki instant access mil sake!"
    )
    
    await context.bot.send_photo(
        chat_id=query.from_user.id,
        photo=QR_IMAGE_URL,
        caption=payment_caption,
        parse_mode="Markdown"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot is running fresh...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
