from typing import List

import pandas as pd


def min_max_scaling(df: pd.DataFrame, scale_features: List[str]) -> pd.DataFrame:
    for scale_feature in scale_features:
        feature_min = min(df[scale_feature])
        feature_max = max(df[scale_feature])
        df[scale_feature] = (df[scale_feature] - feature_min) / (feature_max - feature_min)
    return df
