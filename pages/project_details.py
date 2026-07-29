import streamlit as st

header = st.container()

with header:
    col1, col2 = st.columns([5.5,1])

    col1.title(f"{st.session_state['selected_project']}",text_alignment = "center")

    back_button = col2.button("Back to Projects", key = "back_button")

    if back_button:
        st.session_state['selected_project'] = "None"
        st.switch_page("app.py")