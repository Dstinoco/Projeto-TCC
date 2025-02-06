from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, DateField, TimeField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


from projeto.funcoes import get_grupo, get_usuario, get_funcionalidade, get_download_arquivo


class FormLogar(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    entrar = SubmitField("Entrar")
    redefinir = SubmitField("Solicitar Redefinicao")


class FormCriarUser(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirmar_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo("senha")])
    grupo = SelectField("Grupo", coerce=int, choices=get_grupo)
    status = BooleanField("Status")
    submit = SubmitField("Cadastrar")
    update = SubmitField("Alterar")
    vincular = SubmitField("Vincular Grupo")
    redefinir = SubmitField("Redefinir Senha")

class FormGrupo(FlaskForm):
    grupoID = IntegerField("grupoID")
    nome = StringField('Nome', validators=[DataRequired()])
    status = BooleanField("Status")
    submit = SubmitField("Cadastrar")
    update = SubmitField("Alterar")



class FormUsuarioGrupo(FlaskForm):
    usuario = SelectField("Usuário", coerce=int, choices=get_usuario, validators=[DataRequired()])
    grupo = SelectField("Grupo", coerce=int, choices=get_grupo, validators=[DataRequired()])
    submit = SubmitField("Vincular")


class FormLayoutArquivo(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    formato = StringField('Formato', validators=[DataRequired()])
    colunas = TextAreaField('Colunas', validators=[DataRequired()])
    grupo = SelectField("Grupo", coerce=int, choices=get_grupo)
    submit = SubmitField("Cadastrar")
    update = SubmitField("Alterar")
    vincular = SubmitField("Vincular Grupo")


class FormAlterarSenha(FlaskForm):
    password = PasswordField('Senha', validators=[DataRequired()])
    confirmar_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo("senha")])
    update = SubmitField("Alterar")


class FormFuncionalidade(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    grupo = grupo = SelectField("Grupo", coerce=int, choices=get_grupo)
    submit = SubmitField("Cadastrar")
    update = SubmitField("Alterar")
    vincular = SubmitField("Vincular Grupo")


class FormFuncionalidadeGrupo(FlaskForm):
    funcionalidade = SelectField("Funcionalidade", coerce=int, choices=get_funcionalidade, validators=[DataRequired()])
    grupo = grupo = SelectField("Grupo", coerce=int, choices=get_grupo, validators=[DataRequired()])
    submit = SubmitField("Vincular Funcionalidade")

class FormDownloadArquivo(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    query = TextAreaField('Query', validators=[DataRequired()])
    grupo = SelectField("Grupo", coerce=int, choices=get_grupo)
    select_download = SelectField("Planilha", coerce=int, choices=get_download_arquivo, validators=[DataRequired()])
    submit = SubmitField("Cadastrar")
    update = SubmitField("Alterar")
    download = SubmitField("Download")
    vincular = SubmitField("Vincular Grupo")

