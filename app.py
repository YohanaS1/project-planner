import streamlit as st
import database
# Header
st.header("Project Planner")
st.write("to get started, add a project to the dashboard")
#creating projects table
database.create_projects_table()

#getting all projects from the database
projects = database.get_projects()

#creating columns for metrics
col1, col2, col3, col4 = st.columns(4)
st.write()
#project submit form
with st.form(key = "Add Project", clear_on_submit=True):
    name_of_project = st.text_input("Project Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if(name_of_project == "" or name_of_project in [project[1] for project in projects]):
            st.warning('Change project Name. Project name cannot be empty or duplicate', icon="⚠️")
        else:
            database.add_project(name_of_project)
            st.success(f"Project {name_of_project} added successfully!")
            st.rerun()

#progress metrics
total_projects = len(projects)
in_progress = 0
overdue = 0
completed = 0
col1.metric("Total Projects", f"{total_projects}")
col2.metric("In Progress", f"{in_progress}")
col3.metric("Overdue", f"{overdue}")
col4.metric("Completed", f"{completed}")
# saving selected project to session state
if 'selected_project' not in st.session_state:
    st.session_state['selected_project']= "None"

#displaying projects
left, middle, right = st.columns(3)
counter = 1
for project in projects:
    if counter ==1:
        with left:
            container = st.container(border = True, horizontal = True, horizontal_alignment = "distribute")
            container.write(project[1])
            edit_clicked = container.button('',key = f"edit_{project[0]}",icon="✏️", icon_position = "right", width = 50)
            # check if edit button is clicked
            if edit_clicked:
                st.session_state['selected_project'] = project[0]
                st.switch_page("pages/project_details.py")

            
    elif counter ==2:
        with middle:
            container = st.container(border = True, horizontal = True, horizontal_alignment = "distribute")
            container.write(project[1])
            edit_clicked = container.button('',key = f"edit_{project[0]}",icon="✏️", icon_position = "right", width = 50)
            # check if edit button is clicked
            if edit_clicked:
                st.session_state['selected_project'] = project[0]
                st.switch_page("pages/project_details.py")
            
    else:
        with right:
            container = st.container(border = True, horizontal = True, horizontal_alignment = "distribute")
            container.write(project[1])
            edit_clicked = container.button('',key = f"edit_{project[0]}",icon="✏️", icon_position = "right", width = 50)
            # check if edit button is clicked
            if edit_clicked:
                st.session_state['selected_project'] = project[0]
                st.switch_page("pages/project_details.py")
    counter +=1
    if counter >3:
        counter = 1


        




