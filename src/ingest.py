import pandas as pd
import os

PROCESSED_FILE = 'data/processed_events.csv'

def load_new_events(df):
    """Filter out events already processed in previous runs (idempotent rerun)."""
    if os.path.exists(PROCESSED_FILE):
        processed = pd.read_csv(PROCESSED_FILE)
        processed_ids = set(processed['event_id'])
        new_df = df[~df['event_id'].isin(processed_ids)].copy()
    else:
        new_df = df.copy()
    return new_df

def mark_processed(df):
    """Append processed event_ids for future reruns."""
    if os.path.exists(PROCESSED_FILE):
        existing = pd.read_csv(PROCESSED_FILE)
        updated = pd.concat([existing, df[['event_id', 'run_id']]], ignore_index=True)
    else:
        updated = df[['event_id', 'run_id']].copy()
    updated.to_csv(PROCESSED_FILE, index=False)