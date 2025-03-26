import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

RECIPIENT_EMAILS = [
    "mukit.work@gmail.com",
    "malihazaman@iut-dhaka.edu",
    "ittehadrahman@iut-dhaka.edu",
    "mdsoyeb@iut-dhaka.edu",
    "mushfique2@iut-dhaka.edu",
    "zannatul@iut-dhaka.edu",
    "saminsadaf@iut-dhaka.edu",
    "jarif@iut-dhaka.edu",
    "mizbaulhaque@iut-dhaka.edu"
]