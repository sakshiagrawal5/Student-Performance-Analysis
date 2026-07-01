import pandas as pd

def generate_report(df, analysis):

    report = {}

    report["Total Students"] = len(df)
    report["Passed Students"] = (df["Marks"] >= 40).sum()
    report["Failed Students"] = (df["Marks"] < 40).sum()

    report["Highest Marks"] = analysis["Highest Marks"]
    report["Lowest Marks"] = analysis["Lowest Marks"]
    report["Average Marks"] = analysis["Average Marks"]
    report["Average Attendance"] = analysis["Average Attendance"]

    
    for grade in analysis["Grade Distribution"]:
        report["Grade " + str(grade) + " Count"] = analysis["Grade Distribution"][grade]

    report_df = pd.DataFrame([report])

    return report_df


def save_report(df, path):

    df.to_csv(path, index=False)
    print("Report saved at:", path)