from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from datetime import timedelta
from projeto.config import base, drive
from dotenv import load_dotenv
import os
load_dotenv()

username_db = os.getenv('DB_USER')
password_db = os.getenv('DB_PASSWORD1') 
host_db = os.getenv('DB_HOST')
database_db = os.getenv('DB_DATABASE')



from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Flask(__name__)


# A alteração da base deve ser feita no arquivo config.py


if base == 'HML':
    datalake_diretorio_base = 'portal_dados_hml'
    base_url = 'hml'

elif base == 'PRD':
    datalake_diretorio_base = 'portal_dados'
    base_url = 'prd'


app.config.suppress_callback_exceptions = True
app.title = 'Portal-Dados'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

app.config.update(

SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}',
#SQLALCHEMY_DATABASE_URI =  = f'postgresql://{username_db}:{password_db}@{host_db}:{porta}/{database_db}'
#SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://username_db:password_db@host_db:1433/database_db?driver={drive}",
SECRET_KEY = os.getenv('SECRET_KEY'),
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30),
SESSION_PERMANENT = True,
SQLALCHEMY_TRACK_MODIFICATIONS=False

)


database = SQLAlchemy(app)

login_manager = LoginManager()
bcrypt= Bcrypt(app)
login_manager.init_app(app)

login_manager.login_view = '/login'



# configuração DASH
app_dash = Dash(__name__, server=app, external_stylesheets=[dbc.themes.MINTY, dbc.icons.BOOTSTRAP], url_base_pathname='/dashboard/',
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app_dash.config.suppress_callback_exceptions = True
app_dash.title = 'Portal-Dados'

load_figure_template('minty')


from projeto.routes import routes
from projeto.views import login
