import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("esport.csv")
statement = data.iloc[:, 16:28]
statement_names = [x.split(":")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(statement.columns)]
statement.columns = statement_names
v = statement.iloc[:, 0].unique()[:-1]
statement = statement.apply(lambda x: x.fillna(np.random.choice(v)))
values_map = {
    "Zdecydowanie się nie zgadzam": 1,
    "Raczej się nie zgadzam": 2,
    "Nie mam zdania": 3,
    "Raczej się zgadzam": 4,
    "Zdecydowanie się zgadzam": 5,
}
mapped_statement = statement.apply(lambda x: pd.Series.map(x, values_map))
# mapped_statement = mapped_statement.rename_axis("answer").reset_index()
mapped_statement = mapped_statement.describe().T
df = mapped_statement.rename_axis("Odpowiedź").reset_index()
df = df.rename(columns={'mean': "Średnia", 'std': "Odchylenie standardowe"})
df = df.iloc[:, [0, 2, 3]]
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns)),
    cells=dict(values=[df[x] for x in df.columns],))
])
fig.update_layout(font_family="Roboto")
fig.show()