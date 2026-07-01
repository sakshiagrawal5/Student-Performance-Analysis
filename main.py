import os

from source.load_data import load_data
from source.clean_data import clean_data, save_cleaned
from source.transform import add_grade
from source.analyze import analyze_data, sorting
from source.report import generate_report, save_report


DATA_PATH = "data/student_dataset_v2.csv"
OUTPUT_DIR = "output"


os.makedirs(OUTPUT_DIR, exist_ok=True)


df = load_data(DATA_PATH)

df = clean_data(df)
save_cleaned(df, OUTPUT_DIR + "/cleaned_data.csv")


df = add_grade(df)


toppers = df[df["Marks"] > 85]
failed = df[df["Marks"] < 40]

toppers.to_csv(OUTPUT_DIR + "/toppers.csv", index=False)
failed.to_csv(OUTPUT_DIR + "/failed.csv", index=False)

print("Toppers saved")
print("Failed students saved")


analysis = analyze_data(df)
sorting(df)


top10 = df.sort_values("Performance Score", ascending=False).head(10)

print("\nTop 10 Students")
print(top10[["ID", "Name", "Performance Score"]])

top10.to_csv(OUTPUT_DIR + "/top10.csv", index=False)


report_df = generate_report(df, analysis)
save_report(report_df, OUTPUT_DIR + "/report.csv")

print("\nProject completed")

print("Failed students:", len(failed))