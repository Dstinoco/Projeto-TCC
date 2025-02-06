from projeto import bcrypt, database
from flask_login import login_manager, login_required, login_user, logout_user, current_user
from flask import redirect, render_template, flash, session, request, url_for, g
from email_validator import validate_email
from projeto.funcoes import gerar_codigo_aleatorio
from projeto.enviar_email import envio_email, msg_boas_vindas, msg_redefinicao





from projeto.models import USUARIO, USUARIO_GRUPO, time_brasil
from projeto.forms import FormCriarUser, FormAlterarSenha
from projeto.querys import grupo_x_usuarios_filtrado
from projeto.funcoes import grupo_x_usuario_for_forms_and_table





def Cadastro_User():

    try:

        form_cadastro = FormCriarUser()
        form_senha = FormAlterarSenha()
        usuario_ativo = USUARIO.query.all()
        usuario_inativo = USUARIO.query.filter_by(STATUS='I')

        if request.method == 'POST':
            if request.form.get('form') == 'cadastro_form':


                    senha = gerar_codigo_aleatorio()
                    senha_hash =  bcrypt.generate_password_hash(senha)

                    status = "A" if form_cadastro.status.data == 1 else "I"
                    nome = form_cadastro.nome.data
                    email_form =form_cadastro.email.data
                    email = validate_email(email_form)
                    
                    novo_user = USUARIO(
                        NOME = nome ,
                        PASSWORD = senha_hash,
                        EMAIL = email_form,
                        STATUS = status,
                        USUARIO_ATUALIZACAO = g.id_user
                    )
                    database.session.add(novo_user)
                    database.session.commit()

                    msg = msg_boas_vindas(nome, email_form, senha)
                    envio_email(form_cadastro.email.data, msg )

                    if form_cadastro.grupo.data:
                        vinculo_user = USUARIO.query.filter_by(EMAIL = form_cadastro.email.data).first()
                        novo_vinculo = USUARIO_GRUPO(
                            USUARIO_ID = vinculo_user.USUARIO_ID,
                            GRUPO_ID = form_cadastro.grupo.data
                        )
                        database.session.add(novo_vinculo)
                        database.session.commit()



                    flash(f"O usuário {form_cadastro.nome.data} foi cadastrado com sucesso!", 'success')
                    return redirect(url_for("cadastro_usuario"))
                
            
            elif request.form.get('form') == 'senha_form':
                    
                    senha_gerada = gerar_codigo_aleatorio()

                    pass_hash = bcrypt.generate_password_hash(senha_gerada)
                    user_id = request.form.get('userId')

                    usuario = USUARIO.query.filter_by(USUARIO_ID = user_id).first()

                    nome = usuario.NOME
                    email = usuario.EMAIL

                    usuario.PASSWORD = pass_hash
                    database.session.commit()

                    msg = msg_redefinicao(nome, senha_gerada)
                    envio_email(email, msg )

                    flash("Senha alterada com sucesso!", "success")
                    return redirect(url_for('cadastro_usuario'))
            
            
            elif request.form.get('form') == 'delete_form':

                user_delete_id = request.form.get('deleteID')

                return redirect(url_for('delete_usuario', id=user_delete_id))
            
                
         

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastro_usuario'))


    return render_template('usuario/cadastro_user.html', form=form_cadastro, form_senha=form_senha, usuario_ativo=usuario_ativo, usuario_inativo=usuario_inativo )


def Update_User(id):

    try:
        query = grupo_x_usuarios_filtrado(id)
        form_cadastro = FormCriarUser()
        usuario = USUARIO.query.filter_by(USUARIO_ID = id).first()
        usuario_ativo = grupo_x_usuario_for_forms_and_table(modelo='table', query=query)
        

        if request.method == 'POST':
            if request.form.get('form') == 'update_form':

                usuario.STATUS = "A" if form_cadastro.status.data == 1 else "I"
                usuario.NOME = form_cadastro.nome.data
                usuario.EMAIL = form_cadastro.email.data
                usuario.USUARIO_ATUALIZACAO = g.id_user
                usuario.DT_ATUALIZACAO = time_brasil()

                database.session.commit()
                flash("Usuário alterada com sucesso!", "success")
                return redirect(f"/cadastro/usuario/update/{id}")
            
            elif request.form.get("form") == 'add_grupo_form':
                vincular_grupo = USUARIO_GRUPO(
                    USUARIO_ID = id,
                    GRUPO_ID = form_cadastro.grupo.data
                )
                database.session.add(vincular_grupo)
                database.session.commit()
                flash("Usuário alterada com sucesso!", "success")
                return redirect(f"/cadastro/usuario/update/{id}")
        
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastro_usuario'))
    
    return render_template('usuario/update_usuario.html', form=form_cadastro, usuario_grupo=usuario_ativo, update=usuario)


def Status_User(id):

    try:

        usuario = USUARIO.query.filter_by(USUARIO_ID = id).first()

        if usuario.STATUS == 'A':
            usuario.STATUS = 'I'
            flash("Cliente Inativado com sucesso!", "success")
        elif usuario.STATUS == 'I':
            usuario.STATUS = 'A'
            flash("Cliente Ativado com sucesso!", "success")
        database.session.commit()
        return redirect(url_for('cadastro_usuario'))
    
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastro_usuario'))


def Delete_User(id):

    try:
        usuario = USUARIO.query.filter_by(USUARIO_ID = g.id_user).first()
        
        if usuario.PERMITE_EXCLUIR == 'S':

            usuario_delete = USUARIO.query.filter_by(USUARIO_ID = id).first()
            database.session.delete(usuario_delete)
            database.session.commit()
            flash("Usuario excluido com sucesso!", "success")
            return redirect(url_for('cadastro_usuario'))
        
        else:
            flash("Você não possui permissão de exclusão", "danger")
            return redirect(url_for('cadastro_usuario'))

    
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastro_usuario'))
