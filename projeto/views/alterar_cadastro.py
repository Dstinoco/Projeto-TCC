from flask import redirect, url_for, g, request, render_template, flash

from projeto import database, bcrypt
from projeto.forms import FormCriarUser
from projeto.models import USUARIO, time_brasil

def alterar_perfil():

    try:
        form = FormCriarUser()
        id = g.id_user
        meu_user = USUARIO.query.filter_by(USUARIO_ID = id).first()


        if request.method == 'POST':
            if request.form.get('form') == 'perfil_form':
                meu_user.NOME = form.nome.data
                meu_user.EMAIL = form.email.data
                meu_user.DT_ATUALIZACAO = time_brasil()
                meu_user.USUARIO_ATUALIZACAO = id

                database.session.commit()
                flash("Informações alteradas!", "success")
                return redirect(url_for('perfil'))
            
            elif request.form.get('form') == 'senha_form':
                if form.password.data == form.confirmar_password.data:

                    if len(form.password.data) < 8:
                        flash(f"A senha precisa ter no minimo 8 digitos", 'danger')
                        return redirect(url_for("perfil"))

                    senha = form.password.data
                    senha_hash =  bcrypt.generate_password_hash(senha)

                    meu_user.PASSWORD = senha_hash
                    database.session.commit()
                    flash("Informações alteradas!", "success")
                    return redirect(url_for('perfil'))
                else:
                    flash("Senha inválida!", "danger")
                    return redirect(url_for('perfil'))






    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('perfil'))

    

    return render_template('usuario/editar_perfil.html', form=form, usuario=meu_user)