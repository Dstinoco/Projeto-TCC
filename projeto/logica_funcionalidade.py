from projeto import app, database
from sqlalchemy import text

from flask import redirect, url_for, g

def pegar_grupos_do_usuario():
    usuario_id = g.id_user
    list_grupos = []
    query = text(f"""
                    SELECT
                    G.GRUPO_ID

                    FROM USUARIO_GRUPO UG

                    LEFT JOIN USUARIO U ON U.USUARIO_ID = UG.USUARIO_ID
                    LEFT JOIN GRUPO G ON G.GRUPO_ID = UG.GRUPO_ID 
                    WHERE U.USUARIO_ID = {usuario_id} """)
    
    with app.app_context():

        result = database.session.execute(query)
        result_list = result.fetchall()
        keys = result.keys()

        grupos_dict = [dict(zip(keys, row)) for row in result_list]

        for  grupo in grupos_dict:
            list_grupos.append(grupo['GRUPO_ID'])

    return list_grupos


def checar_permissao():
    
    list_funcionalidade = []
    grupo_ids = pegar_grupos_do_usuario()

    
    
    if not grupo_ids: # usuario sem nenhum grupo
        return redirecionar()      

    list_grupos_str = ', '.join(map(str, grupo_ids))
    with app.app_context():

        query = text(f"""
                        SELECT
                        FUNCIONALIDADE_ID

                        FROM GRUPO_FUNCIONALIDADE GF
                        
                        WHERE GRUPO_ID IN({list_grupos_str})""")
        
        result = database.session.execute(query)
        result_list = result.fetchall()
        keys = result.keys()
        func_dict = [dict(zip(keys, row)) for row in result_list]

        for func in func_dict:
            list_funcionalidade.append(func['FUNCIONALIDADE_ID'])
            
        #permissao = True if funcionalidade_id in list_funcionalidade else False
        return list_funcionalidade
    

def redirecionar():
    return redirect(url_for('acesso_negado'))




       