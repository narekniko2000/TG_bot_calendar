from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from dotenv import load_dotenv
import calendar
import datetime
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

# Generates the calendar keyboard for a given month/year
def create_calendar(year, month):
    keyboard = []
    # Header with Month and Year
    keyboard.append([InlineKeyboardButton(f'{calendar.month_name[month]} {year}', callback_data='IGNORE')])
    # Weekdays header
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    keyboard.append([InlineKeyboardButton(day, callback_data='IGNORE') for day in days])

    month_calendar = calendar.monthcalendar(year, month)
    for week in month_calendar:
        row = []
        for day in week:
            if day == 0:
                row.append(InlineKeyboardButton(" ", callback_data="IGNORE"))
            else:
                row.append(InlineKeyboardButton(str(day), callback_data=f"DAY|{year}|{month}|{day}"))
        keyboard.append(row)

    # Navigation buttons
    prev_month = month - 1 or 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    keyboard.append([
        InlineKeyboardButton("<", callback_data=f"PREV|{prev_year}|{prev_month}"),
        InlineKeyboardButton(" ", callback_data="IGNORE"),
        InlineKeyboardButton(">", callback_data=f"NEXT|{next_year}|{next_month}")
    ])

    return InlineKeyboardMarkup(keyboard)

# Command to start calendar
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now()
    markup = create_calendar(now.year, now.month)
    await update.message.reply_text("Please choose a date:", reply_markup=markup)

# Handles all callback queries for calendar
async def calendar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "IGNORE":
        return

    action, *parts = data.split("|")

    if action == "DAY":
        year, month, day = map(int, parts)
        selected = datetime.date(year, month, day)
        await query.edit_message_text(f"You selected: {selected.strftime('%Y-%m-%d')}")
    elif action in ["PREV", "NEXT"]:
        year, month = map(int, parts)
        markup = create_calendar(year, month)
        await query.edit_message_reply_markup(reply_markup=markup)

# Main function to run the bot
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(calendar_handler))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
