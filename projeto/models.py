from projeto import database, login_manager
from datetime import datetime, timedelta
import pytz

def time_brasil():
    time_brasil = pytz.timezone('America/Sao_Paulo')
    return datetime.now(time_brasil)



@login_manager.user_loader
def load_usuario(USUARIO_ID):
    return USUARIO.query.get(int(USUARIO_ID))
class USUARIO(database.Model):
    __tablename__ = 'USUARIO'

    USUARIO_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    NOME = database.Column(database.String(200), unique=True, nullable=False)
    PASSWORD = database.Column(database.String(200), nullable=False)
    EMAIL = database.Column(database.String(200), unique=True, nullable=False)
    STATUS = database.Column(database.String(10), unique=False, nullable=False)
    USUARIO_ATUALIZACAO  = database.Column(database.Integer, nullable=False)
    DT_ATUALIZACAO = database.Column(database.DateTime, nullable=False, default=time_brasil())
    ENG_DADOS = database.Column(database.String(1), nullable=False, default='N')
    PERMITE_EXCLUIR =database.Column(database.String(1), nullable=False, default='N')
    
    def get_id(self):
        return (self.USUARIO_ID)
    
    def is_active(self):
        return self.STATUS == 'A'
    
    def is_authenticated(self):
        return (self.USUARIO_ID)


class GRUPO(database.Model):
    __tablename__ = 'GRUPO'

    GRUPO_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    NOME = database.Column(database.String(100), unique=True, nullable=False)
    STATUS = database.Column(database.String(10), unique=False, nullable=False)
    USUARIO_ATUALIZACAO  = database.Column(database.Integer, nullable=False)
    DT_ATUALIZACAO = database.Column(database.DateTime, nullable=False, default=time_brasil())


class USUARIO_GRUPO(database.Model):
    __tablename__ = 'USUARIO_GRUPO'
    
    USUARIO_GRUPO_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    USUARIO_ID = database.Column(database.Integer, nullable=False )
    GRUPO_ID =  database.Column(database.Integer, nullable=False )


class FUNCIONALIDADE(database.Model):
    __tablename__ = 'FUNCIONALIDADE'

    FUNCIONALIDADE_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    NOME = database.Column(database.String(100), unique=True, nullable=False)
    DESCRICAO = database.Column(database.String(300), unique=True, nullable=False)


class GRUPO_FUNCIONALIDADE(database.Model):
    __tablename__ = 'GRUPO_FUNCIONALIDADE'

    GRUPO_FUNCIONALIDADE_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    GRUPO_ID = database.Column(database.Integer, nullable=False )
    FUNCIONALIDADE_ID = database.Column(database.Integer, nullable=False )


class LOGIN(database.Model):
    __tablename__ = 'LOGIN'

    LOGIN_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    USUARIO_ID = database.Column(database.Integer, nullable=False)
    DATA_LOGIN = database.Column(database.DateTime, nullable=False, default=time_brasil())
    IP = database.Column(database.String(50), nullable=False)
    USER_AGENT = database.Column(database.String(200), nullable=False)


class DOWNLOAD_ARQUIVO(database.Model):
    __tablename__ = 'DOWNLOAD_ARQUIVO'

    DOWNLOAD_ARQUIVO_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    NOME= database.Column(database.String(100), nullable=False)
    QUERY= database.Column(database.String(500), nullable=False)


class DOWNLOAD_LOG(database.Model):
    __tablename__ = 'DOWNLOAD_LOG'

    DOWNLOAD_LOG_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    USUARIO_ID = database.Column(database.Integer, nullable=False)
    DOWNLOAD_ARQUIVO_ID = database.Column(database.Integer, nullable=False)
    DATA_LOG = database.Column(database.DateTime, nullable=False, default=time_brasil())


class DOWNLOAD_ARQUIVO_GRUPO(database.Model):
    __tablename__ = 'DOWNLOAD_ARQUIVO_GRUPO'

    DOWNLOAD_ARQUIVO_GRUPO_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)
    DOWNLOAD_ARQUIVO_ID = database.Column(database.Integer, nullable=False )
    GRUPO_ID =  database.Column(database.Integer, nullable=False )
    

class SESSAO(database.Model):
    __tablename__ = 'SESSAO'

    SESSAO_ID = database.Column(database.Integer, primary_key=True, autoincrement=True)  
    USUARIO_ID = database.Column(database.Integer, nullable=False )
    INICIO_SESSAO = database.Column(database.DateTime, nullable=False)
    ULTIMA_ATIVIDADE = database.Column(database.DateTime, nullable=False)
    TEMPO_EXPIRACAO = database.Column(database.DateTime, nullable=False)


