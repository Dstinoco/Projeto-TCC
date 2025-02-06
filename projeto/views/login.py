from projeto import app, database, bcrypt
from flask_login import login_manager, login_required, login_user, logout_user, current_user
from flask import redirect, render_template, flash, session, request, url_for, g

from projeto.models import USUARIO, LOGIN
from projeto.forms import FormLogar
from projeto.sessao import inicio_sessao, remove_sessao_expiradas



def Login():

    try:
        if current_user.is_authenticated:
            return redirect(url_for("index"))

        form_logar = FormLogar()

        if form_logar.validate_on_submit():
            usuario = USUARIO.query.filter_by(EMAIL=form_logar.email.data).first()
            if usuario and bcrypt.check_password_hash(usuario.PASSWORD, form_logar.password.data):
                if usuario.STATUS == 'A':
                    login_user(usuario)
                    

                    # Gravando log de acesso
                    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
                    ip_address = '177.137.232.38'
                    user_agent = request.user_agent.string 

                    salvar_log = LOGIN(
                        USUARIO_ID = usuario.USUARIO_ID,
                        IP = ip_address,
                        USER_AGENT = user_agent
                    )
                    database.session.add(salvar_log)
                    database.session.commit()

                    #gravando log sessao
                    inicio_sessao(usuario.USUARIO_ID)
                    #remove_sessao_expiradas()

                    flash("Login realizado com sucesso!","success")
                    return redirect(url_for("index"))
                else:
                    flash("Usuário inativo. Entre em contato com o suporte","primary")
            else:
                flash("Login inválido. Verifique suas credenciais.","danger")

    except Exception as e:
        flash(f"Error {e}", 'danger')
        return redirect(url_for("logar"))

    return render_template('login.html', form=form_logar)