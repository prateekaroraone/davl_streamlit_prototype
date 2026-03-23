import pandas as pd
import yaml
from datetime import datetime

def load_registry(path="decision_registry.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)['decisions']

def check_freshness(file_path, max_hours):
    df = pd.read_csv(file_path)
    latest_ts = pd.to_datetime(df['timestamp']).max()
    age_hours = (datetime.now() - latest_ts).total_seconds() / 3600
    return age_hours <= max_hours, age_hours

def check_completeness(df, min_completeness):
    completeness = df.notnull().sum().sum() / df.size
    return completeness >= min_completeness, completeness

def validate_decision(decision):
    results = {}
    for source in decision['sources']:
        df = pd.read_csv(source)
        r = decision['requirements']
        fresh_pass, age = check_freshness(source, r.get('freshness_hours', 24))
        comp_pass, completeness = check_completeness(df, r.get('min_completeness', 1.0))
        results[source] = {
            'fresh_pass': fresh_pass,
            'age_hours': age,
            'completeness_pass': comp_pass,
            'completeness': completeness
        }
    return results
