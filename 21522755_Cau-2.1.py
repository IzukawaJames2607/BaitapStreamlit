import streamlit as st

st.title("Calculator for Sum, Difference, Product and Quotient")
number1 = st.number_input('First number', value=0.0, step=0.01)
number2 = st.number_input('Second number', value=0.0, step=0.01)

sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
if number2 != 0:
    quotient_result = number1 / number2
else:
    quotient_result = "undefined (cannot divide by zero)"

st.write(f"Sum: {sum_result}")
st.write(f"Difference: {difference_result}")
st.write(f"Product: {product_result}")
st.write(f"Quotient: {quotient_result}")

if st.button("Reset"):
    number1 = 0.0
    number2 = 0.0
    st.experimental_rerun()