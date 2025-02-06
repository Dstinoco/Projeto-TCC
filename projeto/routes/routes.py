from projeto import app, database, bcrypt
from flask_login import login_manager, login_required, logout_user, current_user
from flask import redirect, render_template, flash, session, url_for, g

from projeto.views import (crud_grupo, crud_usuario, login, crud_funcionalidade, 
crud_funcionalidade_x_grupo, download_arquivo, crud_download_arquivo,alterar_cadastro, email
)

from ..logica_funcionalidade import checar_permissao, redirecionar
from projeto.sessao import request_sessao, remove_sessao_logout

from projeto.routes import routes_dash





@app.before_request
def before_request():
    session.permanent = True

    if current_user.is_authenticated:
        g.nome_user = current_user.NOME
        g.id_user = current_user.USUARIO_ID
        primeiro_nome = str(current_user.NOME).split(" ")
        g.primeiro_nome = primeiro_nome[0]
        request_sessao(current_user.USUARIO_ID)
      

    else:
        g.nome_user = 'Convidado'   
        print(type(current_user))






# ----------------------------------------------------------------------------------------

#         CRUD CADASTRO DE USUARIO

@app.route('/cadastro/usuario', methods=['GET', 'POST'])
@login_required
def cadastro_usuario():
    permissoes = checar_permissao() 
    if 1 in permissoes:
        return crud_usuario.Cadastro_User()
    
    return redirecionar()   

    
@app.route("/cadastro/usuario/delete/<int:id>")
@login_required
def delete_usuario(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_usuario.Delete_User(id)
    
    return redirecionar() 


@app.route("/cadastro/usuario/inactivate/<int:id>")
@login_required
def status_usuario(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_usuario.Status_User(id)
    
    return redirecionar() 


@app.route("/cadastro/usuario/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update_usuario(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_usuario.Update_User(id)
    
    return redirecionar() 

#         CRUD CADASTRO DE USUARIO
    
# ----------------------------------------------------------------------------------------

#         CRUD CADASTRO DE GRUPO

@app.route("/cadastro/grupo", methods=['GET', 'POST'])
@login_required
def grupo():
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_grupo.Cadastrar_Grupo()
    
    return redirecionar() 


@app.route('/cadasto/grupoxusuario/delete/<int:id>')  
@login_required
def delete_grupo_x_usuario(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_grupo.Delete_Grupo_x_Usuario(id)
    
    return redirecionar() 


@app.route('/cadastro/grupo/delete/<int:id>')
@login_required
def delete_grupo(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_grupo.Delete_Grupo(id)
    
    return redirecionar() 


#         CRUD CADASTRO DE GRUPO

# ----------------------------------------------------------------------------------------



#         CRUD FUNCIONALIDADE

@app.route('/cadastro/funcionalidade', methods=['GET', 'POST'])
@login_required
def cadastrar_funcionalidade():
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_funcionalidade.cadastrar_funcionalidade()
    
    return redirecionar() 


@app.route("/cadastro/funcionalidade/delete/<int:id>")
@login_required
def deletar_funcionalidade(id):
    return crud_funcionalidade.deletar_funcionalidade(id)


@app.route("/cadastro/funcionalidade/update/<int:id>", methods=['GET', 'POST'])
@login_required
def editar_funcionalidade(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_funcionalidade.editar_funcionalidade(id)
    
    return redirecionar() 



#         CRUD FUNCIONALIDADE

# ----------------------------------------------------------------------------------------



#         CRUD FUNCIONALIDADE X GRUPO

@app.route('/cadastro/funcionalidade_grupo', methods=['GET', 'POST'])
@login_required
def cadastrar_funcionalidade_grupo():
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_funcionalidade_x_grupo.cadastrar_funcionalidade_x_grupo()
    
    return redirecionar() 


@app.route('/cadastro/funcionalidade_grupo/delete/<int:id>', methods=['GET'])
@login_required
def deletar_funcionalidade_grupo(id):
    permissoes = checar_permissao()
    if 1 in permissoes:
        return crud_funcionalidade_x_grupo.deletar_funcionalidade_x_grupo(id)
    
    return redirecionar() 


#         CRUD FUNCIONALIDADE X GRUPO

# ----------------------------------------------------------------------------------------


#         CRUD DOWNLOAD ARQUIVO

@app.route("/cadastro/download_arquivo", methods=['POST', 'GET'])
@login_required
def cadastrar_download_arquivo():
    permissoes = checar_permissao()
    if 1 in  permissoes:
        return crud_download_arquivo.cadastrar_arquivo()
    
    return redirecionar()


@app.route("/cadastro/download_arquivo/update/<int:id>", methods=['POST', 'GET'])
@login_required
def editar_download_arquivo(id):
    permissoes = checar_permissao()
    if 1 in  permissoes:
        return crud_download_arquivo.update_arquivo(id)
    
    return redirecionar()


@app.route("/cadastro/download_arquivo/delete/<int:id>", methods=['POST', 'GET'])
@login_required
def deletar_download_arquivo(id):
    permissoes = checar_permissao()
    if 1 in  permissoes:
        return crud_download_arquivo.deletar_arquivo(id)
    
    return redirecionar()


@app.route("/cadastro/download_arquivo_grupo/delete/<int:id>", methods=['POST', 'GET'])
@login_required
def deletar_download_arquivo_grupo(id):
    permissoes = checar_permissao()
    if 1 in  permissoes:
        return crud_grupo.delete_grupo_x_download_arquivo(id)
    
    return redirecionar()



#         CRUD DOWNLOAD ARQUIVO

# ----------------------------------------------------------------------------------------


#          NAVEGAÇÃO



@app.route("/index") # pagina de navegacao
@login_required
def index():
    permissoes = checar_permissao()

    return render_template('index.html', permissoes=permissoes)



@app.route("/seguranca") # pagina de navegacao
@login_required
def seguranca():
    permissoes = checar_permissao()

    return render_template('seguranca.html', permissoes=permissoes)



@app.route("/dashboard") # pagina de navegacao
@login_required
def dashboard():
    permissoes = checar_permissao()

    return render_template('dashboards.html', permissoes=permissoes)


#          NAVEGAÇÃO

# ----------------------------------------------------------------------------------------


#          ROTAS FUNCIONALIDADES

@app.route("/download_arquivo", methods=['POST', 'GET'])
@login_required
def download_csv():
    permissoes = checar_permissao()
    if 1 in  permissoes or 2 in permissoes:
        return download_arquivo.baixar_csv()
    
    return redirecionar()



#          ROTAS FUNCIONALIDADES

# ----------------------------------------------------------------------------------------


#          ROTAS REDEFINICAO SENHA

@app.route("/recuperacao_senha", methods=["POST", "GET"])
def recuperar_senha():

    return email.solicitar_redefinicao_senha()


@app.route("/redefinir_senha/<string:token>", methods=["POST", "GET"])
def redefinir_senha(token):

    return email.redefinir_senha(token)


@app.route("/sessao_expirada")
def sessao_expirada():

    return render_template('email/sessao_expirada.html')




#          ROTAS REDEFINICAO SENHA

# ----------------------------------------------------------------------------------------

   




# ROTA DE LOGIN
@app.route("/login", methods=["POST", "GET"])
def logar():
    return login.Login()    


# ROTA ACESSO NEGADO
@app.route('/access_denied') 
@login_required
def acesso_negado():
    return render_template('negado.html')



@app.route('/perfil', methods=["POST", "GET"]) 
@login_required
def perfil():
    return alterar_cadastro.alterar_perfil()


@app.route('/beneficiario', methods=["POST", "GET"]) 
@login_required
def beneficiario():

    permissoes = checar_permissao() # id do dicionario é 5
    if 1 in  permissoes or 6 in permissoes:
        return consulta_senha_imagem.consultar_beneficiario()
    
    return redirecionar()


# ROTA LOGOUT
@app.route("/sair", methods=['GET'])
@login_required
def sair():
    try:
        remove_sessao_logout(g.id_user)
        logout_user()
        flash("Logout efetuado com sucesso!","success")
        return redirect(url_for("logar"))
    except Exception as e:
        logout_user()
        flash(f"{str(e)}","danger")
        return redirect(url_for("logar"))



@app.route("/", methods=["GET"])
def raiz():
    if current_user.is_authenticated:
            return redirect(url_for("index")) 
    else:
        return redirect(url_for("logar")) 


