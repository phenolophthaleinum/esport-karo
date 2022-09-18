import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("esport.csv")
watching = data.iloc[:, 29:35]
watching_names = [x.split("*")[-1].translate(str.maketrans({"[": "", "]": ""})) for x in list(watching.columns)]
watching.columns = watching_names
v = watching.iloc[:, 0].unique()[:-1]
watching = watching.apply(lambda x: x.fillna(np.random.choice(v)))
watching_counts = watching.apply(pd.Series.value_counts)
watching_counts = watching_counts.rename_axis("answer").reset_index()
watching_counts = watching_counts.melt('answer', var_name="reason", value_name="value").reset_index(drop=True)

fig = px.bar(watching_counts, x="reason", y="value", color="answer",
             title="Oglądam wydarzenia e-sportowe ponieważ: ",
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