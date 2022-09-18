import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
place = data.iloc[:, 42]
place = place.to_frame()
place.columns = ["value"]
place_counts = place.apply(pd.Series.value_counts)
place_counts = place_counts.rename_axis("answer").reset_index()

fig = px.pie(place_counts, values="value", names="answer",
             title="Miejsce zamieszkania",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn',
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
