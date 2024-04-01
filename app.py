import streamlit as st
from factorial import factorial


def main():
    st.title("Factorial Calcutator")
    number = st.number_input("Insert the number you want to calculate factorial", min_value =  0, max_value = 900, step = 1, placeholder="Type a number..." )
    if st.button("Calculate"):
        result = factorial(number)
        st.write(f"The Factorial of {number} is : {result}")
        st.balloons()

if __name__ == "__main__":
    main()


