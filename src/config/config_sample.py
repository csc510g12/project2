"""
RENAME THIS FILE TO config.py, ADD YOUR CONFIGURATION SETTINGS
This module contains configuration settings for the Money Manager application.
"""

import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017",
)

TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY", "")
TOKEN_ALGORITHM = os.getenv("TOKEN_ALGORITHM", "HS256")

API_BIND_HOST = os.getenv("API_BIND_HOST", "0.0.0.0")
API_BIND_PORT = int(os.getenv("API_BIND_PORT", "9999"))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_BOT_API_BASE_URL = os.getenv(
    "TELEGRAM_BOT_API_BASE_URL", "http://localhost:9999"
)

TIME_ZONE = os.getenv("TIME_ZONE", "America/New_York")

TELEGRAM_PRIVATE_CHAT_COMMAND_TEXT = """
start - Start the bot and display available commands
menu - Display available commands
signup - Register if you are a new user
login - Welcome back and log in
logout - Logout from the telegram bot
expenses_add - Record/Add a new spending
expenses_view - Display spending history
expenses_update - Update an expense
expenses_delete - Delete an expense
expenses_delete_all - Delete all the expenses
accounts_add - Create a new account
accounts_view - View all accounts
accounts_update - Update an account
accounts_delete - Delete an account
categories_add - Create a new category with monthly budget
categories_view - View all categories and budgets
categories_update - Update a category
categories_delete - Delete a category
analytics - Display analytics
exports - Export data to pdf, xlsx, csv
cancel - To cancel any operation
"""

TELEGRAM_GROUP_CHAT_COMMAND_TEXT = """
menu - Display available commands
bill_split - Split a bill with group members
bill_split_status - Check the status of an ongoing bill split
bill_split_proceed - Proceed with ongoing bill split
transfer - Transfer money to another group member
cancel_transfer - Cancel the ongoing transfer
cancel - Cancel the ongoing bill split
"""

MAIL_SMTP_SERVER = os.getenv("GMAIL_SMTP_SERVER", "smtp.gmail.com")
MAIL_SMTP_PORT = int(os.getenv("GMAIL_SMTP_PORT", "587"))
MAIL_SMTP_USERNAME = os.getenv("GMAIL_SMTP_USERNAME", "")
MAIL_SMTP_PASSWORD = os.getenv("GMAIL_SMTP_PASSWORD", "")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
