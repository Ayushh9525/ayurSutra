# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from config import settings

# conf = ConnectionConfig(
#     MAIL_USERNAME = settings.MAIL_USERNAME,
#     MAIL_PASSWORD = settings.MAIL_PASSWORD,
#     MAIL_FROM = settings.MAIL_FROM,
#     MAIL_PORT = settings.MAIL_PORT,
#     MAIL_SERVER = settings.MAIL_SERVER,
#     MAIL_TLS = settings.MAIL_TLS,
#     MAIL_SSL = settings.MAIL_SSL,
#     USE_CREDENTIALS = True
# )

# async def send_email(subject: str, email_to: str, body: str):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype="plain"
#     )
#     fm = FastMail(conf)
#     await fm.send_message(message)






import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# configure your Gmail or SMTP details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"   # use app password, not your real Gmail password

def send_email_notification(to_email: str, subject: str, message: str):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
