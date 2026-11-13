\# Daily Metrics Pipeline



ETL pipeline that processes retail sales transactions and generates daily product-level metrics.



\## Features

\- Handles sales and reversal events

\- Calculates daily units sold, revenue, and active transactions per product

\- Supports incremental transaction processing

\- Automated tests with pytest



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

Daily metrics CSV generated at `data/daily\_metrics\_output.csv`





