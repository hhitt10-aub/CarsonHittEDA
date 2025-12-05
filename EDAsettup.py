import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def read_games(dataset: str = "games") -> pd.DataFrame:
    if dataset == "games":
        games : pd.core.frame.DataFrame = pd.read_pickle("export/games_cleaned_added_features.pkl")

    return games

def make_games_bar(df: pd.DataFrame, x_col: str, y_col: str):
    import seaborn as sns

    gamesBar = sns.barplot(data=df, x=x_col, y=y_col) #makes the plot and sets the x and y axis
    gamesBar.bar_label(gamesBar.containers[0], fontsize=10) #add the numbers at the top of each bar
    gamesBar.set(title="Each Category's Total Profit") #adds the title
    gamesBar.grid() #adds the grid to make it easier to read
    return gamesBar



