# Signal Pipeline MLOps Assessment

## Overview
This project implements a minimal production-style MLOps batch pipeline for generating trading signals using rolling averages on OHLCV data.

The pipeline demonstrates:
- Reproducibility
- Observability
- Structured logging
- Metrics generation
- Dockerized execution

---

## Features

- YAML-based configuration
- Deterministic execution using seeds
- Dataset validation
- Rolling mean computation
- Binary signal generation
- Machine-readable metrics
- Structured logs
- Docker support

---

## Project Structure

```bash
project/
│
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── README.md
│
├── src/
│   ├── config.py
│   ├── validator.py
│   ├── processing.py
│   ├── metrics.py
│   └── logger.py
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Local Execution

```bash
python run.py \
--input data.csv \
--config config.yaml \
--output metrics.json \
--log-file run.log
```

---

## Docker Execution

### Build image

```bash
docker build -t signal-pipeline .
```

### Run container

```bash
docker run --rm \
-v $(pwd):/app \
signal-pipeline \
python run.py \
--input data.csv \
--config config.yaml \
--output metrics.json \
--log-file run.log
```

---

## Metrics Output

Example:

```json
{
    "rows_processed": 10000,
    "signal_rate": 0.51,
    "latency_ms": 19.54,
    "version": "v1"
}
```

---

## Logging

The pipeline generates structured logs in `run.log`.

---

## Technologies Used

- Python
- Pandas
- NumPy
- PyYAML
- Docker

---

## Author

Palak Pallavi