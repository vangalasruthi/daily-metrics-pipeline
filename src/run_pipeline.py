import pandas as pd
from transform import calculate_daily_metrics
from validate import validate_events
from reconcile import reconcile

df = pd.read_csv('data/sample_input.csv')
valid, rejects = validate_events(df)
metrics = calculate_daily_metrics(valid)

print("=== Daily Metrics ===")
print(metrics)
print("\n=== Rejected Records ===")
print(rejects)

metrics.to_csv('data/daily_metrics_output.csv', index=False)
rejects.to_csv('data/rejected_records.csv', index=False)

reconcile(valid, metrics)