from flask import flash, redirect, url_for, request, render_template, Response, g
import csv
from io import StringIO, BytesIO
import pandas as pd
from projeto import database

from projeto.models import DOWNLOAD_ARQUIVO, DOWNLOAD_LOG
from projeto.forms import FormDownloadArquivo
from projeto.conexao import ConectarBanco



def baixar_csv():
    try:
        form = FormDownloadArquivo()
        id_user = g.id_user

        if request.method == 'POST':
            get_guery = DOWNLOAD_ARQUIVO.query.filter_by(DOWNLOAD_ARQUIVO_ID = form.select_download.data).first()
            query = get_guery.QUERY
            query = query.replace("\n", ' ').replace("''", "'")
            print(query)
            db = ConectarBanco()
            dados = db.consulta_banco(query=query)
                
            
            df = pd.DataFrame(dados)
            si = BytesIO()
            df.to_csv(si, index=False, sep=';')
     
            tabela = si.getvalue()
            si.close()
            if tabela:
                salvar_log = DOWNLOAD_LOG(
                    USUARIO_ID= id_user,
                    DOWNLOAD_ARQUIVO_ID=get_guery.DOWNLOAD_ARQUIVO_ID
                )
                database.session.add(salvar_log)
                database.session.commit()

                return Response(
                    tabela,
                    mimetype="text/csv",
                    headers={"Content-Disposition": f"attachment;filename={get_guery.NOME}.csv"}
                )


    
    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('download_csv'))
    
    return render_template("arquivo/download_arquivo.html", form=form)