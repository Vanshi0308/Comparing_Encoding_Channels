import pandas as pd
import plotly.express as px

df = pd.read_csv('gapminder.csv')

fig_1 = px.scatter(df, x="year", y="lifeExp", symbol="continent", title="Evolution of life expectancy over the years by continent", labels={"year": "Year", "lifeExp": "Life Expectancy", "continent": "Continent"})
fig_1.show()

fig_2 = px.scatter(df, x="year", y="lifeExp", color="continent", title="Evolution of life expectancy over the years by continent", labels={"year": "Year", "lifeExp": "Life Expectancy", "continent": "Continent"})
fig_2.show()

fig_3 = px.scatter(df, x="year", y="lifeExp", color="continent", color_discrete_sequence=["rgb(0,0,0)", "rgb(50,50,50)", "rgb(100,100,100)", "rgb(150,150,150)", "rgb(200,200,200)"], title="Evolution of life expectancy over the years by continent", labels={"year": "Year", "lifeExp": "Life Expectancy", "continent": "Continent"})
fig_3.show()