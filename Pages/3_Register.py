import streamlit as st
from passlib.hash import sha256_crypt
import mysql.connector

# Function for user registration
def register(connection, cursor):
    st.subheader("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    role = st.selectbox("Role", ("coach", "player"))

    if st.button("Register"):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            st.error("User already exists. Please log in.")
        else:
            hashed_password = sha256_crypt.hash(password)
            cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", (name, email, hashed_password, role))
            connection.commit()
            cursor.close()
            st.success("Registration successful. You can now log in.")

# Function for user login
def login(connection, cursor):
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            hashed_password = user[3]  # Assuming 'password' is the fourth column
            if sha256_crypt.verify(password, hashed_password):
                st.success("Login successful")
                st.write(f"Welcome to Sportans , Mr/Mrs {user[1]}  !")
                st.write(f"Your {user[4]} Id is {user[0]}")

                st.session_state["Name"] = user[1]
                st.session_state["Login"] = user[4]
                st.session_state["Id"]=user[0]
                
                return user # Return the user record
            else:
                st.error("Invalid login. Please check your credentials.")
        else:
            st.error("User not found. Please register first.")
    return None

def main():
    st.sidebar.write("Created with  ❤  by Team Sportans")

    db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Reddy0314@",
    "database": "SSIP",
    }

    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    with st.sidebar:
        selected_option=st.radio("Select an Option",["Register","Login"])
    
    if selected_option=="Register":
        register(connection,cursor)
    else:
        user=login(connection,cursor)
        
    

if __name__ == "__main__":
    main()
