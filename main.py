# Import Pandas and Plotly
import pandas as pd
import plotly.express as px

# API Endpoint
url = 'http://api.open-notify.org/iss-now.json'

# Pass url into a dataframe
df = pd.read_json(url)

df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['latitude', 'iss_position']

df.reset_index(inplace=True)

df = df.drop(['index', 'message'], axis=1)

# Show map of earth
fig = px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()

