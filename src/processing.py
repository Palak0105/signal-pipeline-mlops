import numpy as np


def compute_signals(df, window):
    """
    Compute rolling mean and binary trading signal.
    """

    # Rolling mean
    df["rolling_mean"] = (
        df["close"]
        .rolling(window=window)
        .mean()
    )

    # Generate signal
    df["signal"] = np.where(
        df["close"] > df["rolling_mean"],
        1,
        0
    )

    # Handle NaN rolling mean rows
    df.loc[df["rolling_mean"].isna(), "signal"] = 0

    return df