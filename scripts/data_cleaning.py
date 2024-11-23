import pandas as pd

def clean_financial_data(df):
    df = df.copy()
    # Handle negative values in parentheses and remove currency symbols
    df['Amount'] = df['Amount'].str.replace('$', '')\
                              .str.replace(',', '')\
                              .str.replace('(', '-')\
                              .str.replace(')', '')\
                              .astype(float)
    return df

def clean_budget_data(df):
    df = df.copy()
    # Standardize department names and handle case sensitivity
    df['Department'] = df['Department'].str.strip().str.title()
    df['Planned_Budget'] = pd.to_numeric(df['Planned_Budget'], errors='coerce')
    df['Actual_Spend'] = pd.to_numeric(df['Actual_Spend'], errors='coerce')
    return df

def clean_staffing_data(df):
    df = df.copy()
    # Standardize certification status and position titles
    df['Position'] = df['Position'].str.strip().str.title()
    df['Certification_Status'] = df['Certification_Status'].str.strip().str.title()
    df['Overtime_Hours'] = df.apply(lambda x: max(x['Hours_Worked'] - 8, 0), axis=1)
    return df
