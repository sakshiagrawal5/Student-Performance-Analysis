import pandas as pd   

def clean_data(df):

    df = df.drop_duplicates()

    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
    df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
    df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
    df["Name"] = df["Name"].fillna("Unknown")

    df = df[df["Attendance"] >= 0]
    df = df[df["Attendance"] <= 100]

    df = df[df["StudyHours"] >= 0]

    df = df[df["Marks"] >= 0]
    df = df[df["Marks"] <= 100]

    return df


def save_cleaned(df, path):

    df.to_csv(path, index=False)
    print("Cleaned data saved at:", path)