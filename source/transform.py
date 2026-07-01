import pandas as pd

def add_grade(df):

    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Marks"].apply(grade)

    def result(marks):
        if marks >= 40:
            return "Pass"
        else:
            return "Fail"

    df["Result"] = df["Marks"].apply(result)

    
    df["Performance Score"] = (
        df["Marks"] * 0.5 +
        df["Attendance"] * 0.3 +
        df["StudyHours"] * 0.2
    )


    return df