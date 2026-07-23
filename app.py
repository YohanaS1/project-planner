
import streamlit as st

st.header("Project Planner")
st.write("to get started, add a project to the dashboard")
if 'projects' not in st.session_state:
    st.session_state['projects']=[]
col1, col2, col3, col4 = st.columns(4)
total_tasks = 0
in_progress = 0
overdue = 0
completed = 0
col1.metric("Total Tasks", f"{total_tasks}")
col2.metric("In Progress", f"{in_progress}")
col3.metric("Overdue", f"{overdue}")
col4.metric("Completed", f"{completed}")
with st.form(key = "Add Project", clear_on_submit=True):
    project_name = st.text_input("Project Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if(project_name != ""):
            st.success(f"Project {project_name} added successfully!")
            st.session_state.projects.append(project_name)
        else:
            st.warning('Project name cannot be empty!', icon="⚠️")

for project in st.session_state.projects:
    with st.container():
        st.write(f"Project: {project}")



        




