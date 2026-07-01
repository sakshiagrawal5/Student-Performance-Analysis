import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    print("First 5 Rows")
    print(df.head())

    print("\nLast 5 Rows")
    print(df.tail())

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns)

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Records")
    print(df.duplicated().sum())

    print("\nDescriptive Statistics")
    print(df.describe())

    print("\nMemory Usage")
    print(df.memory_usage())

    print("\nSummary")
    print(df.info())

    return df