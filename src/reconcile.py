import pandas as pd

def reconcile(df, metrics):
    input_count = len(df)
    output_count = len(metrics)
    input_revenue = df[df['event_type'] == 'sale']['amount'].sum() - df[df['event_type'] == 'reversal']['amount'].sum()
    output_revenue = metrics['revenue'].sum()
    status = 'PASS' if abs(input_revenue - output_revenue) < 0.01 else 'FAIL'
    report = {
        'input_rows': input_count,
        'output_rows': output_count,
        'input_revenue': input_revenue,
        'output_revenue': output_revenue,
        'reconciliation_status': status
    }
    print("=== Reconciliation Report ===")
    print(report)
    return report