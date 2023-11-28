import smtplib

SEND = 'mahdiarmazraei@gmail.com'
PASS = '13831383123321@'
def send_message(rmail, sub, body):
    message = f'subject:{sub}\n{body}'
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SEND, PASS)
        server.sendmail(SEND, rmail, message)


send_message = ('mazraee104729@gmail.com', 'not', 'hello')



