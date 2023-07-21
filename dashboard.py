from adminui import *

app = AdminApp(use_fastapi=True)
app.app_title = "Fecomercio MT"
app.app_logo = "https://proton-resources-production.imgix.net/98b270aed2d9069d9cbb0bdfc1d4dde8d32622fa1dbe4d017d01b40acae1bf66.png?auto=compress"
app.copyright_text = 'Fecomério - MT'
app.app_styles = {'nav_theme': 'dark', 'layout': 'sidemenu'}


chart_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chart_data = [1.5, 2.3, 4.3, 2.2, 5.1, 6.5, 2.3, 2.3, 2.2, 1.1]
chart_data2 = [6.5, 2.3, 2.3, 2.2, 1.1, 1.5, 2.3, 4.3, 2.2, 5.1]


app.set_menu(
    [
        MenuItem('Dashboard', '/', icon="dashboard"),
        MenuItem('Usuários', '/usuarios', icon="user", children=[
            MenuItem('Cadastrar', '/usuario/novo', icon="plus"),
            MenuItem('Buscar', '/usuario/buscar', icon="search"),
            MenuItem('Métricas', '/usuario/metricas', icon="setting")
        ]),
        MenuItem('Empresas', '/empresas', icon="home", children=[
            MenuItem('Cadastrar', '/cadastrar-empresa', icon='plus'),
            MenuItem('Buscar', '/buscar-empresa', icon="search"),
            MenuItem('Métricas', '/metricas-empresa', icon="setting")
        ]),
        MenuItem('About', '/about', icon="info-circle")
    ]
)

@app.page('/', 'Dashboard')
def home_page():
    return [
        #indicadores
        #Graficos   

        Card(content=[
            Row([
                Column([
                    Header(text = 'Cadastro de usuários'),
                    BarChart({'Titular': chart_data, 'Dependente': chart_data2}, chart_labels)         
                ])
            ])
        ]),
 
        Card(content=[
            Row([
                Column([
                    Header(text = 'Cadastro de empresas'),
                    LineChart(chart_data, chart_labels, show_area=True)
                
                ])
            ])
        ]),
 
    ]

app.set_as_shared_app()
import usuarios



fastapi_app = app.prepare()
