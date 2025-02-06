from ..dashboard.portal_dados import layout_pd
from ..dashboard.negado import layout_negado

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from projeto import app, database, app_dash
from flask_login import current_user
from sqlalchemy import text
from projeto.models import time_brasil
import pandas as pd
from ..logica_funcionalidade import checar_permissao, redirecionar
from flask import redirect





app_dash.layout = dbc.Container(fluid=True, style={'background-color': '#f2f2f2'},
                                className="container py-3",
children=[
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='auth-state', storage_type='session', data=False),
    
        html.Div(id='conteudo', )
            

    
], )


@app_dash.callback(
        Output('conteudo', 'children'),
        Input('url', 'pathname'))
def carregar_pagina(pathname):
    if current_user.is_authenticated:
        if pathname == '/dashboard/portal_dados':
            permissoes = checar_permissao() 
            if 1 in permissoes:
                return layout_pd
    
            return layout_negado

        else:
            return dcc.Location(pathname='/index', id='login')
            
    else: 
        return dcc.Location(pathname='/login', id='login')








