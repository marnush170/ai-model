import streamlit as st
from sympy import symbols, Eq, solve, sympify

st.set_page_config(page_title="Algebra Solver", page_icon="🧠")

st.title("🧮 AI Algebra Solver")
st.write("Enter a linear algebra equation like `2x + 3 = 7` to solve for x.")

# Input from user
user_input = st.text_input("Equation (solve for x):", value="2x + 3 = 7")

x = symbols('x')

if user_input:
    try:
        # Split and parse
        lhs, rhs = user_input.split('=')
        eq = Eq(sympify(lhs.strip()), sympify(rhs.strip()))
        
        # Solve
        solution = solve(eq, x)
        
        st.success(f"✅ Solution: x = {solution[0]}")
    except Exception as e:
        st.error(f"❌ Could not solve the equation. Error: {str(e)}")