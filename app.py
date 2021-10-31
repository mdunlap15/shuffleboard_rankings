# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, Input, Output, callback
from dash import dash_table as dt
import pandas as pd
import dash_bootstrap_components as dbc
from dash_table import DataTable, FormatTemplate


df = pd.read_csv('Rankings_Table.csv')

app = Dash(__name__)

percentage = FormatTemplate.percentage(1)

app.layout = dbc.Container([
    dbc.Label('Brooklyn Shuffleboard Rankings', style={"font-weight": "bold"}),
    dt.DataTable(
        data=df.to_dict('records'),
        columns=[
            dict(id='Ranking', name='Ranking'),
            dict(id='Player', name='Player'),
            dict(id='Elo', name='Elo Rating'),
            dict(id='Wins', name='Wins'),
            dict(id='Losses', name='Losses'),
            dict(id='Win%', name='Win %', type='numeric', format=percentage)],
        style_cell={'textAlign':'center'}
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)
