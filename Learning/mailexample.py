import smtplib
server = smtplib.SMTP('smtp.gmail.com', 465)
server.ehlo()
server.starttls()
server.ehlo()
server.login("geeknanda13456@gmail.com", "123")
text = 'nanda mail test'
server.sendmail("geeknanda13456@gmail.com", "geeknanda13456@gmail.com", text)
