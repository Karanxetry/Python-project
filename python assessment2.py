from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

driver=webdriver.Chrome()


driver.get("https://apna.co/jobs?search=true&text=python")
time.sleep(5)

all_jobs = []


for page in range(2):   
    print(f"Scraping Page {page + 1}...")

    time.sleep(5)
    job_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='job-card']")

    for job in job_cards:
        try:
            title = job.find_element(By.CSS_SELECTOR, "h2[data-testid='job-title']").text
        except:
            title = "N/A"

        try:
            company = job.find_element(By.CSS_SELECTOR, "div[data-testid='company-title']").text
        except:
            company = "N/A"

        try:
            location = job.find_element(By.CSS_SELECTOR, "p[data-testid='job-location']").text
        except:
            location = "N/A"

        try:
            salary = job.find_element(By.CSS_SELECTOR, "p[data-testid='job-salary']").text
        except:
            salary = "N/A"

        all_jobs.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Salary": salary
        })

    
    try:
        next_button = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
        driver.execute_script("arguments[0].click();", next_button)
        print("Next page clicked.")
        time.sleep(5)
    except:
        print("No next page found.")
        break


df = pd.DataFrame(all_jobs)
df.to_csv("apna_jobs_python.csv", index=False, encoding="utf-8-sig")

print("Scraping completed. Data saved to apna_jobs_python.csv")

driver.quit()





import pandas as pd
import re


df = pd.read_csv("apna_jobs_python.csv")


def extract_salary(salary_text):
    if isinstance(salary_text, str):
        
        nums = re.findall(r'\d[\d,]*', salary_text)
        if nums:
            
            nums = [int(x.replace(',', '')) for x in nums]
            return sum(nums) / len(nums)
    return None  

df["Salary (Numeric)"] = df["Salary"].apply(extract_salary)


df_numeric = df.dropna(subset=["Salary (Numeric)"])


average_salary = df_numeric["Salary (Numeric)"].mean()

print(f"Average monthly salary: ₹{average_salary:,.0f}")


df.to_csv("apna_jobs_python_cleaned.csv", index=False, encoding="utf-8-sig")




