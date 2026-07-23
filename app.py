
import streamlit as st
# Header
st.header("Project Planner")
st.write("to get started, add a project to the dashboard")

#storing projects in session state
if 'projects' not in st.session_state:
    st.session_state['projects']=[]
#creating colums for metrics
col1, col2, col3, col4 = st.columns(4)
#project submit form
with st.form(key = "Add Project", clear_on_submit=True):
    project_name = st.text_input("Project Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if(project_name != ""):
            st.success(f"Project {project_name} added successfully!")
            st.session_state.projects.append(project_name)
        else:
            st.warning('Project name cannot be empty!', icon="⚠️")

#progress metrics
total_projects = len(st.session_state.projects)
in_progress = 0
overdue = 0
completed = 0
col1.metric("Total Projects", f"{total_projects}")
col2.metric("In Progress", f"{in_progress}")
col3.metric("Overdue", f"{overdue}")
col4.metric("Completed", f"{completed}")

#displaying projects
left, middle, right = st.columns(3)
counter = 1
for project in st.session_state.projects:
    if counter ==1:
        with left:
            container = st.container(border = True)
            container.write(project)
    elif counter ==2:
        with middle:
            container = st.container(border = True)
            container.write(project)
    else:
        with right:
            container = st.container(border = True)
            container.write(project)
    counter +=1
    if counter >3:
        counter = 1
        



        




