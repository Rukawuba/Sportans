import streamlit as st
from datetime import date, time
import mysql.connector
from dotenv import load_dotenv
import os
import MySQLdb

# Function to add an event to the database
def search_event():
    # Connection parameters
    db_host = 'sportan-sportans.g.aivencloud.com'
    db_port = 10931
    db_user = 'avnadmin'
    db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
    db_name = 'defaultdb'

    try:
        # Establish a connection
        connection = MySQLdb.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        cursor = connection.cursor()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    Date=st.date_input(" Event Date " ,min_value=date.today())
    if Date:
        cursor.execute("Select * from schedule where event_date=%s",(Date,))
        events=cursor.fetchall()
        
    cursor.close()
    connection.close()

    return events
def add_event(event_type, event_date, event_time, location, description):
   # Connection parameters
    db_host = 'sportan-sportans.g.aivencloud.com'
    db_port = 10931
    db_user = 'avnadmin'
    db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
    db_name = 'defaultdb'

    try:
        # Establish a connection
        connection = MySQLdb.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        cursor = connection.cursor()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    # Insert the event into the database
    cursor.execute("INSERT INTO schedule (event_type, event_date, event_time, location, description) VALUES (%s, %s, %s, %s, %s)",
                   (event_type, event_date, event_time, location, description))

    
    connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()

# Function to retrieve all events from the database
def get_events():
    # Connection parameters
    db_host = 'sportan-sportans.g.aivencloud.com'
    db_port = 10931
    db_user = 'avnadmin'
    db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
    db_name = 'defaultdb'

    try:
        # Establish a connection
        connection = MySQLdb.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        cursor = connection.cursor()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    # Retrieve all events from the database
    cursor.execute("SELECT id, event_type, event_date, event_time, location, description FROM schedule")
    events = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    return events

def main():
    st.title('Event Scheduler')
    with st.sidebar:
        select=st.radio("Select an Option : ",["Add Event","See Events"])
    if select=="Add Event":
        st.subheader('Add Event')
        event_type = st.text_input('Event Type')
        event_date = st.date_input('Event Date', min_value=date.today())
        event_time = st.time_input('Event Time')
        location = st.text_input('Location')
        description = st.text_area('Description')

        if st.button('Add Event'):
            add_event(event_type, event_date, event_time, location, description)
            st.success('Event added successfully!')

    else:
        st.subheader('Scheduled Events')
        box=st.selectbox(" View ",("Search By Date" , "View all events"))

        if box=="Search By Date":
                events=search_event()
                if events:
                    for event in events:
                        st.write(f"Event ID: {event[0]}")
                        st.write(f"Event Type: {event[1]}")
                        st.write(f"Event Date: {event[2].strftime('%Y-%m-%d')}")
                        st.write(f"Event Time: {event[3]}")
                        st.write(f"Location: {event[4]}")
                        st.write(f"Description: {event[5]}")
                        st.write('---')
                else:
                    st.info('No events scheduled.')

        elif box=="View all events":
            events = get_events()

            if events:
                for event in events:
                    st.write(f"Event ID: {event[0]}")
                    st.write(f"Event Type: {event[1]}")
                    st.write(f"Event Date: {event[2].strftime('%Y-%m-%d')}")
                    st.write(f"Event Time: {event[3]}")
                    st.write(f"Location: {event[4]}")
                    st.write(f"Description: {event[5]}")
                    st.write('---')
            else:
                st.info('No events scheduled.')

if __name__ == '__main__':
    st.sidebar.write("Created with  ❤  by Team Sportans")
    
    main()
