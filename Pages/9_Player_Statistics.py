import streamlit as st
import mysql.connector

# Function to add player statistics to the database
def add_player_statistics(player_id, goals_scored, assists, other_metrics):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Reddy0314@",
        "database": "SSIP",
    }

    # Establish a database connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Insert player statistics into the database
    cursor.execute("INSERT INTO player_statistics (player_id, goals_scored, assists, other_metrics) VALUES (%s, %s, %s, %s)",
                   (player_id, goals_scored, assists, other_metrics))
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

# Function to retrieve player statistics from the database
def get_player_statistics(player_id):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Reddy0314@",
        "database": "SSIP",
    }

    # Establish a database connection
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Retrieve player statistics from the database
    cursor.execute("SELECT id, player_id, goals_scored, assists, other_metrics FROM player_statistics WHERE player_id = %s", (player_id,))
    player_stats = cursor.fetchall()

    # Close the database connection
    cursor.close()
    db.close()

    return player_stats

def main(user_role):
    if user_role == 'coach':
        st.subheader('Add Player Statistics')
        player_id = st.text_input('Player ID')
        points_scored = st.number_input('Points Scored', min_value=0)
        assists = st.number_input('Assists', min_value=0)
        other_metrics = st.text_area('Other Metrics')

        if st.button('Add Player Statistics'):
            add_player_statistics(player_id, points_scored, assists, other_metrics)
            st.success('Player statistics added successfully!')
    elif user_role == 'player':
        st.subheader('View Player Statistics')
        player_id_to_view = st.text_input('Player ID to view statistics')
    
        if st.button('View Player Statistics'):
            player_stats = get_player_statistics(player_id_to_view)

            if player_stats:
                for player_stat in player_stats:
                    st.write(f"ID: {player_stat[0]}")
                    st.write(f"Player ID: {player_stat[1]}")
                    st.write(f"Goals Scored: {player_stat[2]}")
                    st.write(f"Assists: {player_stat[3]}")
                    st.write(f"Other Metrics: {player_stat[4]}")
                    st.write('---')
            else:
                st.info('No player statistics available for the specified player.')
    else:
        st.error("Please Login to Continue ")

if __name__ == '__main__':
    st.sidebar.write("Created with  ❤  by Team Sportans")

    db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Reddy0314@",
    "database": "SSIP",
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    if "Login" not in st.session_state :
        st.session_state["Login"] = ""
        st.error("Please Login to Continue")
    else :
        user=st.session_state["Login"]
        main(user)
    
