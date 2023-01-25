import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('devananth511@gmail.com','Deva@5112002')
server.sendmail('devananth511@gmail.com','devananth511@gmail.com','heloooo')
print("email sent")