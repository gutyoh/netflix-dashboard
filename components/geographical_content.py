import pandas as pd
import plotly.express as px
from dash import dcc, html

df = pd.read_csv('netflix_titles.csv')

# Filter out entries without country information and if there are multiple production countries,
# consider the first one as the production country
df['country'] = df['country'].str.split(',').apply(lambda x: x[0].strip() if isinstance(x, list) else None)

# Extract the year from the date_added column
df['year_added'] = pd.to_datetime(df['date_added']).dt.year
df = df.dropna(subset=['country', 'year_added'])

# Compute the count of content produced by each country for each year
df_counts = df.groupby(['country', 'year_added']).size().reset_index(name='count')

# Sort the DataFrame by 'year_added' to ensure the animation frames are in ascending order
df_counts = df_counts.sort_values('year_added')

# Create the choropleth map with a slider for the year
fig1 = px.choropleth(df_counts,
                     locations='country',
                     locationmode='country names',
                     color='count',
                     hover_name='country',
                     animation_frame='year_added',
                     projection='natural earth',
                     title='Content produced by countries over the years',
                     color_continuous_scale='YlGnBu',
                     range_color=[0, df_counts['count'].max()])
fig1.update_layout(width=1280, height=720, title_x=0.5)

# Compute the count of content produced for each year by type and fill zeros for missing type-year pairs
df_year_counts = df.groupby(['year_added', 'type']).size().reset_index(name='count')

# Create the line chart using plotly express
fig2 = px.line(df_year_counts, x='year_added', y='count', color='type',
               title='Content distribution by type over the years',
               markers=True, color_discrete_map={'Movie': 'dodgerblue', 'TV Show': 'darkblue'})
fig2.update_traces(marker=dict(size=12))
fig2.update_layout(width=1280, height=720, title_x=0.5)

layout = html.Div([
    dcc.Graph(figure=fig1),
    html.Hr(),
    dcc.Graph(figure=fig2)
])