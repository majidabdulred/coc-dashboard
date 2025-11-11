import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Script Dashboard"
)
import pandas as pd


df_wars = pd.read_csv("files/29GPY0J2V-war-statistics.csv")

column_names = {"Attacks":"⚔️","Attack: Average Stars":"Attack Avg. ⭐","Attack: 3 Stars Count":"🗡️⭐⭐⭐","Attack: 2 Stars Count":"🗡️⭐⭐","Attack: 1 Star Count":"🗡️⭐","Defense: count":"🛡️"
               ,"Defense: Average Stars":"Defense Avg. ⭐","Defense: 3 Stars Count":"🎯⭐⭐⭐","Defense: 2 Stars Count":"🎯⭐⭐","Defense: 1 Star Count":"🎯⭐"}

def count_attacks(row):
    total_attacks = row["Attack: 3 Stars Count"] + row["Attack: 2 Stars Count"] + row["Attack: 1 Star Count"]+ row["Attack: 0 Star Count"]+row["Attack: Miss attacks"]
    return f"{row['Attack: count']}/{total_attacks}"

df_wars["Attacks"] = df_wars.apply(count_attacks,axis=1)

df_wars = df_wars.rename(columns=column_names)



df_wars = df_wars[["Name"]+list(column_names.values())]

df_wars =df_wars.set_index("Name")


st.dataframe(data=df_wars,height="stretch")