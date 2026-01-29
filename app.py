import streamlit as st
import json
import pandas as pd

# 1. Title and Description
st.title("⚖️ Tort Experts: Lead Qualifier")
st.write("Upload raw lead data to filter for the 'Earplug Lawsuit'.")

# 2. Load Data (Simulating a database connection)
# We use a try/except block just in case the file isn't found
try:
    with open('data.json', 'r') as file:
        raw_data = json.load(file)
    
    # 3. Show Raw Data
    st.subheader("Raw Leads (Input)")
    st.dataframe(raw_data)

    # 4. The "Magic Button"
    if st.button("Run Qualification Logic"):
        qualified_leads = []
        
        for lead in raw_data:
            # Our Safe Logic (reused here)
            if (2015 <= lead['usage_year'] <= 2018) and lead['injury'] == 'Tinnitus' and not lead['has_lawyer']:
                lead['status'] = 'Qualified'
                qualified_leads.append(lead)
            else:
                pass
                
        # 5. Show Results
        if qualified_leads:
            st.success(f"Found {len(qualified_leads)} qualified leads!")
            st.subheader("Qualified Candidates")
            st.dataframe(qualified_leads)
        else:
            st.warning("No leads qualified.")

except FileNotFoundError:
    st.error("Error: 'data.json' not found. Please make sure the file exists.")