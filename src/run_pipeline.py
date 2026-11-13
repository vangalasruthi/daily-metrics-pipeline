import pandas as pd
from transform import calculate_daily_metrics

df = pd.read_csv('data/sample_input.csv')
metrics = calculate_daily_metrics(df)
print(metrics)
metrics.to_csv('data/daily_metrics_output.csv', index=False)