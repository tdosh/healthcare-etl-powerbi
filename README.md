## ETL Process

1. Extract: Load raw CSV data (10,000 records)
2. Transform:
    * Standardize column names
    * Parse dates and create time features
    * Calculate derived metrics (length of stay, age groups)
    * Create categorical bins for analysis
    * Handle missing values and duplicates
3. Load: Export cleaned data for Power BI consumption

## Dashboard Screenshots

### Overview Page
![Overview Dashboard](https://github.com/tdosh/healthcare-etl-powerbi/blob/main/Screenshots/Page1_overview.PNG
)

### Patient Demographics
![Demographics](https://github.com/tdosh/healthcare-etl-powerbi/blob/main/Screenshots/page2_demographics.PNG
)

### Billing Analysis
![Billing](https://github.com/tdosh/healthcare-etl-powerbi/blob/main/Screenshots/page3_billing.PNG
)

### Medical Insights
![Insights](https://github.com/tdosh/healthcare-etl-powerbi/blob/main/Screenshots/page4_medinsight.PNG
)

## Technologies Used

* Python: Data extraction and transformation
* Pandas: Data cleaning and manipulation
* Power BI: Interactive dashboard and visualizations
* CSV: Data storage format

## Key Features

* 10,000+ patient records processed
* 4 interactive dashboard pages
* 15+ visualizations including charts, graphs, and KPIs
* Dynamic filtering by age, gender, condition, admission type, date range
* Business insights on patient demographics, billing patterns, and medical trends

## Dashboard Pages

1. Overview: Key metrics, top conditions, admission trends
2. Demographics: Age distribution, blood types, patient profiles
3. Billing Analysis: Cost patterns by condition and admission type
4. Medical Insights: Test results, length of stay, admission patterns

## Technical Architecture

The data flows through three distinct layers to ensure clean, actionable insights:

1. Data Source Layer: Raw healthcare data stored in CSV format containing patient demographics, medical history, and billing info.
2. Processing Layer (ETL): Python and Pandas are used to clean data, handle missing values, and calculate metrics like Length of Stay.
3. Visualization Layer (BI): Cleaned data is loaded into Power BI for analysis. The model uses the processed flat file to drive 15+ interactive visualizations and dynamic KPIs.

## Project Structure

```text
healthcare-etl-powerbi/
├── data/
│   ├── healthcare_dataset.csv       # Raw data
│   └── healthcare_clean.csv         # Cleaned data
├── scripts/
│   └── simple_etl.py                # ETL pipeline
├── powerbi/
│   └── Healthcare_Analytics_Dashboard.pbix
├── screenshots/
│   └── [dashboard screenshots]
└── README.md
```
## How to Run ETL Pipeline
1. Navigate to the scripts folder
2. Run the command: python healthcare_etl.py

## Power BI Dashboard
1. Open Healthcare_Analytics_Dashboard.pbix in Power BI Desktop
2. Refresh data if needed
3. Interact with filters and visualizations

## Key Insights Discovered
 * Arthritis, Diabetes, and Hypertension are top 3 conditions
 * Average patient stay: 15 days
 * Emergency admissions show higher average costs
 * Patient age peaks in 45-65 range
 * Test result distribution: Normal (33%), Abnormal (33%), Inconclusive (33%)

## Skills Demonstrated
 * ETL Development: Data extraction, transformation, loading
 * Python Programming: Pandas, data manipulation, scripting
 * Business Intelligence: Power BI dashboard creation
 * Data Analysis: Statistical analysis, pattern recognition
 * Data Visualization: Interactive charts and KPIs
 * Data Quality: Cleaning, validation, standardization

## Dataset
 * Source: Kaggle Healthcare Dataset
 * Records: 10,000+ synthetic patient records
 * Features: Demographics, medical conditions, billing, admissions, test results

## Author
Tyler Dosh

GitHub: @tdosh

LinkedIn: https://www.linkedin.com/in/tyler-dosh/

Email: tdosh05@gmail.com

## License
MIT License
