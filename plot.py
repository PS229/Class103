import pandas as pd
import plotly.express as px

data = [1,2,3,4,5]
#df = pd.DataFrame(data)
#print(df)
df = pd.read_csv("line_chart.csv")
fig = px.line(df,x = "Year", y = "Per capita income", title = "Per capita income", color = "Country")
fig.show()