import streamlit as st
import mysql.connector

def send_feedback(name, user_message):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Reddy0314@",
        "database": "SSIP",
    }

    # Establish a database connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    query='select * from Users where name="%s"'%(name)
    user_id=cursor.fetchone()[0][0]
    # Store the user's feedback in the database
    cursor.execute("INSERT INTO Feedback (user_id,name, content) VALUES (%s, %s)", (user_id,name, user_message))
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

    return True

# Function to embed user guides and video tutorials
def display_user_guides():
    st.header("User Guides and Tutorials")

    # Getting Started Guide
    st.subheader("Getting Started Guide")
    st.write("Welcome to our sports management system. Here's how to get started:")
    st.write("1. **Create an account** if you're a new user. You can register as either a coach or a player.")
    st.write("2. **Log in with your credentials**. Use your registered email and password to access the system.")
    st.write("3. **Explore the dashboard** to navigate and utilize the system's features.")

    st.write("---")
    
    # Frequently Asked Questions (FAQ)
    st.header("Frequently Asked Questions (FAQ)")
    st.subheader("Got questions? Check our FAQ section for answers.")
    st.text("")
    st.text("")

    # Create two columns
    col1, _ ,col2 = st.columns([1,0.5,1])

    with col1:
        st.write("1. **How do I add a player to my team?**")
        st.write("   - To add a player to your team, log in as a coach.")
        st.write("   - Navigate to the 'Team Management' section.")
        st.write("   - Click 'Add Player' and provide the player's details.")
        st.text("")  # Add spacing between items 1 and 3
        st.text("")  
        st.write("3. **Where can I view player statistics?**")
        st.write("   - To view player statistics, navigate to the 'Player Statistics' section.")
        st.write("   - Select the player you want to view stats for.")


    
    with col2:
        st.write("2. **Can I edit an event in the schedule?**")
        st.write("   - Yes, as a coach, you can edit events in the schedule.")
        st.write("   - Go to the 'Schedule' section, find the event, and click 'Edit'.")
        st.text("")  # Add spacing between items 2 and 4
        st.text("")
        st.text("")
        st.text("")
        st.write("4. **How do I request to join a team as a player?**")
        st.write("   - If you're a player looking to join a team, you can send a request to a coach.")
        st.write("   - Navigate to the 'Player Requests' section and send a request to the coach of the team you're interested in.")

    st.write("---")
    # Feedback
    st.subheader("Feedback")
    st.write("Have a question, suggestion, or need assistance? Send us a message below:")
    name = st.text_input("Name")
    user_message = st.text_area("Your Message")

    
    if st.button("Send Feedback"):
        if name and user_message:
            result = send_feedback(name, user_message)
            if result is True:
                st.success("Your feedback has been submitted! Thank you for your input.")
            else:
                st.error(f"Failed to send the feedback.")
        else:
            st.warning("Please enter your feedback before submitting.")

    

# Main Streamlit app
def main():
    st.title("Sports Management System")
    st.sidebar.write("Created with  ❤  by Team Sportans")

    st.sidebar.write("Please explore user guides and tutorials.")

    # Display user guides and tutorials
    display_user_guides()

if __name__ == "__main__":
    main()
