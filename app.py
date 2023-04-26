import streamlit as st
import pandas as pd
import random

pd.set_option('display.max_columns', None)
fighters_altered = pd.read_csv("fighters_altered_updated.csv")
pure_stat = pd.read_csv("Pure_Stat.csv")
averages = pd.read_csv("averages.csv")

def main():
    st.title("MMA Statistics App")

    single_fighter()
    st.header("Compare Fighters")
    compare_fighters()
    st.header("Random Fighter")
    random_fighter()
    st.header("Weight Class Averages")
    weight_class_averages()

def single_fighter():
    st.title("Single Fighter")
    name = st.text_input("Enter fighter's name:")
    if name:
        fighter_data = fighters_altered[fighters_altered["Name"] == name]
        fight_data = pure_stat[(pure_stat["Fighter 1"] == name) | (pure_stat["Fighter 2"] == name)]
        if not fighter_data.empty:
            st.write(fighter_data)
            st.write(fight_data)
        else:
            st.warning("No data found for the entered fighter's name.")

def compare_fighters():
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
    if st.button("Generate Random Fighter"):
        random_name = random.choice(fighters_altered["Name"].values)
        fighter_data = fighters_altered[fighters_altered["Name"] == random_name]
        fight_data = pure_stat[(pure_stat["Fighter 1"] == random_name) | (pure_stat["Fighter 2"] == random_name)]
        st.write(fighter_data)
        st.write(fight_data)

def weight_class_averages():
    st.write(averages)

if __name__ == "__main__":
    main()