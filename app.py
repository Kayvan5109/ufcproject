import pandas as pd
import streamlit as st

# Load the datasets
ufc_stat = pd.read_csv("ufc_stat.csv")
fighters = pd.read_csv("fighters.csv")

# Set page title
st.set_page_config(page_title="UFC Fighter Stats")

# Set app header
st.title("UFC Fighter Stats")

# User input for fighter name
fighter_name = st.text_input("Enter a fighter's name:")

# Filter fighter stats by name
fighter_stats = fighters[fighters["Fighter Name"].str.contains(fighter_name)]

# Display fighter stats
if not fighter_stats.empty:
    st.subheader(fighter_name)
    st.write(fighter_stats[["Fighter Name", "Weight Class", "# of Fights", "Wins", "Decision Wins", "KO/TKO Wins", "Submission Wins",
                            "avg fight duration", "Avg Strikes Per Fight", "Avg Sig Strikes Per Fight", "Avg TDA Per Fight", "Avg TDL Per Fight",
                            "average control time", "LP Count", "Bangfest Count", "strikes absorbed per fight", "Stinker Count",
                            "Potential Robbery Count", "Standup Count", "Comeback Count", "Massacre Count"]])
    
    st.subheader("UFC Stat Data")
    
    # Filter ufc_stat by fighter name in either "Fighter 1" or "Fighter 2"
    ufc_fighter_stats = ufc_stat[(ufc_stat["Fighter 1"].str.contains(fighter_name)) | (ufc_stat["Fighter 2"].str.contains(fighter_name))]
    
    # Display ufc_stat data
    if not ufc_fighter_stats.empty:
        st.write(ufc_fighter_stats)
    else:
        st.write("No fighter found in UFC Stat data.")
else:
    st.write("No fighter found with that name.")
