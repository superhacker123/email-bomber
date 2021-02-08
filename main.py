import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail():
    login = input('Введите вашу почту: ')
    password = input('Введите пароль от почты: ')
    smtp = input('Введите SMTP сервер (например: smtp.yandex.ru): ')
    to = input('Введите адрес получателя: ')
    topic = input('Тема: ')
    message = input('Сообщение: ')
    num = int(input("Введите количество сообщений: "))

    for i in range(num):
        msg = MIMEMultipart()

        msg['Subject'] = topic
        msg['From'] = login
        msg.attach( MIMEText(message, 'plain') )

        server = root.SMTP_SSL( smtp, 465 )
        server.login(login, password)
        server.sendmail(login, to, msg.as_string())
    server.quit()

if __name__ == '__main__':
    send_mail()
