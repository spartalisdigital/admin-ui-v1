from adminui import *

app = AdminApp.shared_app()

@app.page('/usuario/buscar', 'Buscar Usuários')
def buscar_usuarios():
    return [
        #Titulo
        Header(text='Usuários cadastrados')

        #Tabela
    ]

@app.page('/usuario/novo', 'Novo Usuário')
def novo_usuario():
    return [
        #Titulo
        Header(text='Cadastrar novo usuário')

        #formulario
    ]

@app.page('/usuario/editar', 'Editar Usuário')
def editar_usuario():
    return [
        #Titulo
        Header(text='Editar usuário')

        #formulario
    ]

@app.page('/usuario/metricas', 'Métricas')
def metricas_usuarios():
    return [
        #Titulo
        Header(text='Métricas dos usuário')

        #grafico
    ]