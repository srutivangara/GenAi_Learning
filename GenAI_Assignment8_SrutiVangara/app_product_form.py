import streamlit as st
pro_name = st.sidebar.text_input("Enter product name: ")
category = st.sidebar.selectbox("Cateory",["Electronics","Clothing","Books","Food","Other"])
price = st.sidebar.number_input("Enter Price:")
if st.sidebar.button("Add Product"):
    st.success("Product added successfully")
    st.subheader("Product Details")
    st.write(f"Product name: {pro_name} | Category: {category}  | Price: {price}\n")
