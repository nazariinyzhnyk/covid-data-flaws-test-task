from typing import List

import pandas as pd


def merge_single_country_files(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    final_df = pd.DataFrame()
    for i, df in enumerate(dfs):
        if i == 0:
            final_df = df
        else:
            final_df = final_df.append(df, ignore_index=True)
    final_df = final_df.sort_values("date")
    final_df = final_df.reset_index(drop=True)

    assert len(pd.unique(final_df["date"])) == len(final_df), \
        "there are duplicate dates! please analyse data more precisely!"

    assert all(pd.to_datetime(final_df["date"]).diff().loc[1:].dt.days) == 1, \
        "some day(s) are missing from sequence. please analyse data more precisely!"

    return final_df

