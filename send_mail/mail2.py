import smtplib, ssl
from password import passWord
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "minhazrahman1010@gmail.com"  # Enter your address
receiver_email = "shamssharifapurbo@gmail.com"  # Enter receiver address
passs=passWord
#get password
#1)go to myaccountgoogle
#2)go to security 
#3)app password
#4)generete a password by writing "Python"


context = ssl.create_default_context()
for i in range(5):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        message=input("what do u want to write: ")
        server.login(sender_email, passs)
        server.sendmail(sender_email, receiver_email, message)