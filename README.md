📅 Telegram Calendar Bot - README

This is a simple Telegram bot that displays an interactive calendar. Users can navigate between months and select a specific date using inline buttons.

✅ Features

Inline calendar view with month navigation (< and >) Select a date to receive it in YYYY-MM-DD format Clean and simple interface using Telegram inline buttons

🗂 Scripts

tgcalendar_bot.py

A basic interactive calendar bot where users can: Navigate through months (<, >) Select any day of the month

tgcalendar_disable_past_dates.py

Extended version of the calendar bot that disables selection of past dates. Only today and future dates are clickable Past days are shown but not selectable

📁 Files

tgcalendar_bot.py, tgcalendar_disable_past_dates) – Main script .env – Stores the bot token (TELEGRAM_TOKEN)

📦 Requirements

pip install python-telegram-bot==20.7 python-dotenv

🔧 Bot Commands

/start – Launch the calendar interface

📌 Notes

! Do not name the script calendar.py. This will conflict with Python’s standard calendar module and cause import errors.

Handles Telegram callbacks with: DAY|year|month|day for day selection PREV|year|month and NEXT|year|month for navigation

📤 Example Output

After pressing /start, the bot sends:

Please choose a date: [ [ ], [ Mo Tu We Th Fr Sa Su ], [ 1 2 3 4 5 6 7 ], ... [ < • > ] ] When a user clicks a date, it replies:

You selected: 2025-05-29
