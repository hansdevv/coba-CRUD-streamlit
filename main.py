# import streamlit as st
# from database.models import *
# # membuat koneksi ke database


# # membuat tabel jika belum ada


# # membuat tampilan web dengan Streamlit
# def main():
# 	st.title("CRUD Streamlit with SQLite3")
	
# 	# menu untuk menambahkan data
# 	if st.sidebar.button("Add User"):
# 			name = st.text_input("Name")
# 			email = st.text_input("Email")
# 			age = st.number_input("Age")
# 			add_user(name, email, age)
# 			st.success("User has been added!")
	
# 	# menu untuk melihat data
# 	if st.sidebar.button("View Users"):
# 			users = get_users()
# 			if len(users) > 0:
# 					for user in users:
# 							st.write("ID:", user[0])
# 							st.write("Name:", user[1])
# 							st.write("Email:", user[2])
# 							st.write("Age:", user[3])
# 							st.write("---")
# 			else:
# 					st.warning("No data found.")
	
# 	# menu untuk mengupdate data
# 	if st.sidebar.button("Update User"):
# 			id = st.number_input("Enter user ID:")
# 			name = st.text_input("Name")
# 			email = st.text_input("Email")
# 			age = st.number_input("Age")
# 			update_user(id, name, email, age)
# 			st.success("User has been updated!")
	
# 	# menu untuk menghapus data
# 	if st.sidebar.button("Delete User"):
# 			id = st.number_input("Enter user ID:")
# 			delete_user(id)
# 			st.success("User has been deleted!")
	
# 	# menutup koneksi database
# 	conn.close()

# if __name__ == '__main__':
#     main()


# import streamlit as st
# from deta import Deta
# from dotenv import load_dotenv
# import os

# load_dotenv()

# st.title("CRUD Streamlit with SQLite3")

# # Data to be written to Deta Base
# with st.form("form"):
#     name = st.text_input("Your name")
#     age = st.number_input("Your age")
#     submitted = st.form_submit_button("Store in database")

# # Connect to Deta Base with your Data Key
# # deta = Deta(st.secrets["KEY"])
# deta = Deta(os.getenv("KEY"))

# # Create a new database "example-db"
# # If you need a new database, just use another name.
# db = deta.Base("Coba_base")

# # If the user clicked the submit button,
# # write the data from the form to the database.
# # You can store any data you want here. Just modify that dictionary below (the entries between the {}).
# if submitted:
#     db.put({"name": name, "age": age})

# "---"
# "Here's everything stored in the database:"
# # This reads all items from the database and displays them to your app.
# # db_content is a list of dictionaries. You can do everything you want with it.
# db_content = db.fetch().items
# st.write(db_content)
# update = db.update({name: 'cobaUbah'},key='91a39v3e6pq5')
# update


import streamlit as st
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
def init_connection():
	# user = os.getenv("user")
	# host = os.getenv("host")
	# database = os.getenv("database")
	# password = os.getenv("password")
	user = st.secrets("user")
	host = st.secrets("host")
	database = st.secrets("database")
	# user = st.secrets("user")
	password = st.secrets("password")
	# return mysql.connector.connect(user=user,host=host,database=database,password=password)
	return mysql.connector.connect(host=host,database=database,password=password)
	# return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from orang;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
