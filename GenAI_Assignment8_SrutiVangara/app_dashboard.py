import streamlit as st
st.title("Simple Sales Dashboard")
st.write("View monthly sales")
month = ["January","February","March","April"]
sales = {"January":1200,"February":1500,"March":900,"April":2000}
selected_month = st.selectbox("Select a month",month)
st.metric("Selected month sales:",sales[selected_month])
st.subheader("Montly sales chart")
st.bar_chart(list(sales.values()))