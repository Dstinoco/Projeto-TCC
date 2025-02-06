from projeto import app
from projeto.sessao import remove_sessao_expiradas
from apscheduler.schedulers.background import BackgroundScheduler

remove_sessao_expiradas()



if __name__ == '__main__':
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=remove_sessao_expiradas, trigger="interval", minutes=10)
    scheduler.start()

    app.run(host= '0.0.0.0', port=5000, debug=True)