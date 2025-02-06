from sqlalchemy import text




grupo_x_usuarios = text(f"""
                        SELECT
                        UG.USUARIO_GRUPO_ID,
                        U.NOME AS USUARIO,
                        G.NOME AS GRUPO

                        FROM USUARIO_GRUPO UG

                        LEFT JOIN USUARIO U ON U.USUARIO_ID = UG.USUARIO_ID
                        LEFT JOIN GRUPO G ON G.GRUPO_ID = UG.GRUPO_ID 
                        """)






grupo_x_funcionalidade = text(f"""
                                SELECT
                                GF.GRUPO_FUNCIONALIDADE_ID,
                                F.NOME AS NOME_FUNCIONALIDADE,
                                G.NOME AS NOME_GRUPO

                                FROM GRUPO_FUNCIONALIDADE GF

                                LEFT JOIN GRUPO G ON G.GRUPO_ID = GF.GRUPO_ID
                                LEFT JOIN FUNCIONALIDADE F ON F.FUNCIONALIDADE_ID = GF.FUNCIONALIDADE_ID
                                ORDER BY G.NOME """)



# ------------------------------- Funções ------------------------------------------------





def grupo_x_usuarios_filtrado(id):
        return text(f"""
                            SELECT
                            UG.USUARIO_GRUPO_ID,
                            U.NOME AS USUARIO,
                            G.NOME AS GRUPO

                            FROM USUARIO_GRUPO UG

                            LEFT JOIN USUARIO U ON U.USUARIO_ID = UG.USUARIO_ID
                            LEFT JOIN GRUPO G ON G.GRUPO_ID = UG.GRUPO_ID 
                            WHERE U.USUARIO_ID = {id}
                            """)
        

def grupo_x_funcionalidade_filtrado(id):
    return text(f"""
                    SELECT
                    GF.GRUPO_FUNCIONALIDADE_ID,
                    F.NOME AS NOME_FUNCIONALIDADE,
                    G.NOME AS NOME_GRUPO

                    FROM GRUPO_FUNCIONALIDADE GF

                    LEFT JOIN GRUPO G ON G.GRUPO_ID = GF.GRUPO_ID
                    LEFT JOIN FUNCIONALIDADE F ON F.FUNCIONALIDADE_ID = GF.FUNCIONALIDADE_ID
                    WHERE F.FUNCIONALIDADE_ID = {id}""")



def grupo_x_download_arquivo_filtrado(id):
    return text(f"""
                SELECT 
                DAG.DOWNLOAD_ARQUIVO_GRUPO_ID,
                DA.NOME AS NOME_ARQUIVO,
                G.NOME AS NOME_GRUPO

                FROM DOWNLOAD_ARQUIVO_GRUPO DAG

                LEFT JOIN GRUPO G ON G.GRUPO_ID = DAG.GRUPO_ID
                LEFT JOIN DOWNLOAD_ARQUIVO DA ON DA.DOWNLOAD_ARQUIVO_ID = DAG.DOWNLOAD_ARQUIVO_ID
                WHERE DA.DOWNLOAD_ARQUIVO_ID = {id} """)



def retorno_usuario_in_grupo(grupo_id):
    return text(f"""
                SELECT
                UG.USUARIO_ID,
                U.NOME

                FROM USUARIO_GRUPO UG
                LEFT JOIN USUARIO U ON U.USUARIO_ID = UG.USUARIO_ID 
                WHERE UG.GRUPO_ID = {grupo_id}
                """)


def retorno_funcionalidade_in_grupo(grupo_id):
     return text(f"""
                SELECT 
                GF.FUNCIONALIDADE_ID,
                F.NOME
                FROM GRUPO_FUNCIONALIDADE GF
                LEFT JOIN FUNCIONALIDADE F ON F.FUNCIONALIDADE_ID = GF.FUNCIONALIDADE_ID 
                WHERE GF.GRUPO_ID = {grupo_id}
                """)


def retorno_download_in_grupo(grupo_id):
     return text(f"""
                SELECT 
                DAG.DOWNLOAD_ARQUIVO_ID,
                DA.NOME
                FROM DOWNLOAD_ARQUIVO_GRUPO DAG
                LEFT JOIN DOWNLOAD_ARQUIVO DA ON DA.DOWNLOAD_ARQUIVO_ID = DAG.DOWNLOAD_ARQUIVO_ID 
                WHERE DAG.GRUPO_ID = {grupo_id}
                """)


def retorno_layout_in_grupo(grupo_id):
     return text(f"""
                SELECT 
                LG.LAYOUT_ARQUIVO_ID,
                LA.NOME
                FROM LAYOUT_GRUPO LG
                LEFT JOIN LAYOUT_ARQUIVO LA ON LA.LAYOUT_ARQUIVO_ID = LG.LAYOUT_ARQUIVO_ID 
                WHERE LG.GRUPO_ID = {grupo_id}
                """)