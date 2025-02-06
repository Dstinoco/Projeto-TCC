from flask import redirect, request, url_for, flash, render_template, g
from projeto import database

from projeto.models import FUNCIONALIDADE, GRUPO_FUNCIONALIDADE, USUARIO
from projeto.forms import FormFuncionalidade, FormFuncionalidadeGrupo
from projeto.querys import grupo_x_funcionalidade_filtrado
from projeto.funcoes import grupo_x_funcionalidade_for_forms_and_table


def cadastrar_funcionalidade():

    try:
        form = FormFuncionalidade()
        func = FUNCIONALIDADE.query.all()

        if request.method == 'POST':

            if request.form.get('form') == 'cadastro_form':

                nova_funcionalidade = FUNCIONALIDADE(
                    NOME = form.nome.data,
                    DESCRICAO = form.descricao.data
                )
                database.session.add(nova_funcionalidade)
                database.session.commit()

                if form.grupo.data:
                    nova_func = FUNCIONALIDADE.query.filter_by(NOME= form.nome.data).first()
                    novo_vinculo = GRUPO_FUNCIONALIDADE(
                            FUNCIONALIDADE_ID = nova_func.FUNCIONALIDADE_ID,
                            GRUPO_ID = form.grupo.data

                        )
                    database.session.add(novo_vinculo)
                    database.session.commit()

                flash("Funcionalidade cadastrada com sucesso!", 'success')
                return redirect(url_for("cadastrar_funcionalidade"))
            
            elif request.form.get('form') == 'delete_form':
                user_delete_id = request.form.get('deleteID')

                return redirect(url_for('deletar_funcionalidade', id=user_delete_id))



    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastrar_funcionalidade'))
    
    return render_template("funcionalidade/cadastrar_funcionalidade.html", form=form, func=func)



def deletar_funcionalidade(id):
    
    try:
        usuario = USUARIO.query.filter_by(USUARIO_ID = g.id_user).first()

        if usuario.PERMITE_EXCLUIR == 'S':

            remover_func = FUNCIONALIDADE.query.filter_by(FUNCIONALIDADE_ID = id).first()

            database.session.delete(remover_func)
            database.session.commit()
            flash("Funcionalidade removida com sucesso!", 'success')
            return redirect(url_for("cadastrar_funcionalidade"))
        else:
            flash("Você não possui permissão de exclusão", "danger")
            return redirect(url_for('cadastrar_funcionalidade'))

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastrar_funcionalidade'))
    

def editar_funcionalidade(id):

    try:
        func_grupo = grupo_x_funcionalidade_for_forms_and_table("table", query=grupo_x_funcionalidade_filtrado(id))
        form = FormFuncionalidade()
        editar_func = FUNCIONALIDADE.query.filter_by(FUNCIONALIDADE_ID = id).first()

        if request.method == 'POST':
            if request.form.get('form') == 'cadastro_form':

                editar_func.NOME = form.nome.data
                editar_func.DESCRICAO = form.descricao.data

                database.session.commit()
                flash("Funcionalidade Alterada!", 'success')
                return redirect(f'/cadastro/funcionalidade/update/{id}')
           
            elif request.form.get("form") == 'add_grupo_form' :
                novo_vinculo = GRUPO_FUNCIONALIDADE(
                    FUNCIONALIDADE_ID = id,
                    GRUPO_ID = form.grupo.data
                )
                database.session.add(novo_vinculo)
                database.session.commit()
                flash("Funcionalidade Alterada!", 'success')
                return redirect(f'/cadastro/funcionalidade/update/{id}')




    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastrar_funcionalidade'))
    
    return render_template('funcionalidade/update_funcionalidade.html', form=form, func=editar_func, func_grupo=func_grupo)





