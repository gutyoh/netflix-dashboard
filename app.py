from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from components import (
    geographical_content,
    content_classification
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dcc.Store(id='store'),
        html.H1('Netflix Movies and TV Shows Dashboard'),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label='Geographical content distribution', tab_id='tab1'),
                dbc.Tab(label='Content classification', tab_id='tab2'),
            ],
            id='tabs',
            active_tab='tab1',
        ),
        html.Div(id='tab-content', className='p-4'),
    ]
)


# This callback function switches between tabs in a dashboard based on user selection.
# It updates the 'tab-content' component with the layout of the newly selected tab.
@app.callback(Output('tab-content', 'children'), [Input('tabs', 'active_tab')])
def switch_tab(at):
    if at == 'tab1':
        return geographical_content.layout
    elif at == 'tab2':
        return content_classification.layout


if __name__ == '__main__':
    app.run(debug=True)