import pandas as pd

# -----------------------------
# STEP 1: Load cleaned data
# -----------------------------
df = pd.read_csv("output/cleaned_data.csv")

print("Generating Report...")

# -----------------------------
# STEP 2: Create Summary Tables
# -----------------------------

# Average salary by department
dept_salary = df.groupby("Department")["Salary"].mean().reset_index()

# Count of employees by city
city_count = df.groupby("City")["ID"].count().reset_index()
city_count.columns = ["City", "Employee_Count"]

# Average age by department
dept_age = df.groupby("Department")["Age"].mean().reset_index()

# -----------------------------
# STEP 3: Create Excel Report
# -----------------------------

with pd.ExcelWriter("output/report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
    dept_salary.to_excel(writer, sheet_name="Dept_Salary", index=False)
    city_count.to_excel(writer, sheet_name="City_Count", index=False)
    dept_age.to_excel(writer, sheet_name="Dept_Age", index=False)

print("Report generated successfully!")
print("Saved as output/report.xlsx")