"""
Healthcare Data ETL Script
Cleans and transforms raw healthcare data for Power BI analysis
"""
import os
import pandas as pd
from datetime import datetime

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data(file_path):
    """Load raw healthcare data"""
    print("Loading data...")
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        print(f"Current directory: {os.getcwd()}")
        print(f"Looking for file at: {os.path.abspath(file_path)}")
        return None
    
    df = pd.read_csv(file_path)
    print(f"Successfully loaded {len(df)} records")
    return df

def transform_data(df):
    """Clean and transform the data"""
    print("Transforming data...")
    
    # 1. Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # 2. Convert date columns
    df['date_of_admission'] = pd.to_datetime(df['date_of_admission'])
    df['discharge_date'] = pd.to_datetime(df['discharge_date'])
    
    # 3. Calculate length of stay
    df['length_of_stay'] = (df['discharge_date'] - df['date_of_admission']).dt.days
    
    # 4. Create age groups
    df['age_group'] = pd.cut(
        df['age'], 
        bins=[0, 18, 35, 50, 65, 100], 
        labels=['Child (0-18)', 'Young Adult (19-35)', 'Adult (36-50)', 
                'Senior (51-65)', 'Elderly (66+)']
    )
    
    # 5. Extract date components for time analysis
    df['admission_year'] = df['date_of_admission'].dt.year
    df['admission_month'] = df['date_of_admission'].dt.month
    df['admission_month_name'] = df['date_of_admission'].dt.month_name()
    df['admission_day_of_week'] = df['date_of_admission'].dt.day_name()
    
    # 6. Create billing categories
    df['billing_category'] = pd.cut(
        df['billing_amount'],
        bins=[0, 10000, 25000, 40000, 100000],
        labels=['Low (<$10k)', 'Medium ($10k-$25k)', 
                'High ($25k-$40k)', 'Very High (>$40k)']
    )
    
    # 7. Clean text fields
    df['name'] = df['name'].str.strip().str.title()
    df['gender'] = df['gender'].str.strip().str.title()
    df['medical_condition'] = df['medical_condition'].str.strip().str.title()
    df['blood_type'] = df['blood_type'].str.strip()
    df['admission_type'] = df['admission_type'].str.strip().str.title()
    df['test_results'] = df['test_results'].str.strip().str.title()
    
    # 8. Handle missing values
    df['medical_condition'].fillna('Unknown', inplace=True)
    df['test_results'].fillna('Pending', inplace=True)
    
    # 9. Remove duplicates
    original_count = len(df)
    df = df.drop_duplicates(subset=['name', 'date_of_admission'])
    duplicates_removed = original_count - len(df)
    
    print(f"Transformation complete!")
    print(f"   - Records after cleaning: {len(df)}")
    print(f"   - Duplicates removed: {duplicates_removed}")
    print(f"   - Columns created: {len(df.columns)}")
    
    return df

def export_data(df, output_path):
    """Export cleaned data to CSV"""
    print("Exporting data...")
    
    # Create directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df.to_csv(output_path, index=False)
    print(f"Data exported to: {output_path}")

def generate_summary_stats(df):
    """Generate summary statistics"""
    print("\n" + "="*60)
    print("DATA SUMMARY STATISTICS")
    print("="*60)
    print(f"Total Patients: {len(df):,}")
    print(f"Date Range: {df['date_of_admission'].min()} to {df['date_of_admission'].max()}")
    print(f"Average Age: {df['age'].mean():.1f} years")
    print(f"Average Billing: ${df['billing_amount'].mean():,.2f}")
    print(f"Average Length of Stay: {df['length_of_stay'].mean():.1f} days")
    print(f"\nTop 5 Medical Conditions:")
    print(df['medical_condition'].value_counts().head())
    print("="*60 + "\n")

def main():
    """Run the complete ETL pipeline"""
    print("\nStarting Healthcare ETL Pipeline")
    print("="*60)
    
    # File paths using BASE_DIR for portability
    input_file = os.path.join(BASE_DIR, '..', 'data', 'healthcare_dataset.csv')
    output_file = os.path.join(BASE_DIR, '..', 'data', 'healthcare_clean.csv')
    
    # ETL Process
    df = load_data(input_file)
    
    if df is None:
        print("ERROR: Could not load data. Exiting.")
        return
    
    df_clean = transform_data(df)
    generate_summary_stats(df_clean)
    export_data(df_clean, output_file)
    
    print("="*60)
    print("ETL Pipeline Complete!")
    print(f"Clean data ready at: {output_file}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
