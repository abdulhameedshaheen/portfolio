import smtplib
import ssl

host = "smtp.gmail.com"
port = "465"

username = "mis1411@gmail.com"
password = "ifzqzcsfittiedyn"

receiver = "mis1411@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: hi 
how are you ?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
