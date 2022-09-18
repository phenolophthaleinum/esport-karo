import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
age = data.iloc[:, 39]
age = age.to_frame()
age.columns = ["value"]
age_counts = age.apply(pd.Series.value_counts)
age_counts = age_counts.rename_axis("answer").reset_index()
temp = pd.DataFrame(columns=age_counts.columns, data=[["40 - 44", 0], ["45 - 49", 0], ["50 - 54", 0], ["55 - 59", 0], ["60 i więcej", 0]])
age_counts = pd.concat([age_counts, temp], axis=0)

fig = px.pie(age_counts, values="value", names="answer",
             title="Przedział wiekowy",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn',
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(textposition='inside')
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
