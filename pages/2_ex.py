import streamlit as st

st.title("Learn Streamlit")

if "count" not in st.session_state:
    st.session_state.count = 0

st.write(f"Count: {st.session_state.count}")
if st.button("Increase count"):
    st.session_state.count += 1

problem1, problem2 = st.tabs(["Problem 1", "Problem 2"])

with problem1:
    st.subheader("1. Expand the expression")
    st.latex(r"(x+y)^2")

    with st.form("forms1"):
        answer1 = st.radio(
            "Choose the expanded expression.",
            [r"$x^2+y^2$", r"$x^2+xy+y^2$", r"$x^2+2xy+y^2$", r"$2x^2+2y^2$"],
            index=None,
        )
        submit_button1 = st.form_submit_button("Submit")

    if submit_button1:
        if answer1 is None:
            st.warning("Choose an answer before submitting.")
        elif answer1 == r"$x^2+2xy+y^2$":
            st.write("Correct!")
        else:
            st.write("Try using the distributive property and calculate again.")

with problem2:
    with st.form("forms2"):
        answer2 = st.radio(
            "Which turtle is the fastest?",
            ["Turtle A", "Turtle B", "Turtle C", "Turtle D"],
            index=None,
        )
        submit_button2 = st.form_submit_button("Submit")

    if submit_button2:
        if answer2 is None:
            st.warning("Choose an answer before submitting.")
        elif answer2 == "Turtle A" or answer2 == "Turtle B":
            st.write("Think again about what it means to be the fastest.")
        elif answer2 == "Turtle C":
            st.write("Speed can depend on the starting position and pace.")
        else:
            st.write("Correct!")
