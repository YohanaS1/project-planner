import streamlit as st
import database
header = st.container()

#making the tasks table
database.create_tasks_table()
#making list of tasks
tasks = database.get_tasks()
#turn into while loop then when button is clicked, set current project to that project on the button
if('selected_project' not in st.session_state or st.session_state['selected_project'] == "None"):
    st.warning("You didn't select a project. Please select a project below or go back to the dashboard and choose one", icon="⚠️")
    #back_button
    back_button = st.button("Back to Projects", key = "back_button")

    if back_button:
        st.session_state['selected_project'] = "None"
        st.switch_page("app.py")
        
    left, middle, right = st.columns(3)
    counter = 1
    projects = database.get_projects()
    for project in projects:
        if counter ==1:
            with left:
                #turn into button
                container = st.container(border = True, horizontal = True, horizontal_alignment = "distribute")
                if(container.button(project[1], key= f"choose_{project[0]}")):
                    st.session_state['selected_project'] = project[0]
                    st.rerun()
                
        elif counter ==2:
            with middle:
                #turn into button
                container = st.container(border = True, horizontal = True, horizontal_alignment = "distribute")
                if(container.button(project[1], key= f"choose_{project[0]}")):
                    st.session_state['selected_project'] = project[0]
                    st.rerun()
                
        else:
            with right:
                #turn into button
                container = st.container(border = True, horizontal = True, horizontal_alignment = "distribute")
                if(container.button(project[1], key= f"choose_{project[0]}")):
                    st.session_state['selected_project'] = project[0]
                    st.rerun()
                
        counter +=1
        if counter >3:
            counter = 1
else:
    #displaying header with project name and back button
    with header:
        col1, col2 = st.columns([5.5,1])
        project_name = database.get_project_name(st.session_state['selected_project'])

        col1.title(f"{project_name}",text_alignment = "center")

        back_button = col2.button("Back to Projects", key = "back_button")

        if back_button:
            st.session_state['selected_project'] = "None"
            st.switch_page("app.py")

    #storing tasks in session state
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

    #making the to do list submit form

    with st.form(key = "Add Task", clear_on_submit = True):
        
        task_name = st.text_input("Add a task")
        due_date = st.date_input("Add a due date")
        description = st.text_input("Add a description")
        submitted = st.form_submit_button("Submit")
        if submitted:
                if(task_name != ""):
                    st.success(f"task {task_name} added successfully!")
                    database.add_task(task_name, due_date, "Not Started", description)
                    st.rerun()
                else:
                    st.warning('Change task Name. Task name cannot be empty or duplicate', icon="⚠️")

    #displaying to do list
    to_do_list = st.container(border = True)

    with to_do_list:
        for task in tasks:
            to_do_list.write(task[1])
    #delete project section
    st.header(":red[Danger Zone]")
    understand = st.checkbox("I understand that this action cannot be undone", key = "understand_checkbox")
    delete_project = st.button("Delete Project", key = "delete_project", icon = "🗑️")
    if delete_project and understand:
        database.remove_project(st.session_state['selected_project'])
        st.session_state['selected_project'] = "None"
        st.success("Project deleted successfully!")
        st.rerun()
            
