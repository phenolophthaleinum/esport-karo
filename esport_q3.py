import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
statement = data.iloc[:, 16:28]
statement_names = [x.split(":")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(statement.columns)]
statement.columns = statement_names
v = statement.iloc[:, 0].unique()[:-1]
statement = statement.apply(lambda x: x.fillna(np.random.choice(v)))
statement_counts = statement.apply(pd.Series.value_counts)
statement_counts = statement_counts.rename_axis("answer").reset_index()
statement_counts = statement_counts.melt('answer', var_name="statement", value_name="value").reset_index(drop=True)
# print(statement)
# values_map = {
#     "Zdecydowanie się nie zgadzam": 1,
#     "Raczej się nie zgadzam": 2,
#     "Nie mam zdania": 3,
#     "Raczej się zgadzam": 4,
#     "Zdecydowanie się zgadzam": 5,
# }
# mapped_statement = statement.apply(lambda x: pd.Series.map(x, values_map))
# # mapped_statement = mapped_statement.rename_axis("answer").reset_index()
# print(mapped_statement.describe().T)

fig = px.bar(statement_counts, x="statement", y="value", color="answer",
             title="Proszę stwierdzić na ile zgadzasz się ze stwierdzeniem: Bardzo często spędzam czas wolny:",
            color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn')
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.show()