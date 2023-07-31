import streamlit
import functions

todos = functions.read_todo(r'todos.txt')


def add_todo():
    new_todo = streamlit.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    functions.write(todos, r'todos.txt')


streamlit.title('My todo app')
keys = 1
for todo in todos:
    checkbox = streamlit.checkbox(label=todo, key=keys)
    if checkbox:
        todos.pop(keys - 1)
        functions.write(todos, r'todos.txt')
        del streamlit.session_state[keys]
        streamlit.experimental_rerun()
    keys = keys + 1


streamlit.text_input(label=' ', placeholder='Enter a new todo', on_change=add_todo, key='new_todo')
