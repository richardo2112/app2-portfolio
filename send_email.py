import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    my_email = "richard.ostkamp@gmail.com"
    password = "zijhgzfizdajlaes"
    receiver = "richard.ostkamp@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(my_email, password)
        server.sendmail(my_email, receiver, message)

