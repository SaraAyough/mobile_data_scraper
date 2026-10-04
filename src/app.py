import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
        
        body, div, p, span, h1, h2, h3 {
            font-family: 'Vazirmatn', sans-serif !important;
            direction: rtl !important;
        }
        [data-testid="column"] {
            text-align: right;
        }
    </style>
""", unsafe_allow_html=True)


conn = sqlite3.connect("MobileProduct.db")
df = pd.read_sql("select * from MobileData", conn)
df2 = pd.read_sql("select * from MobileDetails", conn)

num_cols = 4
num_rows = (len(df) + num_cols - 1) // num_cols

for r in range(num_rows):
    row_container = st.container()
    with row_container:
        cols = st.columns(num_cols)
        for c in range(num_cols):
            item_index = r * num_cols + c
            if item_index < len(df):
                row = df.iloc[item_index]
                row2 = df2.iloc[item_index]
                with cols[c]:
                    st.image(row["image"])
                    st.write(row["title"])
                    st.write(row["price"])
                    st.write("رم:",row2["ram"])
                    st.write("حافظه داخلی:",row2["storage"])
                    st.write("رنگ:",row2["color"])
                    st.write("نمره کاربران:",row2["rating"])
                    st.link_button("View", row["link"])

    if r < num_rows - 1:
        st.markdown("<br>", unsafe_allow_html=True)
