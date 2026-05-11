import argparse
import time
import numpy as np

from src.config import load_config
from src.validator import load_and_validate_dataset
from src.processing import compute_signals
from src.metrics import generate_metrics, save_metrics
from src.logger import setup_logger


def main():
    """
    Main pipeline execution.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to config YAML"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to metrics JSON"
    )

    parser.add_argument(
        "--log-file",
        required=True,
        help="Path to log file"
    )

    args = parser.parse_args()

    logger = setup_logger(args.log_file)

    start_time = time.perf_counter()

    try:
        logger.info("Loading configuration")

        config = load_config(args.config)

        logger.info("Configuration loaded successfully")

        # Set reproducibility seed
        np.random.seed(config["seed"])

        logger.info(
            f"Seed set to {config['seed']}"
        )

        logger.info("Loading dataset")

        df = load_and_validate_dataset(args.input)

        logger.info(
            f"Dataset loaded successfully with {len(df)} rows"
        )

        logger.info("Computing rolling mean and signals")

        df = compute_signals(
            df,
            config["window"]
        )

        end_time = time.perf_counter()

        latency_ms = (
            (end_time - start_time) * 1000
        )

        metrics = generate_metrics(
            df,
            latency_ms,
            config["version"]
        )

        save_metrics(
            metrics,
            args.output
        )

        logger.info(
            f"Metrics saved to {args.output}"
        )

        logger.info(
            f"Pipeline completed successfully in {latency_ms:.2f} ms"
        )

    except Exception as e:
        logger.exception(
            f"Pipeline failed: {e}"
        )
        raise


if __name__ == "__main__":
    main()