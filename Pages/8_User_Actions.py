import streamlit as st
import mysql.connector as sql

# Function for coach actions
def coach_actions():
    st.subheader("Coach Actions")
    st.write("You can manage teams and players here.")

    action = st.selectbox("Select an action", ("Create Team", "List Teams", "Add Player to Team", "Edit/Delete Player", "Search Players"))

    if action == "Create Team":
        team_name = st.text_input("Enter Team Name")
        state = st.text_input("Enter State")
        district = st.text_input("Enter District")

        if team_name and state and district:
            # Connection parameters
            db_host = 'sportan-sportans.g.aivencloud.com'
            db_port = 10931
            db_user = 'avnadmin'
            db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
            db_name = 'defaultdb'

            try:
                # Establish a connection
                connection = sql.connect(
                    host=db_host,
                    port=db_port,
                    user=db_user,
                    passwd=db_password,
                    db=db_name
                )
                cursor = connection.cursor()
            except sql.Error as e:
                print(f"Error: {e}")

            # Insert the new team into the 'team' table
            cursor.execute("INSERT INTO teams (team_name, state, district) VALUES (%s, %s, %s)", (team_name, state, district))
            connection.commit()

            # Close the database connection
            cursor.close()
            connection.close()

            st.success("Team created successfully.")

    elif action == "List Teams":
            # Connection parameters
        db_host = 'sportan-sportans.g.aivencloud.com'
        db_port = 10931
        db_user = 'avnadmin'
        db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
        db_name = 'defaultdb'

        try:
            # Establish a connection
            connection = sql.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                passwd=db_password,
                db=db_name
            )
            cursor = connection.cursor()
        except sql.Error as e:
            print(f"Error: {e}")

        # Retrieve and display teams
        cursor.execute("SELECT * FROM teams")
        teams = cursor.fetchall()

        if teams:
            st.write("List of Teams:")
            for team in teams:
                st.write(f'''- Team ID: {team[0]}
                                     \n - Team Name: {team[1]}
                                     \n - State: {team[2]}
                                     \n - District: {team[3]}''')
                st.write("---")
        else:
            st.info("No teams found.")

        # Close the database connection
        cursor.close()
        connection.close()

    elif action == "Add Player to Team":
        team_name = st.text_input("Enter Team Name")
        player_name = st.text_input("Enter Player Name")
        role = st.text_input("Enter Player Role")
        contact = st.text_input("Enter Player Contact")
        email = st.text_input("Enter Player Email")

        if team_name and player_name and role and contact and email:
                    # Connection parameters
            db_host = 'sportan-sportans.g.aivencloud.com'
            db_port = 10931
            db_user = 'avnadmin'
            db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
            db_name = 'defaultdb'

            try:
                # Establish a connection
                connection = sql.connect(
                    host=db_host,
                    port=db_port,
                    user=db_user,
                    passwd=db_password,
                    db=db_name
                )
                cursor = connection.cursor()
            except sql.Error as e:
                print(f"Error: {e}")


            cursor.execute("SELECT * FROM players WHERE name = %s", (player_name,))
            player = cursor.fetchone()
            if player:
                # Check if the team exists
                cursor.execute("SELECT * FROM teams WHERE team_name = %s", (team_name,))
                team = cursor.fetchone()

                if team:
                    # Insert the new player into the 'players' table
                        cursor.execute("INSERT INTO t_players (name, role, contact_phone, contact_email) VALUES (%s, %s, %s, %s)", (player_name, role, contact, email))
                        connection.commit()
                        cursor.execute("Insert into team_player(team_id,player_id) values (%s,%s)",(team[0],player[0]))
                        connection.commit()
                        st.success("Player added to the team successfully.")
                        
                else:
                    st.error("Team not found. Please check the team name.")
            else:
                st.error("Player not Registered.")

            # Close the database connection
            cursor.close()
            connection.close()

    elif action == "Edit/Delete Player":
        st.warning("To be implemented.")

    elif action == "Search Players":
        search_option = st.selectbox("Search By", ("Team Name", "Player ID"))
        search_value = st.text_input("Enter Search Value")

        if search_option == "Team Name":
            # Search players by team name
            # Connection parameters
            db_host = 'sportan-sportans.g.aivencloud.com'
            db_port = 10931
            db_user = 'avnadmin'
            db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
            db_name = 'defaultdb'

            try:
                # Establish a connection
                connection = sql.connect(
                    host=db_host,
                    port=db_port,
                    user=db_user,
                    passwd=db_password,
                    db=db_name
                )
                cursor = connection.cursor()
            except sql.Error as e:
                print(f"Error: {e}")

            # Retrieve and display players based on team name
            query = 'SELECT * FROM players WHERE id IN (SELECT player_id FROM team_player WHERE team_id IN (SELECT id FROM teams WHERE team_name = %s))'
            
            cursor.execute(query,(search_value,))
            players = cursor.fetchall()

            if players:
                st.write("Players in Team:")
                for player in players:
                    
                    st.write(f'''- Player ID: {player[0]}
                                          \n- Player Name: {player[1]}
                                          \n- Email: {player[2]}''')
            else:
                st.info("No players found in the specified team.")

            # Close the database connection
            cursor.close()
            connection.close()
        elif search_option == "Player ID":
                    # Connection parameters
            db_host = 'sportan-sportans.g.aivencloud.com'
            db_port = 10931
            db_user = 'avnadmin'
            db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
            db_name = 'defaultdb'

            try:
                # Establish a connection
                connection = sql.connect(
                    host=db_host,
                    port=db_port,
                    user=db_user,
                    passwd=db_password,
                    db=db_name
                )
                cursor = connection.cursor()
            except sql.Error as e:
                print(f"Error: {e}")

            cursor.execute("SELECT * FROM t_players WHERE id IN (SELECT id FROM players WHERE id = %s)", (search_value,))
            players = cursor.fetchall()

            if players:
                st.write("Players in Team:")
                for player in players:
                    st.write(f"""- Player ID: {player[0]}
                             \n- Player Name: {player[1]}
                             \n- Role: {player[4]}
                             \n- Contact: {player[3]}
                             \n- Email: {player[2]}""")
            else:
                st.info("No players found in the specified team.")
                
# Function to send a request to join a team
def send_request_to_join_team():
    st.subheader("Send Request to Join a Team")
    team_name = st.text_input("Enter Team Name")
    submit_button = st.button("Send Request")

    if submit_button:
            # Connection parameters
        db_host = 'sportan-sportans.g.aivencloud.com'
        db_port = 10931
        db_user = 'avnadmin'
        db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
        db_name = 'defaultdb'

        try:
            # Establish a connection
            connection = sql.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                passwd=db_password,
                db=db_name
            )
            cursor = connection.cursor()
        except sql.Error as e:
            print(f"Error: {e}")

        # Check if the team exists
        cursor.execute("SELECT * FROM teams WHERE Team_Name = %s", (team_name,))
        team = cursor.fetchone()

        if not team:
            st.error("The team does not exist.")
        else:
            # Get the player's user ID (replace with actual user ID retrieval)
            name = st.text_input("Name")
            # Fetch teams for the user
            cursor.execute(" select id from users where name=%s",(name,))
            player_id=cursor.fetchone()

            # Check if the player has already sent a request to this team
            cursor.execute("SELECT * FROM player_requests WHERE team_id = %s AND player_id = %s", (team[0], player_id))
            existing_request = cursor.fetchone()

            if existing_request:
                st.warning("You have already sent a request to join this team.")
            else:
                # Send the request to join the team
                cursor.execute("INSERT INTO player_requests (team_id, player_id) VALUES (%s, %s)", (team[0], player_id))
                connection.commit()
                st.success("Request sent successfully. Wait for the coach's response.")

        # Close the database connection
        cursor.close()
        connection.close()

def player_actions():
    st.subheader("Player Actions")
    
    # List all teams the player is part of
    st.write("Press Submit if you want to see Which teams You Belong to")
    
    # Connection parameters
    db_host = 'sportan-sportans.g.aivencloud.com'
    db_port = 10931
    db_user = 'avnadmin'
    db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
    db_name = 'defaultdb'

    try:
        # Establish a connection
        connection = sql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        cursor = connection.cursor()
    except sql.Error as e:
        print(f"Error: {e}")

    # Fetch teams for the user
    user_id=st.session_state["Id"]
    if st.button("Submit"):
        cursor.execute("SELECT team_id FROM team_player WHERE player_id = %s", (user_id,))
        teams = cursor.fetchall()
    
        if teams:
            for team in teams:
                st.write(f"- {team[0]}")
        else:
            st.write("You are not part of any teams yet.")

    st.write("---")


    st.write("Explore Sports:")
    st.write("Here is some information about sports and their history:")
    st.write("1. Football: Football is a popular team sport that has a rich history...")
    st.write("2. Basketball: Basketball is a fast-paced sport that was invented by Dr. James Naismith in 1891...")
    st.write("3. Tennis: Tennis is a racket sport with origins dating back to the 12th century...")
    st.write("4. Swimming: Swimming is a water sport that has been part of the Olympic Games since their inception...")


    join_team = st.radio("Join a Team", ["Yes, I want to join a team", "No, I'm not interested"])

    if join_team == "Yes, I want to join a team":
            send_request_to_join_team()
    
    cursor.close()
    connection.close()

# Connection parameters
db_host = 'sportan-sportans.g.aivencloud.com'
db_port = 10931
db_user = 'avnadmin'
db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
db_name = 'defaultdb'

try:
    # Establish a connection
    connection = sql.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        passwd=db_password,
        db=db_name
    )
    cursor = connection.cursor()
except sql.Error as e:
    print(f"Error: {e}")

if "Login" not in st.session_state :
    st.session_state["Login"] = ""
    st.error("Please Login to Continue")
elif st.session_state["Login"]=="player":
        player_actions()
elif st.session_state["Login"]=="coach":
        coach_actions()
else :
    st.error("Please Login to Continue")


