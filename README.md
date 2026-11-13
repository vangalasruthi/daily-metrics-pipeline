\# Daily Metrics Pipeline



ETL pipeline that processes retail sales transactions and generates daily product-level metrics.



\## Features

\- Handles sales and reversal events

\- Calculates daily units sold, revenue, and active transactions per product

\- Schema and business-rule validation with reject/quarantine path

\- Reconciliation report (source vs target revenue check)

\- Automated tests with pytest

\- CI workflow with GitHub Actions



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



\## Output

\- Daily metrics: `data/daily\_metrics\_output.csv`

\- Rejected records: `data/rejected\_records.csv`

\- Reconciliation report printed to console



\## Architecture

1\. Ingest CSV transactions

2\. Validate schema + business rules (rejects quarantined)

3\. Transform: aggregate daily metrics per product (sales - reversals)

4\. Publish metrics CSV

5\. Reconcile source vs target revenue

