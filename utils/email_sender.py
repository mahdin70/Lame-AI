import smtplib
from email.mime.text import MIMEText
from config.email_config import SENDER_EMAIL, EMAIL_PASSWORD, RECIPIENT_EMAILS

def send_email(subject, body, recipients=RECIPIENT_EMAILS):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(recipients)
        
        server.send_message(msg)
        server.quit()
        print("Emails sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")