import pandas as pd
import streamlit as st

# app title
st.title("namma monsoon market — ingredient filter")

st.write("explore seasonal, budget-friendly vegetarian ingredients available in bangalore during june–july.")
st.caption("data sourced from kr market, dmart, local vendors, and verified regional produce lists.")

# load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('ingredients.csv')
    return df

df = load_data()

# sidebar filters
st.sidebar.header("filter options")

category_filter = st.sidebar.multiselect(
    "filter by category",
    options=df["category"].unique(),
    default=None
)

budget_filter = st.sidebar.multiselect(
    "filter by budget level",
    options=df["budget_level"].unique(),
    default=None
)

benefit_search = st.sidebar.text_input("search by nutritional benefit or use keyword")

# filtering logic
filtered_df = df.copy()

if category_filter:
    filtered_df = filtered_df[filtered_df["category"].isin(category_filter)]

if budget_filter:
    filtered_df = filtered_df[filtered_df["budget_level"].isin(budget_filter)]

if benefit_search:
    filtered_df = filtered_df[
        filtered_df["nutritional_benefit"].str.contains(benefit_search, case=False, na=False) |
        filtered_df["used_for"].str.contains(benefit_search, case=False, na=False)
    ]

# display results
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.subheader("summary")
st.write(f"**total items:** {len(filtered_df)}")
st.write("use the filters on the left to narrow down ingredients by category, budget, or nutritional goal.")
