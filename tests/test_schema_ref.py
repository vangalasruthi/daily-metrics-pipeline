import pandas as pd
from src.validate import validate_events

def test_unexpected_schema_change():
    df = pd.DataFrame({
        'event_id': [1],
        'product_id': ['P001'],
        'customer_id': ['C001'],
        'event_type': ['sale'],
        'quantity': [2],
        'amount': [100.0],
        'event_time': ['2026-11-10T10:00:00'],
        'run_id': ['r1'],
        'unexpected_col': ['xyz']
    })
    valid, rejects = validate_events(df)
    assert len(valid) == 1
    assert 'unexpected_col' in df.columns

def test_invalid_reference_key():
    df = pd.DataFrame({
        'event_id': [1],
        'product_id': ['P999'],
        'customer_id': ['C001'],
        'event_type': ['sale'],
        'quantity': [2],
        'amount': [100.0],
        'event_time': ['2026-11-10T10:00:00'],
        'run_id': ['r1']
    })
    valid, rejects = validate_events(df)
    assert len(valid) == 1