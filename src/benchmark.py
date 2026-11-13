import pandas as pd
import time
from transform import calculate_daily_metrics

def generate_large_dataset(n=100000):
    import numpy as np
    np.random.seed(42)
    df = pd.DataFrame({
        'event_id': range(1, n + 1),
        'product_id': np.random.choice(['P001', 'P002', 'P003', 'P004', 'P005'], n),
        'customer_id': np.random.choice(['C001', 'C002', 'C003', 'C004', 'C005'], n),
        'event_type': np.random.choice(['sale', 'reversal'], n, p=[0.9, 0.1]),
        'quantity': np.random.randint(1, 10, n),
        'amount': np.random.uniform(10, 500, n).round(2),
        'event_time': pd.date_range('2026-01-01', periods=n, freq='min'),
        'run_id': 'bench'
    })
    return df

if __name__ == '__main__':
    df = generate_large_dataset(100000)
    start = time.time()
    metrics = calculate_daily_metrics(df)
    duration = time.time() - start
    print(f"Processed {len(df)} rows in {duration:.2f}s")
    print(f"Output rows: {len(metrics)}")