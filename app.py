import streamlit as st
import pandas as pd




#heading
st.write("""# Substraction of two numbers""")

#getting input
st.header('Number 1 - Number 2')

def substraction_of_Two_numbers():
  number_1 = st.number_input("Enter Number 1")
  number_2 = st.number_input("Enter Number 2")
  result   = (int(number_1) - int(number_2) )
  return result

st.write("The resultant number is "+ substraction_of_Two_numbers)



