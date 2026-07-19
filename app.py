
import streamlit as st

st.header("Project Planner")
st.write("to get started, add a project to the dashboard")

col1, col2, col3, col4 = st.columns(4)
total_tasks = 0
in_progress = 0
overdue = 0
completed = 0
col1.metric("Total Tasks", f"{total_tasks}")
col2.metric("In Progress", f"{in_progress}")
col3.metric("Overdue", f"{overdue}")
col4.metric("Completed", f"{completed}")

    






