lead = {
    'name': 'Mike',
    'usage_year': 2016,
    'injury': 'Tinnitus',
    'has_lawyer': False
}

# The Safe Logic (AND + NOT)
if (2015 <= lead['usage_year'] <= 2018) and lead['injury'] == 'Tinnitus' and not lead['has_lawyer']:
    print("Qualified")
else:
    print("Rejected")