import pandas as pd
import plotly.express as px
from dash import dcc, html

df = pd.read_csv('netflix_titles.csv')

# Split the listed_in column and explode to handle multiple genres
df['listed_in'] = df['listed_in'].str.split(', ')
df = df.explode('listed_in')

# Compute the count of each combination of type and genre
df_counts = df.groupby(['type', 'listed_in']).size().reset_index(name='count')

fig = px.treemap(df_counts, path=['type', 'listed_in'], values='count', color='count',
                 color_continuous_scale='Ice', title='Content by type and genre')

fig.update_layout(width=1280, height=960, title_x=0.5)
fig.update_traces(textinfo='label+percent entry', textfont_size=14)

layout = html.Div([
    dcc.Graph(figure=fig),
])