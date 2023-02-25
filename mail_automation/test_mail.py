import smtplib
import schedule
from email.mime.text import MIMEText
from utils import S_MAIL, S_PASS


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


num_hearts = []


def send_email_wrapper():
    subject = "<3   :*   "
    body_template = "I love you 1000! {}"
    sender = S_MAIL
    recipients = ["ticoanionut@yahoo.com"]
    password = S_PASS
    num_hearts.append(1)
    body = body_template.format(subject * len(num_hearts))
    send_email(subject, body, sender, recipients, password)
    print(len(num_hearts))
    

schedule.every(10).seconds.do(send_email_wrapper)
while True:
    schedule.run_pending()
    