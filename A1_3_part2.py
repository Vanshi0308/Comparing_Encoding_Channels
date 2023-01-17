import pandas as pd
import plotly.express as px

df = pd.read_csv('gapminder.csv')

fig_1 = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", title="Correlation between wealth and health by country population", labels={"gdpPercap": "GDP per capita", "lifeExp": "Life Expectancy", "pop": "Population"})
fig_1.show()

fig_2 = px.scatter(df, x="gdpPercap", y="lifeExp", color="pop", title="Correlation between wealth and health by country population", labels={"gdpPercap": "GDP per capita", "lifeExp": "Life Expectancy", "pop": "Population"})
fig_2.show()

fig_3 = px.scatter(df, x= "gdpPercap", y="lifeExp", color="pop", color_continuous_scale=["rgb(200,200,200)", "black"], title="Correlation between wealth and health by country population", labels={"gdpPercap": "GDP per capita", "lifeExp": "Life Expectancy", "pop": "Population"})
fig_3.show()