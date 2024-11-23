import pandas as pd

def validate_financial_data(df):
    """Validates financial data structure and content"""
    required_columns = ['Transaction_Date', 'Amount', 'Department']
    validation_results = {
        'has_required_columns': all(col in df.columns for col in required_columns),
        'no_negative_amounts': (df['Amount'] >= 0).all(),
        'valid_dates': pd.to_datetime(df['Transaction_Date'], errors='coerce').notna().all()
    }
    return validation_results

def validate_budget_data(df):
    """Validates budget data integrity"""
    validation_results = {
        'planned_budget_present': df['Planned_Budget'].notna().all(),
        'valid_departments': df['Department'].notna().all(),
        'valid_amounts': df['Actual_Spend'].notna().all()
    }
    return validation_results

def validate_staffing_data(df):
    """Validates staffing data completeness"""
    validation_results = {
        'valid_hours': (df['Hours_Worked'] > 0).all(),
        'valid_employees': df['Employee_ID'].notna().all(),
        'valid_departments': df['Department'].notna().all()
    }
    return validation_results

def check_data_quality(df):
    """Performs comprehensive data quality assessment"""
    quality_metrics = {
        'completeness': df.notna().mean(),
        'unique_values': df.nunique(),
        'value_ranges': df.describe()
    }
    return quality_metrics
