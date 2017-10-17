import smtplib
server = smtplib.SMTP('smtp.gmail.com', 465)
server.ehlo()
server.starttls()
server.ehlo()
server.login("geeknanda13@gmail.com", "bepositive0363")
text = "nanda mail test".as_string()
server.sendmail("geeknanda13@gmail.com", "geeknanda13@gmail.com", text)
