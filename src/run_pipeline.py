import pandas as pd
import logging
import time
from transform import calculate_daily_metrics
from validate import validate_events
from reconcile import reconcile
from ingest import load_new_events, mark_processed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

run_id = f"run_{int(time.time())}"
start_time = time.time()
logger.info(f"Pipeline started | run_id={run_id}")

df = pd.read_csv('data/sample_input.csv')
new_df = load_new_events(df)
logger.info(f"Input rows: {len(df)} | New rows: {len(new_df)}")

if len(new_df) == 0:
    logger.info("No new events to process (idempotent rerun).")
else:
    valid, rejects = validate_events(new_df)
    metrics = calculate_daily_metrics(valid)
    logger.info(f"Valid rows: {len(valid)} | Rejected rows: {len(rejects)} | Output rows: {len(metrics)}")
    print("=== Daily Metrics ===")
    print(metrics)
    print("\n=== Rejected Records ===")
    print(rejects)
    metrics.to_csv('data/daily_metrics_output.csv', index=False)
    rejects.to_csv('data/rejected_records.csv', index=False)
    reconcile(valid, metrics)
    mark_processed(valid)

end_time = time.time()
logger.info(f"Pipeline completed | run_id={run_id} | duration={end_time - start_time:.2f}s")