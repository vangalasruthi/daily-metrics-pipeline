import pandas as pd

def calculate_daily_metrics(df):
    df = df.copy()
    df['event_date'] = pd.to_datetime(df['event_time']).dt.date

    sales = df[df['event_type'] == 'sale'].groupby(['event_date', 'product_id']).agg(
        units_sold=('quantity', 'sum'),
        revenue=('amount', 'sum'),
        active_transactions=('event_id', 'count')
    ).reset_index()

    reversals = df[df['event_type'] == 'reversal'].groupby(['event_date', 'product_id']).agg(
        units_sold=('quantity', 'sum'),
        revenue=('amount', 'sum'),
        active_transactions=('event_id', 'count')
    ).reset_index()

    metrics = sales.merge(reversals, on=['event_date', 'product_id'], how='outer', suffixes=('_sale', '_reversal'))
    metrics = metrics.fillna(0)
    metrics['units_sold'] = metrics['units_sold_sale'] - metrics['units_sold_reversal']
    metrics['revenue'] = metrics['revenue_sale'] - metrics['revenue_reversal']
    metrics['active_transactions'] = metrics['active_transactions_sale'] - metrics['active_transactions_reversal']
    metrics = metrics[['event_date', 'product_id', 'units_sold', 'revenue', 'active_transactions']]
    return metrics