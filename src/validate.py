import pandas as pd

REQUIRED_COLS = ['event_id', 'product_id', 'customer_id', 'event_type', 'quantity', 'amount', 'event_time', 'run_id']
VALID_TYPES = ['sale', 'reversal']

def validate_events(df):
    df = df.copy()
    rejects = []

    # Missing required fields
    missing = df[REQUIRED_COLS].isnull().any(axis=1)
    for idx in df[missing].index:
        rejects.append({'event_id': df.loc[idx, 'event_id'], 'reason': 'missing_required_field'})

    # Invalid event_type
    invalid_type = ~df['event_type'].isin(VALID_TYPES)
    for idx in df[invalid_type].index:
        rejects.append({'event_id': df.loc[idx, 'event_id'], 'reason': 'invalid_event_type'})

    # Duplicate event_id
    dup = df.duplicated(subset=['event_id'], keep='first')
    for idx in df[dup].index:
        rejects.append({'event_id': df.loc[idx, 'event_id'], 'reason': 'duplicate_event_id'})

    valid = df[~missing & ~invalid_type & ~dup].copy()
    return valid, pd.DataFrame(rejects)