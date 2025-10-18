#import pandas, numpy as np
import pandas as pd

#def load_data(file_path)->pd.DataFrame:
def load_data(file_path) -> pd.DataFrame:
 df = pd.read_csv(file_path)
 print("Data loaded!") 
 return df


def clean_dataset(df):
    df["price"] = df["price"].fillna(0)
    df["quantity"] = df["quantity"].fillna(1.0)
    df['total'] = df["price"]*df["quantity"]
    df['category'] = df['category'].str.lower()
    df = df.drop_duplicates()
    df['date'] = pd.to_datetime(df['date'], errors='ignore')
    #return df, "extra_return_value"  # ⚠️ Mauvais retour
    return df

#def compute_stats(df:pd.DataFrame)->None:
def compute_stats(df: pd.DataFrame) -> None:
  mean=df["total"].mean()
  median=df["total"].median( )
  print(f"Mean:{mean},Median:{median}")

#def save_clean_data(df: pd.DataFrame, output:str):
def save_clean_data(df: pd.DataFrame, output: str):
   df.to_csv(output,index=False)
   print("Data saved at",output)

if __name__=="__main__":
    file = "data.csv"
    data = load_data(file)
    cleaned = clean_dataset(data)
    compute_stats(cleaned)
    save_clean_data(cleaned,"cleaned.csv")
    #print("Job done!!")
    print("Job done!!")
