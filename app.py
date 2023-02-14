import dash
from dash import Input, Output, State, html, dcc

app = dash.Dash(__name__)

images = ['/static/images/verde.png',
          '/static/images/vermelho.png',
          '/static/images/CyberSVG.svg']


#============

app.layout = html.Div([
    html.H1("Tela de Escolha"),
    html.Div([
        html.Img(id="image", src=images[0]),
        dcc.RadioItems(
            options=[
                {"label": "Gostei", "value": "like"},
                {"label": "Não gostei", "value": "dislike"},
            ],
            value="like",
            id="choice-input"
        ),
    ]),
    html.Button("Próximo", id="next-button"),
    html.Div(id="current-image", style={"display": "none"}),
])

@app.callback(
    Output("current-image", "children"),
    [Input("next-button", "n_clicks")],
    [State("current-image", "children")],
)
def update_current_image(n_clicks, current_image):
    if n_clicks is None:
        return 0
    return (current_image + 1) % len(images)

@app.callback(
    Output("image", "src"),
    [Input("current-image", "children")],
)
def update_image(current_image):
    return images[current_image]

@app.callback(
    Output("choice-input", "value"),
    [Input("next-button", "n_clicks")],
    [State("choice-input", "value")],
)
def update_choice(n_clicks, current_choice):
    if n_clicks is None:
        return current_choice
    return "like" if current_choice == "dislike" else "dislike"

#============
server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)