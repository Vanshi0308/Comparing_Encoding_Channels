import pandas as pd
import plotly.express as px

df = pd.read_csv('gapminder.csv')

fig = px.scatter_3d(df, x="gdpPercap", y="lifeExp", z="year", symbol="continent", color="country", size="pop", title="Free form", labels={"gdpPercap": "GDP per capita", "lifeExp": "Life Expectancy", "year": "Year", "continent": "Continent", "country": "Country", "pop": "Population"})
fig.show()