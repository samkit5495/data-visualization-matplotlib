# --------------
import pandas as pd 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# Load the dataset and create column `year` which stores the year in which match was played
df = pd.read_csv(path)
df['year'] = df['date'].str[:4]

match_data = df.drop_duplicates(subset='match_code',keep='first')

# Plot the wins gained by teams across all seasons
win_data = match_data['winner'].value_counts()
print(win_data)
win_data.plot(kind='bar', title='Total wins accross all seasons')
plt.show()

# Plot Number of matches played by each team through all seasons
matches_played = pd.melt(match_data, id_vars=['match_code','years'],value_vars=['team1','team2'])
print(matches_played.head())
matches_played = matches_played['value'].value_counts()
matches_played.plot(kind='bar',title='Total matches played across all seasons')
plt.show()

# Top bowlers through all seasons
df['wicket_kind'].value_counts()
wicket_data = df[df['wicket_kind']!='']
bowlers_wickets_data = wicket_data.groupby(['bowler'])['wicket_kind'].count()
bowlers_wickets_data.head()
bowlers_wickets_data.sort_values(ascending=False, inplace=True)
bowlers_wickets_data[:10].plot(kind='barh')
plt.show()

# How did the different pitches behave? What was the average score for each stadium?
score_venue = df.groupby(['match_code','inning','venue'],as_index=False)['total'].sum()
score_venue.head()
avg_score_venue = df.groupby(['venue'])['total'].mean().sort_values(ascending=False)
avg_score_venue.head()
avg_score_venue[:10].plot(kind='barh')
plt.show()

# Types of Dismissal and how often they occur
dismissal_types = df.groupby('wicket_kind')['match_code'].count()
dismissal_types
dismissal_types.plot.pie()
plt.show()

# Plot no. of boundaries across IPL seasons
boundaries = df[df['runs']>=4]
boundaries_by_season =  boundaries.groupby('year')['runs'].count()
boundaries_by_season
boundaries_by_season.plot.line(title='no. of boundaries across IPL seasons')
plt.show()

# Average statistics across all seasons
num_of_matches = df.groupby('year')['match_code'].nunique()
num_of_matches
num_of_matches.plot.bar(title='Matches per season')
plt.show()

runs_per_match = df.groupby(['year','match_code'],as_index=False)['runs'].sum()
runs_per_match.head()
avg_runs = runs_per_match.groupby(['year'])['runs'].mean()
avg_runs
avg_runs.plot.bar(title='average runs scored per season')
plt.show()



