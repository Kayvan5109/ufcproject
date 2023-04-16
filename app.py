import pandas as pd
import streamlit as st

def display_fight_history(fighter_name):
    fight_history = ufc_stat[(ufc_stat["Fighter 1"].str.contains(fighter_name, case=False)) | (ufc_stat["Fighter 2"].str.contains(fighter_name, case=False))]
    st.subheader(f"{fighter_name}'s Fight History")
    st.write(fight_history)

# Load the datasets
ufc_stat = pd.read_csv("ufc_stat.csv")
fighters = pd.read_csv("fighters.csv")
ufc_avg = pd.read_csv("ufc_avg.csv")
ufc_std = pd.read_csv("ufc_std.csv")

# Set page title
st.set_page_config(page_title="UFC Fighter Stats")

# Set app header
st.title("UFC Fighter Stats")

# Create tabs
tab = st.sidebar.selectbox("Select a tab", ["Fighters", "Matchup Lookup"])

if tab == "Fighters":
    # User input for fighter name
    fighter_name = st.text_input("Enter a fighter's name:")

    # Filter fighter stats by name
    fighter_stats = fighters[fighters["Fighter Name"].str.contains(fighter_name, case=False)]

    # Display fighter stats and weight class stats
    if not fighter_stats.empty:
        st.subheader(fighter_name)
        st.write(fighter_stats)

        weight_class = fighter_stats.iloc[0]["Weight Class"]
        weight_class_avg = ufc_avg[ufc_avg["Weight Class"] == weight_class].reset_index(drop=True)
        weight_class_std = ufc_std[ufc_std["Weight Class"] == weight_class].reset_index(drop=True)

        st.subheader(f"{weight_class} Average Stats")
        st.write(weight_class_avg)

        st.subheader(f"{weight_class} Standard Deviations")
        st.write(weight_class_std)

        display_fight_history(fighter_name)

    else:
        st.write("No fighter found with that name.")

elif tab == "Matchup Lookup":
    # User input for two fighter names
    fighter1_name = st.text_input("Enter the first fighter's name:")
    fighter2_name = st.text_input("Enter the second fighter's name:")

    # Filter fighter stats by name
    fighter1_stats = fighters[fighters["Fighter Name"].str.contains(fighter1_name, case=False)]
    fighter2_stats = fighters[fighters["Fighter Name"].str.contains(fighter2_name, case=False)]

    # Display fighter stats and weight class stats for both fighters
    if not fighter1_stats.empty and not fighter2_stats.empty:
        st.subheader(fighter1_name)
        st.write(fighter1_stats)
        st.subheader(fighter2_name)
        st.write(fighter2_stats)
        
        weight_class1 = fighter1_stats.iloc[0]["Weight Class"]
        weight_class1_avg = ufc_avg[ufc_avg["Weight Class"] == weight_class1].reset_index(drop=True)
        weight_class1_std = ufc_std[ufc_std["Weight Class"] == weight_class1].reset_index(drop=True)

        st.subheader(f"{weight_class1} Average Stats")
        st.write(weight_class1_avg)

        st.subheader(f"{weight_class1} Standard Deviations")
        st.write(weight_class1_std)
        
        display_fight_history(fighter1_name)
        display_fight_history(fighter2_name)
    else:
        st.write("Please enter valid fighter.")
