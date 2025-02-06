from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from projeto import app




def serializar_token(token):
    secret_key = app.config['SECRET_KEY']
    salt = 'ImRvdWdsYXM'

    serializar = URLSafeTimedSerializer(secret_key)
    token_serializado = serializar.dumps(token, salt=salt)

    return token_serializado



def deserializar_token(token):


    secret_key = app.config['SECRET_KEY']
    salt = 'ImRvdWdsYXM'

    serializer = URLSafeTimedSerializer(secret_key)

    chave = serializer.loads(token, salt=salt, max_age=3600)

    return chave



def deserializar_token_48hs(token):


    secret_key = app.config['SECRET_KEY']
    salt = 'ImRvdWdsYXM'

    serializer = URLSafeTimedSerializer(secret_key)

    chave = serializer.loads(token, salt=salt, max_age=3600*48)

    return chave


def deserializar_token_fast_time(token):


    secret_key = app.config['SECRET_KEY']
    salt = 'ImRvdWdsYXM'

    serializer = URLSafeTimedSerializer(secret_key)

    chave = serializer.loads(token, salt=salt, max_age=25)

    return chave


    






