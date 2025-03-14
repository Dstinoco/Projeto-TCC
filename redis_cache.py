import redis
import sqlite3 
from dotenv import load_dotenv
import os
load_dotenv()
from conexao import ConectarBanco

# Conexão com Redis
redis_client = redis.StrictRedis(host='20.81.236.155', port=6379, db=0, password='tinoco@tinoco' ,decode_responses=True)

# Conexão com o Banco de Dados (SQLite como exemplo)
conn = sqlite3.connect("projeto/database.db")
cursor = conn.cursor()


# Função para buscar do banco e armazenar no Redis
def get_users():
    cache_key = "clientes"

    # Verificar se os dados estão no cache Redis
    if redis_client.exists(cache_key):
        print("Dados do cache Redis")
        return redis_client.get(cache_key)

    # Se não estiver no cache, buscar no banco
    print("Buscando do banco e armazenando no cache")
    db = ConectarBanco()
    users = db.consulta_banco('SELECT * FROM public.clientes')

    # Convertendo para string antes de salvar no Redis
    users_str = str(users)
    redis_client.setex(cache_key, 60, users_str)  # Expira em 60 segundos

    return users_str

# Testando a função
print(get_users())  # Primeira vez: banco | Depois: Redis

# Fechar conexões
cursor.close()
conn.close()
