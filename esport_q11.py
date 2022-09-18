import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
work = data.iloc[:, 41]
work = work.to_frame()
work.columns = ["value"]
work_counts = work.apply(pd.Series.value_counts)
work_counts = work_counts.rename_axis("answer").reset_index()
temp = pd.DataFrame(columns=work_counts.columns, data=[["Emeryt/ka", 0]])
work_counts = pd.concat([work_counts, temp], axis=0)

fig = px.pie(work_counts, values="value", names="answer",
             title="Sytuacja zawodowa",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn',
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(textposition='inside')
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
