import pandas as pd

def analyze_financials(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes the financial data and returns a summary of descriptive statistics.

    Args:
    df (pd.DataFrame): The financial data.

    Returns:
    pd.DataFrame: A DataFrame containing the descriptive statistics of the financial data.
    """
    financial_summary = df.describe()
    return financial_summary

def analyze_budget(df: pd.DataFrame) -> pd.Series:
    """
    Analyzes the budget data by summing the amounts for each department.

    Args:
    df (pd.DataFrame): The budget data.

    Returns:
    pd.Series: A Series with the sum of amounts for each department.
    """
    budget_summary = df.groupby('Department')['Amount'].sum()
    return budget_summary

def analyze_staffing(df: pd.DataFrame) -> float:
    """
    Analyzes the staffing data to calculate the total overtime hours.

    Args:
    df (pd.DataFrame): The staffing data.

    Returns:
    float: The total overtime hours across all employees.
    """
    total_overtime = df['Overtime_Hours'].sum()
    return total_overtime

def calculate_overtime_cost(df: pd.DataFrame) -> float:
    """
    Calculates the total overtime cost based on the Pay_Rate and Overtime_Hours columns.

    Args:
    df (pd.DataFrame): The staffing data containing Pay_Rate and Overtime_Hours.

    Returns:
    float: The total overtime cost.
    """
    df['overtime_cost'] = df['Pay_Rate'] * df['Overtime_Hours']
    return df['overtime_cost'].sum()

def calculate_overtime_percentage(df: pd.DataFrame) -> float:
    """
    Calculates the percentage of overtime hours worked compared to total hours worked.

    Args:
    df (pd.DataFrame): The staffing data containing Hours_Worked and Overtime_Hours.

    Returns:
    float: The percentage of overtime hours worked.
    """
    total_hours = df['Hours_Worked'].sum()
    overtime_hours = df['Overtime_Hours'].sum()
    return (overtime_hours / total_hours) * 100

def analyze_department_performance(df: pd.DataFrame) -> pd.Series:
    """
    Analyzes the performance of each department by calculating the average Actual_Spend.

    Args:
    df (pd.DataFrame): The budget data containing Actual_Spend.

    Returns:
    pd.Series: A Series containing the average Actual_Spend per department.
    """
    return df.groupby('Department')['Actual_Spend'].mean()

def analyze_budget_variance(df: pd.DataFrame) -> pd.Series:
    """
    Analyzes the budget variance by calculating the total amount spent per department.

    Args:
    df (pd.DataFrame): The budget data containing Amount.

    Returns:
    pd.Series: A Series containing the sum of the budget amounts per department.
    """
    return df.groupby('Department')['Amount'].sum()

def analyze_staffing_overtime(df: pd.DataFrame) -> pd.Series:
    """
    Analyzes overtime hours for each employee.

    Args:
    df (pd.DataFrame): The staffing data containing Overtime_Hours.

    Returns:
    pd.Series: A Series with the total overtime hours per employee.
    """
    return df.groupby('Employee_ID')['Overtime_Hours'].sum()

def analyze_employee_performance(df: pd.DataFrame) -> pd.Series:
    """
    Analyzes the performance of each employee by calculating the average hours worked.

    Args:
    df (pd.DataFrame): The staffing data containing Hours_Worked.

    Returns:
    pd.Series: A Series containing the average Hours_Worked per employee.
    """
    return df.groupby('Employee_ID')['Hours_Worked'].mean()

# Advanced KPI calculations

def calculate_budget_utilization(df: pd.DataFrame) -> pd.Series:
    """
    Calculates the budget utilization by comparing the actual spend to the planned budget.

    Args:
    df (pd.DataFrame): The budget data containing Actual_Spend and Planned_Budget.

    Returns:
    pd.Series: A Series containing the budget utilization percentage for each department.
    """
    df['budget_utilization'] = (df['Actual_Spend'] / df['Planned_Budget']) * 100
    return df.groupby('Department')['budget_utilization'].mean()

def calculate_cost_per_employee(df: pd.DataFrame) -> pd.Series:
    """
    Calculates the cost per employee by dividing the total cost by the number of employees.

    Args:
    df (pd.DataFrame): The staffing data containing Pay_Rate and Overtime_Hours.

    Returns:
    pd.Series: A Series containing the cost per employee for each department.
    """
    df['employee_cost'] = df['Pay_Rate'] * df['Hours_Worked']
    return df.groupby('Department')['employee_cost'].mean()

def calculate_efficiency_ratio(df: pd.DataFrame) -> pd.Series:
    """
    Calculates the efficiency ratio of each department by dividing total output (e.g., revenue) by total input (e.g., cost).

    Args:
    df (pd.DataFrame): The data containing output and input columns.

    Returns:
    pd.Series: A Series containing the efficiency ratio for each department.
    """
    df['efficiency_ratio'] = df['Output'] / df['Input']
    return df.groupby('Department')['efficiency_ratio'].mean()

def calculate_employee_retention_rate(df: pd.DataFrame) -> float:
    """
    Calculates the employee retention rate by dividing the number of retained employees by the total number of employees.

    Args:
    df (pd.DataFrame): The staffing data containing Employee_ID and Retention_Status.

    Returns:
    float: The retention rate as a percentage.
    """
    retained_employees = df[df['Retention_Status'] == 'Retained']
    return (len(retained_employees) / len(df)) * 100
