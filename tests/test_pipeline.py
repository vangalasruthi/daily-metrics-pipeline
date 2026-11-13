import pandas as pd
from src.transform import calculate_daily_metrics

def test_happy_path():
    df = pd.DataFrame({
        'event_id': [1, 2],
        'product_id': ['P001', 'P001'],
        'customer_id': ['C001', 'C002'],
        'event_type': ['sale', 'sale'],
        'quantity': [2, 1],
        'amount': [100.0, 50.0],
        'event_time': ['2026-11-10T10:00:00', '2026-11-10T11:00:00'],
        'run_id': ['r1', 'r1']
    })
    result = calculate_daily_metrics(df)
    assert len(result) == 1
    assert result['units_sold'].iloc[0] == 3
    assert result['revenue'].iloc[0] == 150.0

def test_reversal():
    df = pd.DataFrame({
        'event_id': [1, 2],
        'product_id': ['P001', 'P001'],
        'customer_id': ['C001', 'C001'],
        'event_type': ['sale', 'reversal'],
        'quantity': [2, 2],
        'amount': [100.0, 100.0],
        'event_time': ['2026-11-10T10:00:00', '2026-11-10T13:00:00'],
        'run_id': ['r1', 'r2']
    })
    result = calculate_daily_metrics(df)
    assert result['units_sold'].iloc[0] == 0
    assert result['revenue'].iloc[0] == 0.0

def test_empty_input():
    df = pd.DataFrame(columns=['event_id', 'product_id', 'customer_id', 'event_type', 'quantity', 'amount', 'event_time', 'run_id'])
    result = calculate_daily_metrics(df)
    assert len(result) == 0