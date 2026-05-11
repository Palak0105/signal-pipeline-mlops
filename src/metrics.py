import json


def generate_metrics(df, latency_ms, version):
    """
    Generate machine-readable metrics.
    """

    metrics = {
        "rows_processed": int(len(df)),
        "signal_rate": float(df["signal"].mean()),
        "latency_ms": round(latency_ms, 2),
        "version": version
    }

    return metrics


def save_metrics(metrics, output_path):
    """
    Save metrics to JSON file.
    """

    with open(output_path, "w") as file:
        json.dump(metrics, file, indent=4)