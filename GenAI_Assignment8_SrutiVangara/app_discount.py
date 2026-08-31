import streamlit as st
price = st.number_input("Enter product price: ")
discount_percentage = st.slider("Select Discount(%): " ,0,50)
if st.button("Calculate discount price"):
    dis_price = price - (price*discount_percentage/100)
    st.success(f"Discounted Price: {dis_price:.2f}")
    st.table({"Before": [f"{price:.2f}"],"After":[f"{dis_price:.2f}"]})