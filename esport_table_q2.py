import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("esport.csv")
devices = data.iloc[:, 11:16]
devices_names = [x.split("*")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(devices.columns)]
devices.columns = devices_names
values_map = {
    "Nigdy": 1,
    "Rzadko": 2,
    "Czasami": 3,
    "Często": 4,
    "Bardzo często": 5,
}
mapped_devices = devices.apply(lambda x: pd.Series.map(x, values_map))
# mapped_statement = mapped_statement.rename_axis("answer").reset_index()
mapped_devices = mapped_devices.describe().T
df = mapped_devices.rename_axis("Odpowiedź").reset_index()
df = df.rename(columns={'mean': "Średnia", 'std': "Odchylenie standardowe"})
df = df.iloc[:, [0, 2, 3]]
df = df.round(3)
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns)),
    cells=dict(values=[df[x] for x in df.columns],))
])
fig.update_layout(font_family="Calibri")
fig.show()