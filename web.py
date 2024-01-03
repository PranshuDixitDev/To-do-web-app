import streamlit as st
import functions
import time


def get_current_time():
    current_time = time.strftime("%d %b %Y, %H:%M:%S")
    return current_time


todos = functions.get_todos()
show_add_todo = st.empty()

selected_todo_index = -1


def edit_or_complete(todo_index):
    global selected_todo_index
    action = st.selectbox("Choose action:", ("Edit", "Complete"))
    if action == "Edit":
        edited_todo = st.text_input("Edit Todo", value=todos[todo_index])
        if st.button("Save"):
            todos[todo_index] = edited_todo + "\n"
            functions.write_todos(todos)
            selected_todo_index = -1
            st.rerun()
    elif action == "Complete":
        if st.button("Confirm"):
            del todos[todo_index]
            functions.write_todos(todos)
            selected_todo_index = -1
            st.rerun()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Task Master")
st.subheader(get_current_time())
st.write("This app is to increase your productivity.")

# Display checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        if selected_todo_index != -1 and selected_todo_index != index:
            st.warning("Please complete the current/first action before selecting another todo.")
            continue
        show_add_todo.empty()
        selected_todo_index = index
        edit_or_complete(index)

if selected_todo_index == -1:
    new_todo = st.text_input(label="Enter here", placeholder="Add new Todo...", on_change=add_todo, key="new_todo")
    show_add_todo.empty().write(new_todo)
