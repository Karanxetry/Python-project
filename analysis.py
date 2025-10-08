import pandas as pd
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",      
    user="postgres",          
    password="karan9630"      
)


query = "SELECT job_title, company, location, salary FROM python_jobs1;"
df = pd.read_sql_query(query, conn)
print("Data loaded successfully from PostgreSQL\n")

print(df.head())


avg_salary_by_job = df.groupby("job_title")["salary"].mean().reset_index().sort_values(by="salary", ascending=False)
print("\nAverage Salary by Job Title:")
print(avg_salary_by_job)


avg_salary_by_location = df.groupby("location")["salary"].mean().reset_index().sort_values(by="salary", ascending=False)
print("\nAverage Salary by Location:")
print(avg_salary_by_location)


common_jobs = df["job_title"].value_counts().reset_index()
common_jobs.columns = ["job_title", "count"]
print("\nMost Common Job Titles:")
print(common_jobs)


job_count_location = df["location"].value_counts().reset_index()
job_count_location.columns = ["location", "job_count"]
print("\nNumber of Job Listings per Location:")
print(job_count_location)


output_path = r"C:\Users\dell\Desktop\Python Assessment1(Karan)\assessment2\job_analysis_results.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    avg_salary_by_job.to_excel(writer, sheet_name="Avg Salary by Job", index=False)
    avg_salary_by_location.to_excel(writer, sheet_name="Avg Salary by Location", index=False)
    common_jobs.to_excel(writer, sheet_name="Common Jobs", index=False)
    job_count_location.to_excel(writer, sheet_name="Jobs per Location", index=False)

print(f"\nAnalysis completed and saved to Excel:\n{output_path}")


conn.close()
