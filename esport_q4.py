import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
follow = data.iloc[:, 28]
follow = follow.to_frame()
follow.columns = ["value"]
follow_counts = follow.apply(pd.Series.value_counts)
follow_counts = follow_counts.rename_axis("answer").reset_index()

fig = px.pie(follow_counts, values="value", names="answer",
             title="Czy śledzisz rozgrywki E-sportowe w swojej ulubionej grze?",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn'
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
