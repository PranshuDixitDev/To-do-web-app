import streamlit as st
import functions
import time


def get_current_time():
    current_time = time.strftime("%d %b %Y, %H:%M:%S")
    return current_time


todos = functions.get_todos()
show_add_todo = st.empty()


def edit_or_complete(todo_index):
    action = st.selectbox("Choose action:", ("Edit", "Complete"))
    if action == "Edit":
        edited_todo = st.text_input("Edit Todo", value=todos[todo_index])
        if st.button("Save"):
            todos[todo_index] = edited_todo + "\n"
            functions.write_todos(todos)
            st.rerun()
    elif action == "Complete":
        if st.button("Confirm"):
            del todos[todo_index]
            functions.write_todos(todos)
            st.rerun()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Task Master")
st.subheader(get_current_time())
st.write("This app is to increase your productivity.")

checkboxes = []
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo)
    checkboxes.append(checkbox)
    if checkboxes[index]:
        show_add_todo.empty()
        edit_or_complete(index)

if not any(checkboxes):
    new_todo = st.text_input(label="Enter here", placeholder="Add new Todo...", on_change=add_todo, key="new_todo")
    show_add_todo.empty().write(new_todo)
