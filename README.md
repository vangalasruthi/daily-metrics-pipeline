\# Daily Metrics Pipeline



ETL pipeline that processes retail sales transactions and generates daily product-level metrics.



\## Features

\- Handles sales and reversal events

\- Calculates daily units sold, revenue, and active transactions per product

\- Schema and business-rule validation with reject/quarantine path

\- Idempotent reruns (processed events tracked, no duplicates on rerun)

\- Reconciliation report (source vs target revenue check)

\- Run metrics logging (run\_id, input/output/rejected counts, duration)

\- Automated tests with pytest (7 tests: happy path, reversal, empty, malformed, nulls, duplicates, late events)

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



\## Architecture

1\. Ingest CSV transactions

2\. Idempotent filter (skip already processed events)

3\. Validate schema + business rules (rejects quarantined)

4\. Transform: aggregate daily metrics per product (sales - reversals)

5\. Publish metrics CSV

6\. Reconcile source vs target revenue

7\. Mark processed events for future reruns



\## Data Dictionary

\- event\_id: unique event identifier (int)

\- product\_id: product identifier (str)

\- customer\_id: customer identifier (str)

\- event\_type: sale | reversal (str)

\- quantity: units sold (int)

\- amount: transaction amount (float)

\- event\_time: ISO-8601 timestamp (str)

\- run\_id: pipeline run identifier (str)



\## Design Trade-offs

\- Idempotency: file-based processed\_events.csv (simple, local; production would use DB/state store)

\- Late events: handled by date-based grouping (recompute affected date partitions)

\- Performance: 100k rows in 0.05s (vectorized pandas ops)



\## Known Limitations

\- File-based idempotency (not scalable for distributed systems)

\- No backfill/retry automation (manual rerun supported)

\- Single-node processing (no Spark/Dask)



\## Possible Next Steps

\- Move to Postgres/Spark for scale

\- Add backfill job scheduler

\- Add data quality dashboards

