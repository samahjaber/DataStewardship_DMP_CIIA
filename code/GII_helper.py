import pandas as pd
import re


def load_gii_year_df(year):
    df = pd.read_csv("./data/GII/Analysis_" + str(year) + ".CSV")

    df.rename(columns={" ": "Indicator", " .1": "Indicator Name"}, inplace=True)

    # Second entry for each country is the score (Header with .1)
    df.rename(columns=lambda x: re.sub(".1", "_score", x), inplace=True)

    # (Header with .2) is possibly change
    df.drop(df.filter(regex=".*\.2").columns, axis=1, inplace=True)
    # (Header with .3) is Strength/Weakness for ?
    df.drop(df.filter(regex=".*\.3").columns, axis=1, inplace=True)
    # (Header with .4) is Strength/Weakness for ?
    df.drop(df.filter(regex=".*\.4").columns, axis=1, inplace=True)

    # Delete unused columns
    df.drop(columns=["Value", "Income Group(Strength/Weakness)", "Strength / Weakness"], inplace=True)
    df.drop(df.filter(regex="Unnamed: .*").columns, axis=1, inplace=True)

    # Merge Indicator columns

    df.loc[df["Indicator Name"] == ' ', 'Indicator Name'] = df["Indicator"]
    df["Indicator"] = df["Indicator Name"]

    # df["Indicator"] = df["Indicator"] + " " + df["Indicator Name"]
    df.drop(columns=["Indicator Name", "Rank Indicators"], inplace=True)

    # Delete unused rows
    df.dropna(axis=0, how="all", inplace=True)

    df.set_index("Indicator", inplace=True, drop=True)

    df_t = df.transpose()

    # Rename old Index column to country
    df_t.reset_index(inplace=True)
    df_t.rename(columns={"index": "Country"}, inplace=True)

    df_t["Year"] = year

    # Keep only Score rows and not the rank rows
    df_t = df_t[df_t["Country"].str.match(".*_score") == True]

    # Somehow needed to remove invalid old index name shown over Country column
    df_t.columns.rename("", inplace = True)

    # Rename score rows
    df_t["Country"] = df_t["Country"].replace(to_replace="_score", value="", regex=True)

    df_t.set_index(["Year", "Country"], inplace=True, drop=True)

    return df_t

load_gii_year_df(2016)


#%%
