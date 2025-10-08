import pandas as pd
import psycopg2


df = pd.read_csv(r"C:\Users\dell\Desktop\Python Assessment1(Karan)\assessment2\apna_jobs_python_cleaned.csv")


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",    
    user="postgres",        
    password="karan9630"
)
cur = conn.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS python_jobs1 (
    id SERIAL PRIMARY KEY,
    job_title TEXT,
    company TEXT,
    location TEXT,
    salary INTEGER
);
"""
cur.execute(create_table_query)
conn.commit()


for _, row in df.iterrows():
    salary = row["Salary (Numeric)"]
    if pd.notna(salary): 
        cur.execute(
            """
            INSERT INTO python_jobs1 (job_title, company, location, salary)
            VALUES (%s, %s, %s, %s)
            """,
            (row["Job Title"], row["Company"], row["Location"], int(salary))
        )

conn.commit()
print("inserted successfully!")


cur.close()
conn.close()
