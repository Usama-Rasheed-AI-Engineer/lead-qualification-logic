import json
import csv

# 1. Load Data
with open('data.json', 'r') as file:
    leads = json.load(file)

print(f"Processing {len(leads)} leads...")

# 2. Setup CSV Output
# 'w' means Write mode. 'newline=""' prevents blank lines on Windows.
with open('qualified_leads.csv', 'w', newline='') as csvfile:
    # Define column headers
    fieldnames = ['name', 'usage_year', 'injury', 'has_lawyer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader() # Write the top row (Name, Usage Year...)

    # 3. Process & Filter
    for lead in leads:
        if (2015 <= lead['usage_year'] <= 2018) and lead['injury'] == 'Tinnitus' and not lead['has_lawyer']:
            print(f"Saving: {lead['name']}")
            writer.writerow(lead) # Write the qualified lead to the CSV

print("Done. Check 'qualified_leads.csv'.")