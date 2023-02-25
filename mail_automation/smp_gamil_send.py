import smtplib
import schedule
from email.mime.text import MIMEText
from utils import S_MAIL, S_PASS


def mail_me():
    sender_email = S_MAIL
    sender_password = S_PASS
    recipient_email = "sdaniana@gmail.com"
    subject = "<3 :*"
    body = """
    <html>
      <body>
        <h1>Te iubesc de dragobete! </h1>
      </body>
    </html>
    """
    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(1)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, html_message.as_string())
    server.quit()
    #<p>This is an <b>HTML</b> email sent from #Python using the Gmail SMTP server.</p>


schedule.every(5).minutes.do(mail_me)
while True: 
  schedule.run_pending()
