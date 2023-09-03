import pandas as pd

# Read csv from .zip file in data folder.
df_winemag = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Create two series grouped by country. First w/country value counts. Second w/ avg points rounded.
df_count = df_winemag.groupby('country').country.value_counts()
df_mean = df_winemag.groupby('country').points.mean().round(1)

# Combine two series into dataframe on country axis, and reset index.
df_summary = pd.concat([df_count, df_mean], axis=1).reset_index()

# Sort dataframe by descending number of reviews.
df_summary = df_summary.sort_values(by='count', ascending=False)

# Write summary of findings to new .csv file in data folder.
df_summary.to_csv('data/reviews-per-country.csv')


