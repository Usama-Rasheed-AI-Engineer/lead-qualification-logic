import json

# Load the data from the "outside"
with open('data.json', 'r') as file:
    leads = json.load(file)

print(f"Loaded {len(leads)} leads from file.\n")

# Process each lead dynamically
for lead in leads:
    # Our Safe Logic
    if (2015 <= lead['usage_year'] <= 2018) and lead['injury'] == 'Tinnitus' and not lead['has_lawyer']:
        print(f"PASS: {lead['name']} is Qualified.")
    else:
        print(f"FAIL: {lead['name']} is Rejected.")