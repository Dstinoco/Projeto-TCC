from projeto.logica_funcionalidade import pegar_grupos_do_usuario

from projeto import app, database
from sqlalchemy import text





def query_download_arquivo():
    grupo_ids = pegar_grupos_do_usuario()
    list_grupos_str = ', '.join(map(str, grupo_ids))
    return text(f"""
                SELECT
                DOWNLOAD_ARQUIVO_ID AS ID
                FROM DOWNLOAD_ARQUIVO_GRUPO
                WHERE GRUPO_ID IN ({list_grupos_str})""")


def checar_permissao_arquivos(query):
    lista_arquivos = []

    resultado = database.session.execute(query)
    resultado_list = resultado.fetchall()
    keys = resultado.keys()
    arquivos_dict = [dict(zip(keys, row)) for row in resultado_list]

    for arquivo_id in arquivos_dict:
        lista_arquivos.append(arquivo_id['ID'])

    return lista_arquivos




