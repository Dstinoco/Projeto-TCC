from projeto.models import USUARIO
import pandas as pd
from projeto import app, database
from sqlalchemy import text




def usuarios_online():

	query = text(f"""
					SELECT 
					U.NOME,
					S.INICIO_SESSAO
					FROM SESSAO S
					LEFT JOIN USUARIO U ON U.USUARIO_ID = S.USUARIO_ID 
					""")
	result = database.session.execute(query)
	usuarios_onlines = result.fetchall()
	colunas = result.keys()
	
	df = pd.DataFrame(usuarios_onlines, columns=colunas)
	return df



def usuarios_por_grupo():

	query = text(f"""
					SELECT 
					U.NOME AS USUARIO,
					G.NOME AS NOME_GRUPO
					FROM USUARIO_GRUPO UG
					LEFT JOIN USUARIO U ON U.USUARIO_ID = UG.USUARIO_ID 
                    LEFT JOIN GRUPO G ON G.GRUPO_ID =  UG.GRUPO_ID       
					""")
	result = database.session.execute(query)
	usuarios_onlines = result.fetchall()
	colunas = result.keys()
	
	df = pd.DataFrame(usuarios_onlines, columns=colunas)
	return df




def total_download_arquivo():

    query = text(f"""
            SELECT 
            U.NOME AS USUARIO,
            LA.NOME AS NOME_ARQUIVO,
            UL.DATA_LOG
            FROM DOWNLOAD_LOG UL
            LEFT JOIN USUARIO U ON U.USUARIO_ID=UL.USUARIO_ID
            LEFT JOIN DOWNLOAD_ARQUIVO LA ON LA.DOWNLOAD_ARQUIVO_ID = UL.DOWNLOAD_ARQUIVO_ID""")

    

    result = database.session.execute(query)
    download = result.fetchall()
    colunas = result.keys()

    df = pd.DataFrame(download, columns=colunas)
    return df


def acessos():

    query = text(f"""
            SELECT 
            U.NOME AS USUARIO,
            UL.DATA_LOGIN
            FROM LOGIN UL
            LEFT JOIN USUARIO U ON U.USUARIO_ID=UL.USUARIO_ID
            """)

    

    result = database.session.execute(query)
    download = result.fetchall()
    colunas = result.keys()

    df = pd.DataFrame(download, columns=colunas)
    return df


