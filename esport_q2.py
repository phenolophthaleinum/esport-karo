import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv("esport.csv")
devices = data.iloc[:, 11:16]
devices_names = [x.split("*")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(devices.columns)]
devices.columns = devices_names
devices_counts = devices.apply(pd.Series.value_counts)
devices_counts = devices_counts.rename_axis("answer").reset_index()
devices_counts = devices_counts.melt('answer', var_name="device", value_name="value").reset_index(drop=True)

fig = px.histogram(devices_counts, x="device", y="value", color="answer",
                   barnorm="fraction",
                   text_auto='.2%',
                   title="Jak często używasz podanych urządzeń do oglądania stremingu gier komputerowych lub wydarzeń e-sportowych?",
                   color_discrete_sequence=px.colors.qualitative.G10,
                   template='seaborn')
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.layout.yaxis.tickformat = ".2%"
fig.show()
