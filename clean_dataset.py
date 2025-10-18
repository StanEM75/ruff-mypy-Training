import pandas as pd

df = pd.read_csv('data/vgsales.csv')

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values 
    cols = df.columns
    for col in cols:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('Unknown')
        else:
            df[col] = df[col].fillna(df[col].median())
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.capitalize().str.replace(' ', '_')

    return df

cleaned_df = clean_dataset(df)

cleaned_df.to_csv('outputs/cleaned_vgsales.csv', index=False)