import yaml


REQUIRED_CONFIG_KEYS = ["seed", "window", "version"]


def load_config(config_path: str):
    """
    Load and validate YAML configuration.
    """

    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Config file not found: {config_path}"
        )

    except yaml.YAMLError as e:
        raise ValueError(
            f"Invalid YAML format: {e}"
        )

    # Validate required keys
    for key in REQUIRED_CONFIG_KEYS:
        if key not in config:
            raise ValueError(
                f"Missing required config key: {key}"
            )

    # Validate window
    if not isinstance(config["window"], int) or config["window"] <= 0:
        raise ValueError(
            "Window must be a positive integer"
        )

    # Validate seed
    if not isinstance(config["seed"], int):
        raise ValueError(
            "Seed must be an integer"
        )

    return config