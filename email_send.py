from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

username = 'bebetinhomaia@gmail.com'
password = '34173571'

mail_from = 'bebetinhomaia@gmail.com'
subject = ('Aluguel efetuado com sucesso!')

def email_send(clientes,cpf,futuro):
    mail_msg = (f'''
  Efetuamos com sucesso o seu aluguel das fantasias, lembrando que a previsão de entrega é {futuro}, e que em caso de atraso
haverá cobrança extra por dia de atraso.

Nós agradecemos a preferencia.
Boas festas!
''')
    mail_h = MIMEText(mail_msg)
    mail_h['from'] = mail_from
    mail_h['to'] = clientes[cpf][1]
    mail_h['subject'] = subject


    server = smtplib.SMTP_SSL(smtp_ssl_host,smtp_ssl_port)
    server.login(username,password)
    server.sendmail(mail_from, clientes[cpf][1], mail_h.as_string())
    server.quit()
    print(f'Email enviado com sucesso para {clientes[cpf][0]}, verificar caixa de entrada!')
