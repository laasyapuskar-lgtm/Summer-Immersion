import streamlit as st

st.title("Welcome App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age", 0, 100, 18)
st.write(f"Selected Age: {age}")

if st.button("Celebrate"):
    st.balloons()
    st.success("🎉 Celebration Time!")