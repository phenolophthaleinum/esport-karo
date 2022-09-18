import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
sex = data.iloc[:, 38]
sex = sex.to_frame()
sex.columns = ["value"]
sex_counts = sex.apply(pd.Series.value_counts)
sex_counts = sex_counts.rename_axis("answer").reset_index()
temp = pd.DataFrame(columns=sex_counts.columns, data=[["Inne", 0]])
sex_counts = pd.concat([sex_counts, temp], axis=0)

fig = px.pie(sex_counts, values="value", names="answer",
             title="Płeć",
             color_discrete_sequence=px.colors.qualitative.G10,
             template='seaborn',
             )
fig.update_layout(
    title_y=1, font_family="Roboto", yaxis_title=None, xaxis_title=None, legend_title_text=None)
fig.update_traces(textposition='inside')
fig.update_traces(marker=dict(line=dict(color='#ffffff', width=2)))
fig.show()
