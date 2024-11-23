import pandas as pd
from datetime import datetime

def calculate_overtime_cost(staffing_data):
    """Calculate total overtime cost from staffing data"""
    overtime_cost = (staffing_data['Overtime_Hours'] * staffing_data['Pay_Rate']).sum()
    return overtime_cost

def generate_summary_report(financial_data, budget_data, staffing_data):
    """Generate comprehensive summary report of all metrics"""
    report = {
        'total_transactions': len(financial_data),
        'total_budget': budget_data['Planned_Budget'].sum(),
        'total_overtime_cost': calculate_overtime_cost(staffing_data),
        'average_transaction': financial_data['Amount'].mean(),
        'departments_count': budget_data['Department'].nunique()
    }
    return report

def generate_department_report(budget_data):
    """Generate detailed department-level performance report"""
    dept_metrics = {
        'total_spend': budget_data.groupby('Department')['Actual_Spend'].sum(),
        'budget_variance': budget_data.groupby('Department')['Variance'].sum(),
        'utilization': (budget_data['Actual_Spend'] / budget_data['Planned_Budget'] * 100).groupby(budget_data['Department']).mean()
    }
    return dept_metrics

def generate_executive_summary(financial_data, budget_data, staffing_data):
    """Create executive-level summary with key insights"""
    summary = {
        'financial_metrics': {
            'total_revenue': financial_data['Amount'].sum(),
            'average_transaction_value': financial_data['Amount'].mean(),
            'transaction_volume': len(financial_data)
        },
        'budget_performance': {
            'total_planned': budget_data['Planned_Budget'].sum(),
            'total_actual': budget_data['Actual_Spend'].sum(),
            'variance_percentage': ((budget_data['Actual_Spend'].sum() - budget_data['Planned_Budget'].sum()) 
                                  / budget_data['Planned_Budget'].sum() * 100)
        },
        'workforce_metrics': {
            'total_overtime_hours': staffing_data['Overtime_Hours'].sum(),
            'overtime_cost': calculate_overtime_cost(staffing_data),
            'departments_staffed': staffing_data['Department'].nunique()
        }
    }
    return summary

def export_reports_to_excel(reports, filename=None):
    """Export all reports to Excel workbook"""
    if filename is None:
        filename = f"financial_reports_{datetime.now().strftime('%Y%m%d')}.xlsx"
    
    with pd.ExcelWriter(filename) as writer:
        for report_name, report_data in reports.items():
            pd.DataFrame(report_data).to_excel(writer, sheet_name=report_name)
    
    return filename
