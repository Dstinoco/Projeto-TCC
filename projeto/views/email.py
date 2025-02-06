from flask import flash, url_for, redirect, request, render_template, render_template_string
from itsdangerous import SignatureExpired, BadSignature


from projeto.enviar_email import enviar_email_redefinicao_senha
from projeto.gerar_token import serializar_token, deserializar_token
from projeto.forms import FormLogar, FormCriarUser
from projeto.models import USUARIO
from projeto import bcrypt, database


def solicitar_redefinicao_senha():

    try:
        form = FormLogar()

        if request.method == 'POST':
            email = form.email.data
            usuario = USUARIO.query.filter_by(EMAIL = email).first()
            if usuario:
                if usuario.STATUS == 'A':
                    email_serializado = (serializar_token(email))
                    url = url_for("redefinir_senha", token=email_serializado, _external=True)

                    corpo_email = f'''
                        <h1>Portal Dados</h1>
                        <h2>Recuperação de senha</h2>
                        <p>Para redefinir a senha clique no link a baixo:</p>
                        <a href="{url}" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #4CAF50; text-align: center; text-decoration: none; border-radius: 5px;">Redefinir Senha</a>
                        '''
                    enviar_email_redefinicao_senha(email, corpo_email)

                    flash('Email de redefinição encaminhado para sua caixa de mensagem, caso o E-mail exista em nossa base', 'success')
                    return redirect(url_for('logar'))     
            else:
                flash('Email de redefinição encaminhado para sua caixa de mensagem, caso o E-mail exista em nossa base', 'success')
                return redirect(url_for('logar')) 

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('recuperar_senha'))
    


    return render_template('email/recuperacao_senha.html', form=form)



def redefinir_senha(token):

    try:
        form = FormCriarUser()
        if request.method == 'GET':
            email = deserializar_token(token)

        elif request.method == 'POST':
            email = deserializar_token(token)
            usuario = USUARIO.query.filter_by(EMAIL = email).first()
            
            if usuario.STATUS == 'A':

                if form.password.data == form.confirmar_password.data:

                        if len(form.password.data) < 8:
                            flash(f"A senha precisa ter no minimo 8 digitos", 'danger')
                            return redirect(f"/redefinir_senha/{token}")
                        

                        senha = form.password.data
                        senha_hash = bcrypt.generate_password_hash(senha)

                        usuario.PASSWORD = senha_hash
                        database.session.commit()
                        flash('Senha alterada com sucesso!', 'success')
                        return redirect(url_for('logar')) 

    except SignatureExpired:

        flash('URL expirada!', 'danger')
        return redirect(f"/sessao_expirada")

    except BadSignature:

        flash('URL inválida!', 'danger')
        return redirect(f"/sessao_expirada")

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(f"/redefinir_senha/{token}")
    
    return render_template('email/redefinir_senha.html', form=form)