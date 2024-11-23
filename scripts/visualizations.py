import matplotlib.pyplot as plt
import seaborn as sns

def plot_financial_distribution(df):
    """Creates histogram of financial distributions"""
    plt.figure(figsize=(10, 6))
    df['Amount'].hist()
    plt.title('Financial Amount Distribution')
    plt.xlabel('Amount ($)')
    plt.ylabel('Frequency')
    plt.savefig('financial_distribution.png')
    plt.close()

def plot_budget_variance(df):
    """Visualizes budget variance across departments"""
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Department', y='Actual_Spend')
    plt.title('Budget Variance by Department')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('budget_variance.png')
    plt.close()

def create_department_dashboard(df):
    """Creates comprehensive department performance dashboard"""
    plt.style.use('seaborn')
    fig = plt.figure(figsize=(15, 10))
    
    # Department spending
    plt.subplot(2,1,1)
    dept_totals = df.groupby('Department')['Actual_Spend'].sum()
    dept_totals.plot(kind='bar')
    plt.title('Total Spending by Department')
    plt.xticks(rotation=45)
    
    # Department trends
    plt.subplot(2,1,2)
    sns.lineplot(data=df, x='Period', y='Actual_Spend', hue='Department')
    plt.title('Spending Trends by Department')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('department_dashboard.png')
    plt.close()
