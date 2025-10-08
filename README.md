# Python Job Scraping and Data Analysis

This project is about scraping job data from Apna Jobs website using Python, cleaning it, and then storing it in PostgreSQL database. After storing, I did some analysis using pandas to get insights like average salary, most common job title, and jobs by location.

## Steps I did

### 1. Web Scraping
I used selenium to scrape job titles, company name, location, and salary from Apna Jobs website.  
The scraped data was stored in a CSV file for cleaning.

### 2. Data Cleaning
Then I used openpyxl and pandas to clean the salary column.  
Some salary ranges like ₹25,000–₹30,000 were converted to average values like 27500.  
Finally, I added a new column called Salary (Numeric).

### 3. Storing in PostgreSQL
After cleaning, I connected Python to PostgreSQL using psycopg2.  
I created a table called python_jobs1 and inserted all rows which had numeric salary data.  


### 4. Data Analysis
Once data was in the database, I used pandas to do some analysis like:
- Finding average salary by job title and location
- Counting number of jobs for each location
- Checking which job title appears most often

### 5. Git and Version Control
I made commits after each main part:
- Initial commit
- Added scraping code
- Cleaned salary data
- Added database insertion
- Added analysis part

