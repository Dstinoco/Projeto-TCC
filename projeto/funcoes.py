from projeto.models import GRUPO, USUARIO, FUNCIONALIDADE, DOWNLOAD_ARQUIVO
from sqlalchemy import text
from projeto import database, app
import random

from projeto.querys import (grupo_x_usuarios, grupo_x_funcionalidade, retorno_usuario_in_grupo, retorno_funcionalidade_in_grupo,
                            retorno_download_in_grupo)
from projeto.logica_visualizar_arquivo import checar_permissao_arquivos, query_download_arquivo
from projeto.logica_funcionalidade import pegar_grupos_do_usuario

def get_grupo():
    grupos = GRUPO.query.all()
    return [(grupo.GRUPO_ID, grupo.NOME) for grupo in grupos ]


def get_usuario():
    usuarios = USUARIO.query.filter_by(STATUS = 'A').all()
    return [(usuario.USUARIO_ID, usuario.NOME )for usuario in usuarios]




def get_funcionalidade():
    funcionalidades = FUNCIONALIDADE.query.all()

    return [(funcionalidade.FUNCIONALIDADE_ID, funcionalidade.NOME) for funcionalidade in funcionalidades]

def get_download_arquivo():
    grupos = pegar_grupos_do_usuario()
    if 1 in grupos:
        downloads = DOWNLOAD_ARQUIVO.query.all()
        choices = [(0, 'Selecione o arquivo')] 
        choices += [(download.DOWNLOAD_ARQUIVO_ID, download.NOME) for download in downloads]
    else:
        query = query_download_arquivo()
        ids = checar_permissao_arquivos(query)
        downloads = DOWNLOAD_ARQUIVO.query.filter(DOWNLOAD_ARQUIVO.DOWNLOAD_ARQUIVO_ID.in_(ids))
        choices = [(0, 'Selecione o arquivo')] 
        choices += [(download.DOWNLOAD_ARQUIVO_ID, download.NOME) for download in downloads]

    return choices

# funcoes de querys

def grupo_x_usuario_for_forms_and_table(modelo, query):

    with app.app_context():
        
        result = database.session.execute(query)
        keys= result.keys()
        result_list = result.fetchall()

    if modelo == 'table':
        usuarios = [dict(zip(keys, row)) for row in result_list]    
    elif modelo == 'form':
        usuarios = [(row[0], f"{row[1]}, {row[2]}") for row in result_list]
    else:
        raise ValueError("Valor invalido, usar apenas 'table' ou 'form' ")
    
    return usuarios
    



def grupo_x_funcionalidade_for_forms_and_table(modelo, query):

    with app.app_context():
       
        result = database.session.execute(query)
        result_list = result.fetchall()
        keys = result.keys()

    if modelo == 'table':
        func = [dict(zip(keys, row)) for row in result_list]
    elif modelo == 'form':
        func = [(row[0], f"{row[1]}, {row[2]}") for row in result_list]
    else:
        raise ValueError("Valor invalido, usar apenas 'table' ou 'form' ")
    
    return func


def grupo_x_download_arquivo_for_forms_and_table(modelo, query):

    with app.app_context():
       
        result = database.session.execute(query)
        result_list = result.fetchall()
        keys = result.keys()

    if modelo == 'table':
        func = [dict(zip(keys, row)) for row in result_list]
    elif modelo == 'form':
        func = [(row[0], f"{row[1]}, {row[2]}") for row in result_list]
    else:
        raise ValueError("Valor invalido, usar apenas 'table' ou 'form' ")
    
    return func


def retornar_usuarios_de_grupo(grupo_id):
    with app.app_context():
        result = database.session.execute(retorno_usuario_in_grupo(grupo_id))
        result_list = result.fetchall()
        keys =result.keys()

        users = [dict(zip(keys, row)) for row in result_list]
        return users
    

def retornar_funcionalidade_de_grupo(grupo_id):
    with app.app_context():
        result = database.session.execute(retorno_funcionalidade_in_grupo(grupo_id))
        result_list = result.fetchall()
        keys =result.keys()

        users = [dict(zip(keys, row)) for row in result_list]
        return users
    

def retornar_download_de_grupo(grupo_id):
    with app.app_context():
        result = database.session.execute(retorno_download_in_grupo(grupo_id))
        result_list = result.fetchall()
        keys =result.keys()

        users = [dict(zip(keys, row)) for row in result_list]
        return users



#função gerar cod aleatorio 8 digitos

def gerar_codigo_aleatorio():
    cod_aleatorio = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.@!#*&', k=8))
    return cod_aleatorio
