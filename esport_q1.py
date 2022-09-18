import pandas as pd
import numpy as np
import plotly.express as px


def sanitise_answers(ans):
    l = ans.split(";")
    if not (("Nigdy o niej nie słyszałem/am" in l or "Słyszałem/am o nich, ale nie używam" in l) and len(l) > 1):
        return l


data = pd.read_csv("esport.csv")

platforms_names = ["YouTube Gaming",
"Twitch",
"InstaGib TV",
"Mixer",
"Hitbox",
"Azubu",
"BigoLive",
"Gosu Gamers",
"Dlive",
"DiscoMelee"]
platforms = data.iloc[:, 1:11]
platforms.columns = platforms_names
platforms_counts = platforms.apply(pd.Series.value_counts)
platforms_counts = platforms_counts.rename_axis("answer").reset_index()
platforms_counts = platforms_counts.melt('answer', var_name="platform", value_name="value").reset_index(drop=True)
# platforms_counts["answer"] = platforms_counts["answer"].apply(lambda x: x.split(";"))
platforms_counts["answer"] = platforms_counts["answer"].apply(lambda x: sanitise_answers(x))
# TODO: remove None rows
platforms_counts = platforms_counts.replace(to_replace='None', value=np.nan).dropna()
print(platforms_counts)
platforms_counts = platforms_counts.explode('answer')
platforms_counts = platforms_counts.groupby(by=["answer", "platform"], as_index=False).sum()
print(platforms_counts.describe())

# fig = px.bar(platforms_counts, x=platforms_names, y="answer",
#              title="Które z podanych platform streamingowych znasz, używasz do oglądania streamingu gier komputerowych lub do oglądania wydarzeń e-sportowych?",
#              )
fig = px.bar(platforms_counts, x="platform", y="value", color="answer",
             title="Które z podanych platform streamingowych znasz, używasz do oglądania streamingu gier komputerowych lub do oglądania wydarzeń e-sportowych?",
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

