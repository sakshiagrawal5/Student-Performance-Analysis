import pandas as pd

def analyze_data(df):

    analysis = {}   

    analysis["Average Marks"] = df["Marks"].mean()
    analysis["Highest Marks"] = df["Marks"].max()
    analysis["Lowest Marks"] = df["Marks"].min()

    analysis["Average Attendance"] = df["Attendance"].mean()
    analysis["Average Study Hours"] = df["StudyHours"].mean()

    analysis["Pass %"] = (df["Marks"] >= 40).mean() * 100
    analysis["Fail %"] = (df["Marks"] < 40).mean() * 100

    analysis["Grade Distribution"] = df["Grade"].value_counts().to_dict()

    print(analysis)

    return analysis  


def sorting(df):

    print("\nSorted by Marks")
    print(df.sort_values("Marks", ascending=False))

    print("\nSorted by Attendance")
    print(df.sort_values("Attendance", ascending=False))

    print("\nSorted by Study Hours")
    print(df.sort_values("StudyHours", ascending=False))