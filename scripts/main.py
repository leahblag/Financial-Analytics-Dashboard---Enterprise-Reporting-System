import matplotlib.pyplot as plt
import seaborn as sns

def plot_financial_distribution(df):
    plt.figure(figsize=(10, 6))
    df['Amount'].hist()
    plt.title('Financial Amount Distribution')
    plt.xlabel('Amount ($)')
    plt.ylabel('Frequency')
    plt.savefig('financial_distribution.png')
    plt.close()

def plot_budget_variance(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Department', y='Actual_Spend')
    plt.title('Budget Variance by Department')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('budget_variance.png')
    plt.close()

def create_department_dashboard(df):
    plt.figure(figsize=(15, 10))
    
    # Department spending
    plt.subplot(2,1,1)
    dept_totals = df.groupby('Department')['Actual_Spend'].sum()
    dept_totals.plot(kind='bar')
    plt.title('Total Spending by Department')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('department_dashboard.png')
    plt.close()
