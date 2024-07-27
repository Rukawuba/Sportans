import streamlit as st
from datetime import date, time
import mysql.connector

# Function to add an event to the database
def search_event():
    db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Reddy0314@",
            "database": "SSIP",
        }

    # Establish a database connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    Date=st.date_input(" Event Date " ,min_value=date.today())
    if Date:
        cursor.execute("Select * from schedule where event_date=%s",(Date,))
        events=cursor.fetchall()
        
    cursor.close()
    db.close()

    return events
def add_event(event_type, event_date, event_time, location, description):
    db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Reddy0314@",
            "database": "SSIP",
        }

    # Establish a database connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Insert the event into the database
    cursor.execute("INSERT INTO schedule (event_type, event_date, event_time, location, description) VALUES (%s, %s, %s, %s, %s)",
                   (event_type, event_date, event_time, location, description))

    
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

# Function to retrieve all events from the database
def get_events():
    db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Reddy0314@",
            "database": "SSIP",
        }

    # Establish a database connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Retrieve all events from the database
    cursor.execute("SELECT id, event_type, event_date, event_time, location, description FROM schedule")
    events = cursor.fetchall()

    # Close the database connection
    cursor.close()
    db.close()

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
