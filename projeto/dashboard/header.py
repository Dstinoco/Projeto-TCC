import dash
import dash_bootstrap_components as dbc
from dash import html



cabecalho = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            [
                                html.Img(
                                    src="/static/img/back-return-svgrepo-com.svg",
                                    style={"height": "50px", "width": "auto"},
                                    alt="Logo"
                                ),
                                
                            ],
                            href="/dashboard",  # Altere para a URL desejada
                            className="d-flex align-items-center"
                        ),
                        width="auto"
                    ),
                    dbc.Col(
                      [html.H1("Portal Dados",
                                style={
                "font-style": "normal",
                "font-weight": "700",
                "font-size": "36px",
                "text-align": "center",
                "color": "rgb(79, 79, 79)",
                "margin": "10px auto"
            })]
                    ),
                ],
                align="center",
                className="w-100"
            )
        ],
        fluid=True
    ),
    color="light",
    dark=False,
    className="shadow-sm  rounded-3 mp-5", style={"height":"15vh"}
)



