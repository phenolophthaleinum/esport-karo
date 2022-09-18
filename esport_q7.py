import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
social2 = data.iloc[:, 36]
social2 = social2.to_frame()
social2.columns = ["value"]
social2_counts = social2.apply(pd.Series.value_counts)
social2_counts = social2_counts.rename_axis("answer").reset_index()

fig = px.pie(social2_counts, values="value", names="answer",
             title="Czy udzielasz się na portalach internetowych lub w grupach o tematyce e-sportowej (np. Reddit)?",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn'
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
