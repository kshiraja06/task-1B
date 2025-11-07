import pandas as pd
import streamlit as st

# app title
st.title("iyer’s ingredient list")

st.write("filter ingredients by group, nutritional focus, budget level, or a specific ingredient to build balanced monsoon-season meal plans for a bangalore-based vegetarian household.")

# load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('ingredients.csv')
    return df

df = load_data()

# sidebar filters
st.sidebar.header("filters")

category_filter = st.sidebar.multiselect(
    "group",
    options=df["category"].unique(),
    default=None
)

budget_filter = st.sidebar.multiselect(
    "budget level",
    options=df["budget_level"].unique(),
    default=None
)

benefit_search = st.sidebar.text_input("search by nutritional focus, ingredient, or use")

# filtering logic
filtered_df = df.copy()

if category_filter:
    filtered_df = filtered_df[filtered_df["category"].isin(category_filter)]

if budget_filter:
    filtered_df = filtered_df[filtered_df["budget_level"].isin(budget_filter)]

if benefit_search:
    filtered_df = filtered_df[
        filtered_df["nutritional_benefit"].str.contains(benefit_search, case=False, na=False) |
        filtered_df["used_for"].str.contains(benefit_search, case=False, na=False) |
        filtered_df["examples"].str.contains(benefit_search, case=False, na=False)
    ]

# display results
st.dataframe(filtered_df, use_container_width=True)

