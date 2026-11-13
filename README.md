\# Daily Metrics Pipeline



ETL pipeline that processes retail sales transactions and generates daily product-level metrics.



\## Features

\- Handles sales and reversal events

\- Calculates daily units sold, revenue, and active transactions per product

\- Schema and business-rule validation with reject/quarantine path

\- Idempotent reruns (processed events tracked, no duplicates on rerun)

\- Reconciliation report (source vs target revenue check)

\- Run metrics logging (run\_id, input/output/rejected counts, duration)

\- Automated tests with pytest (9 tests: happy path, reversal, empty, malformed, nulls, duplicates, late events, schema change, invalid reference key)

\- CI workflow with GitHub Actions

\- Performance benchmark (100k rows)



\## Setup

```bash

pip install -r requirements.txt

```



\## Run

```bash

python src/run\_pipeline.py

```



\## Test

```bash

python -m pytest tests/ -v

```



\## Benchmark (100k rows)

```bash

python src/benchmark.py

```



\## Output

\- Daily metrics: `data/daily\_metrics\_output.csv`

\- Rejected records: `data/rejected\_records.csv`

\- Reconciliation report printed to console

\- Logs: run\_id, input/output/rejected counts, duration



\## Architecture Diagram

