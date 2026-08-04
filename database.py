import sqlite3

#defining a connection
connection = sqlite3.connect("project_planner.db")

#creating cursor
cursor = connection.cursor()

#method to create the projects table
def create_projects_table():
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name,
                    due_date,
                    status
                    )""")
    connection.commit()
    connection.close()

#method to create the materials table
def create_materials_table():
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS materials(
                    id,
                    name,
                    quantity,
                    purchased
                    )""")
    connection.commit()
    connection.close()

#method to create the inspiration table
def create_inspiration_table():
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inspiration(
                    id,
                    url,
                    note
                    )""")
    connection.commit()
    connection.close()

#method to create the tasks table
def create_tasks_table():
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name,
                    due_date,
                    status,
                    description
                    )""")
    connection.commit()
    connection.close()

#adding a project to database
def add_project(project_name):
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO projects (name) VALUES (?)",(project_name,))

    connection.commit()
    connection.close()

#getting all projects from the database
def get_projects():
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, name from projects")
    projects = cursor.fetchall()

    connection.close()
    return projects

#getting the name of a project by id
def get_project_name(project_id):
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()

    cursor.execute("SELECT name from projects WHERE id = ?", (project_id,))
    project_name = cursor.fetchone()

    connection.close()
    return project_name[0]

#remove project from the database
def remove_project(project_id):
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))

    connection.commit()
    connection.close()
    
def get_tasks():
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, name from tasks")
    tasks = cursor.fetchall()

    connection.close()
    return tasks

#adding a task to the database
def add_task(task_name,due_date, status, description):
    connection = sqlite3.connect("project_planner.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO tasks (name, due_date, status, description) VALUES (?,?,?,?)",(task_name, due_date, status, description))

    connection.commit()
    connection.close()


connection.commit()
connection.close()