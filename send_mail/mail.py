from email.message import EmailMessage
import smtplib
import ssl
from password import passWord

email_sender="minhazrahman1010@gmail.com"
email_password=passWord
#get password
#1)go to myaccountgoogle
#2)go to security 
#3)app password
#4)generete a password by writing "Python"
email_receiver='pafoh86215@civikli.com'
subject='test email by python'
body='hi i am minhaz ,wefad i am using python to send u mail'

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,body)