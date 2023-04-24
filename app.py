import streamlit as st
import pandas as pd
import random
fighters_altered = pd.read_csv("fighters_altered.csv")
pure_stat = pd.read_csv("Pure_Stat.csv")
averages = pd.read_csv("averages.csv")
def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("Go to:", ["Home", "Single Fighter", "Compare Fighters", "Random Fighter", "Weight Class Averages"])

    if tab == "Home":
        st.title("Welcome to the MMA Statistics App!")
        st.write("Please use the sidebar to navigate between different sections of the app.")
    elif tab == "Single Fighter":
        single_fighter()
    elif tab == "Compare Fighters":
        compare_fighters()
    elif tab == "Random Fighter":
        random_fighter()
    elif tab == "Weight Class Averages":
        weight_class_averages()

if __name__ == "__main__":
    main()
def single_fighter():
    st.title("Single Fighter")
    name = st.text_input("Enter fighter's name:")
    if name:
        fighter_data = fighters_altered[fighters_altered["Name"] == name]
        fight_data = pure_stat[pure_stat["Name"] == name]
        if not fighter_data.empty:
            st.write(fighter_data)
            st.write(fight_data)
        else:
            st.warning("No data found for the entered fighter's name.")

def compare_fighters():
    st.title("Compare Fighters")
    name1 = st.text_input("Enter first fighter's name:")
    name2 = st.text_input("Enter second fighter's name:")

    if name1 and name2:
        fighter1_data = fighters_altered[fighters_altered["Name"] == name1]
        fighter2_data = fighters_altered[fighters_altered["Name"] == name2]

        if not fighter1_data.empty and not fighter2_data.empty:
            st.write("Fighter 1:")
            st.write(fighter1_data)
            st.write("Fighter 2:")
            st.write(fighter2_data)
        else:
            st.warning("No data found for one or both of the entered fighter's names.")

def random_fighter():
    st.title("Random Fighter")
    if st.button("Generate Random Fighter"):
        random_name = random.choice(fighters_altered["Name"].values)
        fighter_data = fighters_altered[fighters_altered["Name"] == random_name]
        fight_data = pure_stat[pure_stat["Name"] == random_name]
        st.write(fighter_data)
        st.write(fight_data)

def weight_class_averages():
    st.title("Weight Class Averages")
    st.write(averages)
