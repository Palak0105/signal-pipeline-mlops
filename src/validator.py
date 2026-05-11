import pandas as pd


REQUIRED_COLUMNS = ["close"]


def load_and_validate_dataset(input_path: str):
    """
    Load and validate dataset.
    """

    try:
        df = pd.read_csv(input_path)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    except pd.errors.EmptyDataError:
        raise ValueError(
            "Input CSV is empty"
        )

    except pd.errors.ParserError:
        raise ValueError(
            "Invalid CSV format"
        )

    # Validate empty dataframe
    if df.empty:
        raise ValueError(
            "Dataset contains no rows"
        )

    # Validate required columns
    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return df