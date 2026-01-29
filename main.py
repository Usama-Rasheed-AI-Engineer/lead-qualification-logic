# Safe data extraction
lead = {'id': 2} 
# Using the empty dict trick to prevent crashing
email = lead.get('contact_info', {}).get('email', 'No Email')
print(f"Lead Email: {email}")