import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# 1 - Dados do Email
password = open("senha", "r").read()
from_email ="contatodevjunior@gmail.com"
to_email ="contatodevjunior@gmail.com"
subject ="Atualização de planilha"
body = """
Boa tarde!

Olá, segue em anexo a automação da planilha, para a empresa de XYZ Automação.

Qualquer dúvida estou à disposição e ou colaboração!
"""

# 2 - Montando a estrutura do E-mail
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 3 - Adicionando anexo E-mail
anexo = "test.xlsx"
#print(mimetypes.guess_type(anexo)[0].split("/"))
mime_type, mime_subtype = mimetypes.gues_type(anexo)[0].split("/")
with open (anexo, "rb") as a:
    message.add_attachment (
        a.read(),
        maintype=mime_type,
        filename=anexo
        )

# 4 - Enviando o E-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail (
        from_email,
        to_email,
        message.as_string()
    )