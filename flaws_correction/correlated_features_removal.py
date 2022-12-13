import numpy as np

import pandas as pd


def drop_correlated_features(
        df: pd.DataFrame,
        threshold: float = 0.999
) -> pd.DataFrame:
    cor_matrix = df.corr().abs()
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]
    df = df.drop(to_drop, axis=1)
    return df

