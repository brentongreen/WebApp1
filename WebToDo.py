import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("My Web App")
st.subheader("My to do list")
st.write("Enter Items")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=index)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label="",key="new_todo",placeholder="Enter data",on_change=add_todo)
