import pandas as pd
from src.transform import calculate_daily_metrics
from src.validate import validate_events

def test_malformed_input():
    df = pd.DataFrame({
        'event_id': [1],
        'product_id': ['P001'],
        'customer_id': ['C001'],
        'event_type': ['invalid_type'],
        'quantity': [2],
        'amount': [100.0],
        'event_time': ['2026-11-10T10:00:00'],
        'run_id': ['r1']
    })
    valid, rejects = validate_events(df)
    assert len(valid) == 0
    assert len(rejects) == 1
    assert rejects['reason'].iloc[0] == 'invalid_event_type'

def test_null_required_field():
    df = pd.DataFrame({
        'event_id': [1],
        'product_id': [None],
        'customer_id': ['C001'],
        'event_type': ['sale'],
        'quantity': [2],
        'amount': [100.0],
        'event_time': ['2026-11-10T10:00:00'],
        'run_id': ['r1']
    })
    valid, rejects = validate_events(df)
    assert len(valid) == 0
    assert len(rejects) == 1
    assert rejects['reason'].iloc[0] == 'missing_required_field'

def test_duplicate_event():
    df = pd.DataFrame({
        'event_id': [1, 1],
        'product_id': ['P001', 'P001'],
        'customer_id': ['C001', 'C001'],
        'event_type': ['sale', 'sale'],
        'quantity': [2, 2],
        'amount': [100.0, 100.0],
        'event_time': ['2026-11-10T10:00:00', '2026-11-10T10:00:00'],
        'run_id': ['r1', 'r1']
    })
    valid, rejects = validate_events(df)
    assert len(valid) == 1
    assert len(rejects) == 1
    assert rejects['reason'].iloc[0] == 'duplicate_event_id'

def test_late_event():
    df = pd.DataFrame({
        'event_id': [1, 2],
        'product_id': ['P001', 'P001'],
        'customer_id': ['C001', 'C002'],
        'event_type': ['sale', 'sale'],
        'quantity': [2, 1],
        'amount': [100.0, 50.0],
        'event_time': ['2026-11-10T10:00:00', '2026-11-09T09:00:00'],
        'run_id': ['r1', 'r2']
    })
    result = calculate_daily_metrics(df)
    assert len(result) == 2
    assert result[result['event_date'] == pd.to_datetime('2026-11-09').date()]['units_sold'].iloc[0] == 1