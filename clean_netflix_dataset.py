import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Fill missing values
df['director'].fillna('No director', inplace=True)
df['cast'].fillna('No cast', inplace=True)
df['country'].fillna('No country', inplace=True)

# Drop missing and duplicate values
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Strip whitespaces from the `date_added` col and convert values to `datetime`
df['date_added'] = pd.to_datetime(df['date_added'].str.strip())

# Save the cleaned dataset
df.to_csv('netflix_titles.csv', index=False)