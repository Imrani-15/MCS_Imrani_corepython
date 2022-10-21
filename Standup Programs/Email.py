import smtplib
sendermail = "imranishaik15@gmail.com"
recivermail = "startcareer.15@gmail.com"
password = input(str("Please enter your password:"))
message = "Hi guys Happy pongal to all"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sendermail,password)
print("===== login successfully =====")
server.sendmail(sendermail,recivermail,message)
print("message has been sent to ",recivermail)
