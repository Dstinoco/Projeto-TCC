from projeto.models import SESSAO
from projeto import database, app
from datetime import datetime, timedelta
import pytz


def time_brasil():
    time_brasil = pytz.timezone('America/Sao_Paulo')
    return datetime.now(time_brasil)


def inicio_sessao(user_id):
    nova_sessao = SESSAO(

        USUARIO_ID = user_id,
        INICIO_SESSAO = time_brasil(),
        ULTIMA_ATIVIDADE = time_brasil(),
        TEMPO_EXPIRACAO = time_brasil() + timedelta(minutes=30)
    )
    database.session.add(nova_sessao)
    database.session.commit()


def request_sessao(user_id):

    sessao = SESSAO.query.filter_by(USUARIO_ID=user_id).first()
    if sessao:
        sessao.ULTIMA_ATIVIDADE = time_brasil()
        sessao.TEMPO_EXPIRACAO = time_brasil() + timedelta(minutes=30)
        database.session.commit()
    else:
        inicio_sessao(user_id)

def remove_sessao_logout(user_id):

    sessao = SESSAO.query.filter_by(USUARIO_ID=user_id).first()
    database.session.delete(sessao)
    database.session.commit()


def remove_sessao_expiradas():
    try:
        
        with app.app_context():
            now = time_brasil()
            sessoes_expiradas = SESSAO.query.filter(SESSAO.TEMPO_EXPIRACAO <= now).all()
            for session in sessoes_expiradas:
                database.session.delete(session)
            database.session.commit()

    except Exception as e:
        print(str(e))








