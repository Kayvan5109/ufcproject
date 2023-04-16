import pandas as pd
import streamlit as st

# Load the datasets
ufc_stat = pd.read_csv("ufc_stat.csv")
fighters = pd.read_csv("fighters.csv")
ufc_avg = pd.read_csv("ufc_avg.csv")
ufc_std = pd.read_csv("ufc_std.csv")

# Set page title
st.set_page_config(page_title="UFC Fighter Stats")

# Set app header
st.title("UFC Fighter Stats")

# User input for fighter name
fighter_name = st.text_input("Enter a fighter's name:")

# Filter fighter stats by name
fighter_stats = fighters[fighters["Fighter Name"].str.contains(fighter_name)]

# Display fighter stats and weight class stats
if not fighter_stats.empty:
    st.subheader(fighter_name)
    st.write(fighter_stats[["Fighter Name", "Weight Class", "# of Fights", "Wins", "Decision Wins", "KO/TKO Wins", "Submission Wins",
                            "avg fight duration", "Avg Strikes Per Fight", "Avg Sig Strikes Per Fight", "Avg TDA Per Fight", "Avg TDL Per Fight",
                            "average control time", "LP Count", "Bangfest Count", "strikes absorbed per fight", "Stinker Count",
                            "Potential Robbery Count", "Standup Count", "Comeback Count", "Massacre Count"]])
    
    weight_class = fighter_stats.iloc[0]["Weight Class"]
    weight_class_avg = ufc_avg[ufc_avg["Weight Class"] == weight_class].reset_index(drop=True)
    weight_class_std = ufc_std[ufc_std["Weight Class"] == weight_class].reset_index(drop=True)
    
    st.subheader(f"{weight_class} Average Stats")
    st.write(weight_class_avg)
    
    st.subheader(f"{weight_class} Standard Deviations")
    st.write(weight_class_std)
else:
    st.write("No fighter found with that name.")
