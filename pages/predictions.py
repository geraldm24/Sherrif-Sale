# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
          dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Charges Due'), 
        dcc.Slider(
            id='other_charges_due', 
            min=test[:,0], 
            max=test[:,0], 
            step=100, 
            value=-100, 
            marks={n: str(n) for n in range(-100,22000,1000)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Penalty'), 
          dcc.Slider(
            id='penalty_due', 
            min=test[:,0], 
            max=test[:,0], 
            step=, 
            value=-47, 
            marks={n: str(n) for n in range(-47,170000,10000)}, 
            className='mb-5', 
        ), 
          dcc.Markdown('#### Interest Due'), 
          dcc.Slider(
            id=' interest_due', 
            min=test[:,0], 
            max=test[:,0],  
            step=4000, 
            value=4000, 
            marks={n: str(n) for n in range(4000,60000,10000)}, 
            className='mb-5', 
    ],
    md=6,
)

column2 = dbc.Col(
    [

    ]
)
        import pandas as pd
@app.callback(
    Output('prediction-content', 'children'),
    [Input('other_charges_due', 'value'), Input('penalty_due', 'value')], Input('interest_due', 'value')]
)
def predict(other_charges_due, penalty_due,interest_due):
    df_encoded_d = pd.DataFrame(
        columns=['other_charges_due', 'penalty_due','interest_due'], 
        data=[[other_charges_due, penalty_due,interest_due]]
    )
    y_pred = pipeline.predict(df_encoded_d)[0]
    return f'{y_pred:.0f} chance of Sherrif-Sale Property'
layout = dbc.Row([column1, column2])
