import streamlit as st
import Plan 
st.set_page_config(page_title="My App")
st.header("Diet Plan")
# st.balloons()
Name = st.text_input("Enter your name :")
age = st.text_input("Enter your age ")
height = st.text_input("Enter your height")
weight = st.number_input("Enter your weight")


choise = st.selectbox('Select option ',['select','Generate Diet Plan','Health calculate'])

if choise == 'Generate Diet Plan':
    st.text("What is your purpose?")
    pur = st.text_area("Purpose",)
       



str = st.button(label='Submit', key="submit")
if str:
    if choise == 'Generate Diet Plan':
        result = Plan.plan(age=age,height=height,weight=weight,purpose=pur)
    if choise == 'Health calculate':
        result = Plan.call(age=age,height=height,weight=weight)
        st.write(result)