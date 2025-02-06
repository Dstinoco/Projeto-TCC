
from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from projeto.models import USUARIO, DOWNLOAD_LOG, DOWNLOAD_ARQUIVO, SESSAO, time_brasil, LOGIN
from projeto import app, database, app_dash

from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
from sqlalchemy import text

from projeto.dashboard.header import cabecalho
from projeto.dashboard.portal_dados_query import total_download_arquivo, usuarios_online, acessos, usuarios_por_grupo


hora_atual = time_brasil()

dia_hoje = datetime.now().date() + timedelta(days=1)
#dia_ontem = dia_hoje - timedelta(days=1)

#-----------------style ---------------------------------------------

card_icon = {
    "color": "black",
    "text-align": "center",
    "fontSize": "50px",
    'margin-top': '10px'
}

span_text={'padding-top': '20px', 'background-color': 'white','font-family': 'Roboto','font-weight': 'bolder','font-size':'12px'}
icon_text={'background-color': '#7cc4ac', 'color': 'white', 'width': '15vh', "text-align": 'right', 'font-size': '45px'}
#7cc4ac
#597c00
#-----------------style ---------------------------------------------





#-----------------Contexto ---------------------------------------------


with app.app_context():

        df_online = usuarios_online()

        
df_online['INICIO_SESSAO']  = pd.to_datetime(df_online['INICIO_SESSAO'], format='%Y-%m-%d %H:%M:%S.%f')
df_online['INICIO_SESSAO'] = df_online['INICIO_SESSAO'].dt.tz_localize('America/Sao_Paulo')
df_online['TEMPO_LOGADO'] = hora_atual - df_online['INICIO_SESSAO']
df_online['TEMPO_LOGADO'] = df_online['TEMPO_LOGADO'].astype(str).str.split('.').str[0]



#-----------------Contexto ---------------------------------------------












tabela = dash_table.DataTable(
    columns=[{"name": "USUARIO ONLINE", "id": "NOME"}, {"name": "TEMPO_LOGADO", "id": "TEMPO_LOGADO"}],
    style_table={'width': '50%', 'margin': 'auto'},
    style_cell={'textAlign': 'center'},
    style_header={'backgroundColor': '#f2f2f2', 'fontWeight': 'bold', 'color': '#7cc4ac'},
    style_data={'backgroundColor': 'white', 'color': 'black'},
    id="tabela-usuarios-online"
    
)







layout_pd = html.Div([ cabecalho,

      
        dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Intervalo em milissegundos (10 segundos)
        n_intervals=0
    ),


        




        dbc.Row([
             
        dbc.Col([
                html.H5("Data inicial", style={
                "font-style": "normal",
                "font-weight": "700",
                "font-size": "18px",
                "text-align": "center",
                "color": "rgb(79, 79, 79)",
                "margin": "10px auto"
            },className='my-auto'),
                dcc.DatePickerSingle(      
                id='data-inicio',
                date='2025-01-01',  # Data inicial
                display_format='DD/MM/YYYY',  # Formato de exibição
                 className="m-2")
        ], className="d-flex justify-content-center col-3" ),

        dbc.Col([
                html.H5("Data final", style={
                "font-style": "normal",
                "font-weight": "700",
                "font-size": "18px",
                "text-align": "center",
                "color": "rgb(79, 79, 79)",
                "margin": "10px auto"
            },className='my-auto'),
                dcc.DatePickerSingle(
                id='data-fim',
                date=dia_hoje,  # Data inicial
                display_format='DD/MM/YYYY',  # Formato de exibição
                 className="m-2")
        ], className="d-flex justify-content-center col-3 " )




        ], className="border rounded mt-5", justify="center"),

        dbc.Row([
                

                dbc.Col([
                    dbc.InputGroup(
                        [
                            html.Span(html.P(id='texto-acesso'), className='form-control', style=span_text),
                            html.Span( html.I(className='bi bi-door-open-fill m-auto '), className='input-group-text text-justify', style=icon_text ),
                        ], style=card_icon, className="")

                
                        ], className="d-flex justify-content-center col-3 "),
            
            
        

            
                dbc.Col([
                    dbc.InputGroup(
                        [
                            html.Span(html.P(id='texto-download'), className='form-control', style=span_text),
                            html.Span( html.I(className='bi bi-file-earmark-arrow-down m-auto'), className='input-group-text text-justify', style=icon_text ),
                        ], style=card_icon, className="")
                                ], className="d-flex justify-content-center col-3"),

                
                 dbc.Col([
                    dbc.InputGroup(
                        [
                            html.Span(html.P(id='texto-cadastro-user'), className='form-control', style=span_text),
                            html.Span( html.I(className='bi bi-people-fill m-auto'), className='input-group-text text-justify', style=icon_text ),
                        ], style=card_icon, className="")
                                ], className="d-flex justify-content-center col-3")


                ], justify="center", className="container mt-5 m-auto"),





                dbc.Row([

                        dbc.Col([

                                dcc.Graph(id='download-fig',style={"height": '35vh',"border-radius": '30px'},),
                        ], className="col-6"),



                        dbc.Col([

                                dcc.Graph(id='download-arquivo-fig',style={"height": '35vh'}),

                        ], className="col-6"),

                ], justify="center", className="container mt-5 m-auto"),



                dbc.Row([

                        dbc.Col([

                                dcc.Graph(id='acessos-fig',style={"height": '35vh'}),
                        ], className="col-12"),



                        

                ], justify="center", className="container mt-5  m-auto"),







                dbc.Row(
                        [
                             
                            dbc.Col([

                                dcc.Graph(id='grupo-fig',style={"height": '35vh'}),

                                ], className="col-5"),



                           dbc.Col([
                                html.H5("USUARIOS ONLINE", className="text-center"),
                                tabela 

                                   ], className="col-7")   

                        ], justify="center", className="container mt-5 m-auto")

             
], className="container", style={'background-color': '#f2f2f2'})

















#-----------------Callbacks ---------------------------------------------




@app_dash.callback(
    Output('tabela-usuarios-online', 'data'),
    Input('interval-component', 'n_intervals')
)
def update_table(n_intervals):
    hora_atual = time_brasil()
    with app.app_context():
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

    
    
   

    df_online = pd.DataFrame(usuarios_onlines, columns=colunas)
    df_online['INICIO_SESSAO']  = pd.to_datetime(df_online['INICIO_SESSAO'], format='%Y-%m-%d %H:%M:%S.%f')
    df_online['INICIO_SESSAO'] = df_online['INICIO_SESSAO'].dt.tz_localize('America/Sao_Paulo')
    df_online['TEMPO_LOGADO'] = hora_atual - df_online['INICIO_SESSAO']
    
    df_online['TEMPO_LOGADO'] = df_online['TEMPO_LOGADO'].astype(str).str.split('.').str[0]
    df_online['TEMPO_LOGADO'] = df_online['TEMPO_LOGADO'].str.replace(r'0 days ', '', regex=True)

    online_list = df_online[['NOME', 'TEMPO_LOGADO']].to_dict(orient='records')
    
    return online_list






@app_dash.callback([    
     Output('download-fig','figure'),
     Output('download-arquivo-fig','figure'),
     Output('acessos-fig','figure'),
     Output('grupo-fig','figure'),

     Output('texto-acesso','children'),
     Output('texto-download','children'),
     Output('texto-cadastro-user','children'),
     ],

     [Input('data-inicio', 'date'),
      Input('data-fim', 'date')]

)
def manipular_graficos(dt_inicio, dt_fim):

    hora_atual = time_brasil()

     
    with app.app_context():

        download_df = total_download_arquivo()
        usuarios = USUARIO.query.all()
        acessos_df = acessos()
        usuarios_grupo = usuarios_por_grupo()

        download_df = download_df[(download_df["DATA_LOG"] >= dt_inicio) & (download_df["DATA_LOG"] <= dt_fim)]
        acessos_df = acessos_df[(acessos_df["DATA_LOGIN"] >= dt_inicio) & (acessos_df["DATA_LOGIN"] <= dt_fim)]


    usuarios_df = pd.DataFrame(usuarios)




    titulo_bar = {
        'y':0.9,  # Posição vertical do título (0 é a base, 1 é o topo)
        'x':0.5,  # Posição horizontal do título (0 é a esquerda, 1 é a direita)
        'xanchor': 'center',  # Define o ancoramento horizontal
        'yanchor': 'top'  # Define o ancoramento vertical
    }



    


    texto_acesso = f"TOTAL ACESSOS: {len(acessos_df)}"
    texto_download = f"TOTAL DOWNLOADS {len(download_df)}"
    texto_cadastro_user = f"CADASTROS USUARIOS {len(usuarios_df)}"



    download_df_agrupado = download_df.groupby("USUARIO").size().reset_index(name="TOTAL DOWNLOAD").sort_values("TOTAL DOWNLOAD", ascending=False)
    download_fig = px.bar(download_df_agrupado, x="USUARIO", y='TOTAL DOWNLOAD', title="Download feito por usuario", color='USUARIO', text='TOTAL DOWNLOAD')
    download_fig.update_layout(title=titulo_bar)

    download_df_agrupado_arquivo = download_df.groupby("NOME_ARQUIVO").size().reset_index(name="TOTAL DOWNLOAD").sort_values("TOTAL DOWNLOAD", ascending=False)
    download_arquivo_fig = px.pie(download_df_agrupado_arquivo, names="NOME_ARQUIVO", values='TOTAL DOWNLOAD', title="Download por arquivo", color='NOME_ARQUIVO')
    download_arquivo_fig.update_layout(title=titulo_bar)


    acessos_df_agrupados = acessos_df.groupby("USUARIO").size().reset_index(name="LOGINS EFETUADO").sort_values("LOGINS EFETUADO", ascending=False)
    acessos_fig = px.bar(acessos_df_agrupados, x="USUARIO", y='LOGINS EFETUADO', title="Login efetuado por usuario", color='USUARIO', text='LOGINS EFETUADO')
    acessos_fig.update_layout(title=titulo_bar)

    #online_list = df_online[['NOME', 'TEMPO_LOGADO']].to_dict(orient='records')


    usuarios_grupo_df = usuarios_grupo.groupby('NOME_GRUPO').size().reset_index(name='USUARIOS_POR_GRUPO')
    usuarios_grupo_fig = px.pie(usuarios_grupo_df, names='NOME_GRUPO', values='USUARIOS_POR_GRUPO', title='Total de usuarios em cada grupo', color='NOME_GRUPO')
    usuarios_grupo_fig.update_layout(title=titulo_bar)


    return download_fig, download_arquivo_fig, acessos_fig, usuarios_grupo_fig, texto_acesso, texto_download, texto_cadastro_user



#-----------------Callbacks ---------------------------------------------
