import smtplib  #Simple Mail Transfer Protocol
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()  #We can use ssl(secure socket layer) ot tls(transport layer security)
server.login('grk25601@gmail.com','**********')
server.sendmail('grk25601@gmail.com', 'grk25303@gmail.com', 'Hi Rahul sending mail using python(Automation)')
print('Mail Sent')