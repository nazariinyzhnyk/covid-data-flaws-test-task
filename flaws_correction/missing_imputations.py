import pandas as pd


def impute_with_value(x, value=0):
    return value if pd.isna(x) else x


def validate_cols_in_df(df, needed_cols):
    for needed_col in needed_cols:
        if needed_col not in df.columns:
            raise KeyError(f"{needed_col} not found in a target dataframe")


def active_cases_calculation(df: pd.DataFrame) -> pd.DataFrame:
    validate_cols_in_df(df, ["Confirmed", "Deaths", "Recovered"])
    df["Active"] = df["Confirmed"] - df["Deaths"] - df["Recovered"]
    return df


def incident_rate_calculation(df: pd.DataFrame, population_mln: int) -> pd.DataFrame:
    validate_cols_in_df(df, ["Confirmed"])
    df["Incident_Rate"] = df["Confirmed"] / (population_mln * 10)
    return df


def case_fatality_ratio_calculation(df: pd.DataFrame) -> pd.DataFrame:
    validate_cols_in_df(df, ["Confirmed", "Deaths"])
    df["Case_Fatality_Ratio"] = df["Deaths"] / df["Confirmed"] * 100
    return df
