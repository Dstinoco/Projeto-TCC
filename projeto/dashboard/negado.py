from dash import html
import dash_bootstrap_components as dbc

layout_negado = dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        # Flash message include (substitua com o conteúdo desejado ou deixe vazio)
                        # Exemplo: html.Div("Mensagem Flash", id="flash-message"),
                        
                        # Imagem
                        html.Img(src="../static/img/close-circle-svgrepo-com.svg", alt=""),
                        
                        # Texto de acesso negado
                        html.H2("Acesso negado", style={"color": "#f00"}),
                    ],
                    className="text-center p-5"
                ),
                className="shadow-2-strong",
                style={"border-radius": "1rem"},
            ),
            className="d-flex justify-content-center align-items-center h-100"
        )
    ),
    className="py-5 h-100"
)