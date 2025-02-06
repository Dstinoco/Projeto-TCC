from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_required, login_user, logout_user
from projeto import server, bcrypt, app
from dash import html, dcc, Input, Output



@app.callback(
        Output('conteudo', 'children'),
        Input('url', 'pathname'))
def carregar_pagina(pathname):
    if current_user.is_authenticated:
        if pathname == '/':
            return dcc.Location(pathname='/login', id='login')
        elif pathname == '/sair':
            return logout_user() and dcc.Location(pathname='/login', id='login')
        else:
            return dcc.Location(pathname='/dashboard', id='login')
            
    else: 
        return dcc.Location(pathname='/login', id='login')
    



@app.callback(
    Output('sidebar-name', 'children'),
    [Input('url', 'pathname')])
def update_username_display(pathname):
    if current_user.is_authenticated:
        username = current_user.nome

        return f"{username}"
    return None



