# app/utils.py

import pandas as pd
import plotly.express as px

def load_data():
    benin = pd.read_csv("./data/cleaned/benin_clean.csv")
    sierra = pd.read_csv("./data/cleaned/sierraleone_clean.csv")
    togo = pd.read_csv("./data/cleaned/togo_clean.csv")
    
    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"
    
    return pd.concat([benin, sierra, togo], ignore_index=True)

def plot_metric_boxplot(df, metric):
    fig = px.box(df, x="Country", y=metric, color="Country", title=f"{metric} Comparison")
    return fig

def summary_table(df):
    return df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)
