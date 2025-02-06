from flask import redirect, flash, url_for, request, render_template

from projeto import database
from projeto.models import DOWNLOAD_ARQUIVO, DOWNLOAD_ARQUIVO_GRUPO
from projeto.forms import FormDownloadArquivo
from projeto.funcoes import grupo_x_download_arquivo_for_forms_and_table
from projeto.querys import grupo_x_download_arquivo_filtrado




def cadastrar_arquivo():
    try:
        form = FormDownloadArquivo()
        download_arquivos = DOWNLOAD_ARQUIVO.query.all()

        if request.method == 'POST':

            if request.form.get('form') == 'cadastro_form':
                novo_cadastro = DOWNLOAD_ARQUIVO(
                    NOME = form.nome.data,
                    QUERY = form.query.data
                )
                database.session.add(novo_cadastro)
                database.session.commit()
            
                if form.grupo.data:

                    cadastro_grupo = DOWNLOAD_ARQUIVO.query.filter_by(NOME = form.nome.data).first()
                    novo_vinculo = DOWNLOAD_ARQUIVO_GRUPO(
                        GRUPO_ID = form.grupo.data,
                        DOWNLOAD_ARQUIVO_ID = cadastro_grupo.DOWNLOAD_ARQUIVO_ID
                    )
                    database.session.add(novo_vinculo)
                    database.session.commit()
                    flash("Cadastro realizado!", 'success')
                    return redirect(url_for('cadastrar_download_arquivo'))
                else:
                    flash("Cadastro realizado!", 'success')
                    return redirect(url_for('cadastrar_download_arquivo'))
                
            elif request.form.get('form') == 'delete_form':

                delete_id = request.form.get('deleteID')

                return redirect(url_for('deletar_download_arquivo', id=delete_id))


    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastrar_download_arquivo'))
    
    return render_template("arquivo/cadastro_download_arquivo.html", form=form, arquivos=download_arquivos)


def update_arquivo(id):

    try:
        query = grupo_x_download_arquivo_filtrado(id)
        form = FormDownloadArquivo()
        editar_download = DOWNLOAD_ARQUIVO.query.filter_by(DOWNLOAD_ARQUIVO_ID = id).first()
        arquivos = DOWNLOAD_ARQUIVO.query.all()
        arquivo_grupo = grupo_x_download_arquivo_for_forms_and_table("table", query=query)

        if request.method == 'GET':
            form.query.data = editar_download.QUERY

        if request.method == 'POST':
            if request.form.get("form") == 'update_form':

                editar_download.NOME = form.nome.data
                editar_download.QUERY = form.query.data
                database.session.commit()
                flash("Alteração Realizada!", 'success')
                return redirect(f'/cadastro/download_arquivo/update/{id}')
            
            elif request.form.get('form') == 'add_grupo_form':
                vincular_grupo = DOWNLOAD_ARQUIVO_GRUPO(
                    GRUPO_ID = form.grupo.data,
                    DOWNLOAD_ARQUIVO_ID = id
                )
                database.session.add(vincular_grupo)
                database.session.commit()
                flash("Grupo Vinculado!", 'success')
                return redirect(f'/cadastro/download_arquivo/update/{id}')


    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(f'/cadastro/download_arquivo/update/{id}')
    
    return render_template("arquivo/update_download_arquivo.html", form=form, update=editar_download, arquivos=arquivos, arquivo_grupo=arquivo_grupo)


def deletar_arquivo(id):
    try:
        deletar_arquivo = DOWNLOAD_ARQUIVO.query.filter_by(DOWNLOAD_ARQUIVO_ID = id).first()

        database.session.delete(deletar_arquivo)
        database.session.commit()
        flash("Cadastro excluido!", "success")
        return redirect(url_for('cadastrar_download_arquivo'))

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('cadastrar_download_arquivo'))
    


