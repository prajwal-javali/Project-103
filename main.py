import pandas as pd
import plotly.express as px

df = pd.read_csv('data2.csv')
fig = px.scatter(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")
fig.show()
