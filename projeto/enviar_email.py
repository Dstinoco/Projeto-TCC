import smtplib
import email.message
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

from projeto import base_url



def enviar_email_redefinicao_senha(e_mail, corpo):

    password = os.getenv('senha_email')
    msg = email.message.Message()
    msg['Subject'] = 'Email Automático'
    msg['From'] = os.getenv('email') 
    msg['to'] = e_mail
    msg.add_header("Content-Type", 'text/html')
    msg.set_payload(corpo)
    s = smtplib.SMTP("smtp-mail.outlook.com", 587)
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['to']], msg.as_string().encode('ISO-8859-1'))
    s.close()



def envio_email(e_mail, corpo):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    imagem_path = os.path.join(current_dir, 'static', 'img', 'logo-home.png')

    password = 'smtp@1234'
    msg = MIMEMultipart('related')
    msg['Subject'] = 'Medsênior'
    msg['From'] = 'portal.dados@medsenior.com.br'
    msg['To'] = e_mail

   
    corpo_email = MIMEText(corpo, 'html')
    msg.attach(corpo_email)

    corpo_email = MIMEText(corpo, 'html')
    msg.attach(corpo_email)

  
    with open(imagem_path, 'rb') as imagem_arquivo:
        imagem = MIMEImage(imagem_arquivo.read())
        imagem.add_header('Content-ID', '<image1>')  # ID da imagem usado no corpo do e-mail
        msg.attach(imagem)

 
    s = smtplib.SMTP("smtp-mail.outlook.com", 587)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.close()





def msg_boas_vindas(nome, email, senha_random):

    html = f'''

                <div class="card">
                <div class="header">
                    <img src="cid:image1" alt="Logo">
                    <h1>Portal de Dados</h1>
                </div>
                    <div class="card-body">
                        <h6 class="card-title">Bem-vindo(a) ao Portal de Dados</h6>
                    <h3>Olá, <strong>{nome}</strong> <br>Seja muito bem-vindo(a)</h3>
                    
                    <p>Para acessar sua conta, utilize as credenciais abaixo:</p>
                    <div class="credenciais">
                        <ul>
                            <li><strong>{email}</strong></li>
                            <li><strong>{senha_random}</strong></li>
                        </ul>
                    </div>
                    <p>Recomendamos que você altere sua senha assim que fizer login.

                    Se precisar de ajuda, nossa equipe está à disposição para assisti-lo(a).

                    Um abraço,

                    Equipe Portal de Dados</p>


                    <a href="https://{base_url}-portal-dados.azurewebsites.net/login" class="btn btn-success">Acessar o portal</a>
                    </div>
                </div>
                </body>
                </html>

                '''
    css = """
    
                <!DOCTYPE html>
            <html>
            <head>
            <style>
            /* Estilos básicos */
            body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            }

            .header {
            text-align: center;
            padding: 20px;
            background-color: #fff;
            border-bottom: 1px solid #ddd;
            }

            .header img {
            vertical-align: middle;
            width: 50px; /* Defina o tamanho da imagem */
            height: auto;
            }

            .header h1 {
            display: inline-block;
            font-size: 2rem; /* Defina o tamanho da fonte */
            vertical-align: middle;
            margin-left: 10px;
            color: #a4cc3c; /* Cor do texto */
            }

            .card {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            width: 400px;
            margin: 20px auto;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            .credenciais {
            background-color: #a4cc3c;
            border: 1px solid #FFFFFF;
            border-radius: 8px;
            margin: 20px auto;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            .card-body {
            padding: 20px;
            }

            .card-title {
            font-size: 1.5rem;
            margin-bottom: 15px;
            }

            .card-text {
            font-size: 1.2rem;
            margin-bottom: 20px;
            }

            .btn {
            display: flex;
            padding: 10px 20px;
            font-size: 1rem;
            color: #fff;
            background-color: #a4cc3c;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            }

            .btn:hover {
            background-color: #0056b3;
            }

            span{
                text-align: center;
            }
        </style>
                    </head>
                    <body>
            """

    return css + html


def msg_redefinicao(nome, senha_random):

    html = f'''

          <div class="card">
        <div class="header">
            <img src="cid:image1" alt="Logo">
            <h1>Portal de Dados</h1>
        </div>
            <div class="card-body">
                <h6 class="card-title">Sua Senha foi redefinida</h6>
            <h3>Olá, <strong>{nome}</strong></h3>
            
            <p>Segue a baixo sua nova senha de acesso</p>
            <div class="credenciais">
                <ul>
                    
                    <li><strong>{senha_random}</strong></li>
                </ul>
            </div>
            <p>Recomendamos que você altere sua senha assim que fizer login.

            Se precisar de ajuda, nossa equipe está à disposição para assisti-lo(a).

            Um abraço,

            Equipe Portal de Dados</p>


            <a href="https://{base_url}-portal-dados.azurewebsites.net/login" class="btn btn-success">Acessar o portal</a>
            </div>
        </div>
        </body>
        </html>

    '''

    css = """
    
                <!DOCTYPE html>
            <html>
            <head>
            <style>
            /* Estilos básicos */
            body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            }

            .header {
            text-align: center;
            padding: 20px;
            background-color: #fff;
            border-bottom: 1px solid #ddd;
            }

            .header img {
            vertical-align: middle;
            width: 50px; /* Defina o tamanho da imagem */
            height: auto;
            }

            .header h1 {
            display: inline-block;
            font-size: 2rem; /* Defina o tamanho da fonte */
            vertical-align: middle;
            margin-left: 10px;
            color: #a4cc3c; /* Cor do texto */
            }

            .card {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            width: 400px;
            margin: 20px auto;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            .credenciais {
            background-color: #a4cc3c;
            border: 1px solid #FFFFFF;
            border-radius: 8px;
            margin: 20px auto;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            .card-body {
            padding: 20px;
            }

            .card-title {
            font-size: 1.5rem;
            margin-bottom: 15px;
            }

            .card-text {
            font-size: 1.2rem;
            margin-bottom: 20px;
            }

            .btn {
            display: flex;
            padding: 10px 20px;
            font-size: 1rem;
            color: #fff;
            background-color: #a4cc3c;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            justify-content: center;
            }

            .btn:hover {
            background-color: #0056b3;
            }

            span{
                text-align: center;
            }
        </style>
                    </head>
                    <body>
            """
    
    return css + html



