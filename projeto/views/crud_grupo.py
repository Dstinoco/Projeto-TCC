from flask_login import login_manager, login_required, login_user, logout_user, current_user
from flask import redirect, render_template, flash, session, request, url_for, g
from projeto import bcrypt, database, app

from projeto.models import GRUPO, USUARIO_GRUPO, DOWNLOAD_ARQUIVO_GRUPO, USUARIO, time_brasil
from projeto.forms import FormGrupo, FormUsuarioGrupo
from projeto.funcoes import ( grupo_x_usuario_for_forms_and_table, grupo_x_funcionalidade, 
                             retornar_usuarios_de_grupo, retornar_funcionalidade_de_grupo, retornar_download_de_grupo)
from projeto.querys import grupo_x_usuarios




def Cadastrar_Grupo():

    try:
        
        cadastro = FormGrupo()
        update = FormGrupo()
        tables_grupos = GRUPO.query.all()

        if request.method == 'POST':
            if request.form.get('form') == 'grupo_form':
                status = "A" if cadastro.status.data == 1 else "I"
                novo_grupo = GRUPO(
                    NOME=cadastro.nome.data,
                    STATUS = status,
                    USUARIO_ATUALIZACAO= g.id_user
                    )
                database.session.add(novo_grupo)
                database.session.commit()
                return redirect(url_for('grupo'))
            
            elif request.form.get('form') == 'alterar_grupo_form':
                grupo_id = request.form.get("grupoId")
                alterar_grupo = GRUPO.query.filter_by(GRUPO_ID = grupo_id ).first()

                alterar_grupo.NOME = update.nome.data
                alterar_grupo.STATUS = 'A' if update.status.data == 1 else 'I'
                alterar_grupo.USUARIO_ATUALIZACAO = g.id_user
                alterar_grupo.DT_ATUALIZACAO = time_brasil()
                database.session.commit()
                flash("Grupo alterado!", "success")
                return redirect(url_for('grupo'))
            
            elif request.form.get('form') == 'delete_form':

                user_delete_id = request.form.get('deleteID')

                return redirect(url_for('delete_grupo', id=user_delete_id))
            
    except Exception as e:
        app.logger.error(f"Error: {e}")
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('grupo'))

    return render_template('grupo/cadastro_grupo.html', cadastro=cadastro, update=update, grupos=tables_grupos)


def informacoes_grupo(id):

    try:

        usuarios = retornar_usuarios_de_grupo(id)
        funcionalidades = retornar_funcionalidade_de_grupo(id)
        uploads = retornar_upload_de_grupo(id)
        downloads = retornar_download_de_grupo(id) 

        form = FormGrupo()
        grupo = GRUPO.query.filter_by(GRUPO_ID = id).first()


        
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('grupo'))
    
    return render_template('grupo/informacoes_grupo.html', form=form, funcionalidades=funcionalidades, usuarios=usuarios, uploads=uploads, downloads=downloads, grupo=grupo)


def Delete_Grupo(id):

    try:
        usuario = USUARIO.query.filter_by(USUARIO_ID = g.id_user).first()

        if usuario.PERMITE_EXCLUIR == 'S':

            grupo = GRUPO.query.filter_by(GRUPO_ID = id).first()
            database.session.delete(grupo)
            database.session.commit()
            flash('Grupo deletado com sucesso', 'success')

            return redirect(url_for('grupo'))
        else:
            flash("Você não possui permissão de exclusão", "danger")
            return redirect(url_for('grupo'))
    
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('grupo'))





def Delete_Grupo_x_Usuario(id):

    try:

        remove_user_grupo = USUARIO_GRUPO.query.filter_by(USUARIO_GRUPO_ID=id ).first()

        database.session.delete(remove_user_grupo)
        database.session.commit()
        flash('Vínculo removido!', 'success')
        return redirect(f"/cadastro/usuario/update/{remove_user_grupo.USUARIO_ID}")
    
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('grupo'))
    


def delete_grupo_x_download_arquivo(id):

    try:

        remove_user_grupo = DOWNLOAD_ARQUIVO_GRUPO.query.filter_by(DOWNLOAD_ARQUIVO_GRUPO_ID=id ).first()
        id = remove_user_grupo.DOWNLOAD_ARQUIVO_ID

        database.session.delete(remove_user_grupo)
        database.session.commit()
        flash('Vinculação removida!', 'success')
        return redirect(f'/cadastro/download_arquivo/update/{id}')
    
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(f'/cadastro/download_arquivo/update/{id}')















