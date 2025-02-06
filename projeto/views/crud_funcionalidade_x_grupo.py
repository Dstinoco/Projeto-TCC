from projeto import database
from flask import request, redirect, url_for, render_template, flash

from projeto.models import GRUPO_FUNCIONALIDADE
from projeto.forms import FormFuncionalidadeGrupo
from projeto.funcoes import grupo_x_funcionalidade_for_forms_and_table
from projeto.querys import grupo_x_funcionalidade_filtrado


def cadastrar_funcionalidade_x_grupo():

    try:
        form = FormFuncionalidadeGrupo()
        func = grupo_x_funcionalidade_for_forms_and_table('table', query=grupo_x_funcionalidade_filtrado)
        

        if request.method == 'POST':
            nova_func = GRUPO_FUNCIONALIDADE(
                FUNCIONALIDADE_ID = form.funcionalidade.data,
                GRUPO_ID = form.grupo.data
            )
            database.session.add(nova_func)
            database.session.commit()
            flash("Funcionalidade vinculada!", 'success')
            return redirect(url_for('cadastrar_funcionalidade_grupo')) 


    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastrar_funcionalidade_grupo'))
    
    return render_template('funcionalidade/cadastro_funcionalidade_grupo.html', form=form, func=func)


def deletar_funcionalidade_x_grupo(id):

    try:
        remover_func = GRUPO_FUNCIONALIDADE.query.filter_by(GRUPO_FUNCIONALIDADE_ID = id).first()
        database.session.delete(remover_func)
        database.session.commit()
        flash('funcionalidade desvinculada!', 'success')
        return redirect(f'/cadastro/funcionalidade/update/{id}')


    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(f'/cadastro/funcionalidade/update/{id}')