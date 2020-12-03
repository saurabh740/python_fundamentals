import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = "saurabhdhotre10@gmail.com"
password = "send_mail_demo"

def send_mail(text='email body', subject='hello world', from_email='saurabh dhotre <saurabhdhotre10@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['from'] = from_email
    msg['to'] = ', '.join(to_emails)
    msg['subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()

    #login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


if __name__ == "__main__":
    send_mail(to_emails=['saurabhdhotre10@gmail.com'])
    #print(response)
