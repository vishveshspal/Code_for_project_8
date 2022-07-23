import streamlit as st



st.header('Number 1 - Number 2')

def substraction_of_Two_numbers():
  

  Number_1 = st.number_input("n_1")
  Number_2 = st.number_input("n_2")


  result = int(Number_1)-int(Number_2)



  return result



result= substraction_of_Two_numbers()




st.write('The resulting number is '+ str(result))



