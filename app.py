import streamlit as st
import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load Environment Variables (The Secret Vault)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Configure the Brain (Gemini)
if not api_key:
    st.error("❌ API Key not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash") # "Flash" is fast and cheap for tasks like this

st.title("🤖 AI-Powered Legal Qualifier")
st.write("Upload raw lead data. Gemini will analyze the text for eligibility.")

# 3. Load Data
try:
    with open('data.json', 'r') as file:
        raw_data = json.load(file)
    
    st.subheader("Raw Leads")
    st.dataframe(raw_data)

    if st.button("Run AI Analysis"):
        qualified_leads = []
        progress_bar = st.progress(0)
        
        for index, lead in enumerate(raw_data):
            # Update progress bar
            progress_bar.progress((index + 1) / len(raw_data))
            
            # --- THE AI PROMPT (The "Brain" Logic) ---
            prompt = f"""
            You are a legal assistant for the 'Earplug Lawsuit'.
            Assess this lead based on these strict criteria:
            1. Usage Year: Must be between 2015 and 2018 (inclusive).
            2. Injury: Must be "Tinnitus" or "Hearing Loss" (or similar synonyms like "ringing", "cant hear").
            3. Lawyer: Must NOT currently have a lawyer.

            Lead Data: {json.dumps(lead)}

            Return ONLY the word 'Qualified' or 'Rejected'. Do not add any punctuation.
            """
            
            # Send to Gemini
            try:
                response = model.generate_content(prompt)
                decision = response.text.strip() # Clean up any extra spaces
                
                # Visual Feedback in the app
                st.write(f"Analyzing {lead['name']}... **{decision}**")
                
                if decision == "Qualified":
                    lead['status'] = 'Qualified'
                    qualified_leads.append(lead)
            
            except Exception as e:
                st.error(f"AI Error on {lead['name']}: {e}")

        # Final Results
        st.success(f"Analysis Complete. Found {len(qualified_leads)} qualified leads.")
        if qualified_leads:
            st.dataframe(qualified_leads)

except FileNotFoundError:
    st.error("File 'data.json' not found.")