import smtplib
from email.mime.text import MIMEText

###### Conexão com os servidores do Gmail.
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

###### Dados da conta para se conectar no servidor do Gmail.
username = 'seu username do gmail ex: blevers@gmail.com'
password = ['a senha da conta']

###### Os dados do envio.
from_addr = 'email de envio ex: blevers@gmail.com'
to_addrs = ['destinatarios']

###### Utilizando o MIMEText para enviar somente texto.
message = MIMEText('Olá!')
message['subject'] = 'Meu primeiro email usando Python'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

###### Iniciando a conexão com o servidor de forma segura usando o SSL.
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

###### Interação com o servidor externo do Gmail.
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())

###### Encerrando conexão com o servidor
server.quit
