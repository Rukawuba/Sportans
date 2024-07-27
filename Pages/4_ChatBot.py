import streamlit as st
import google.generativeai as genai


# Streamlit page configuration
st.set_page_config(page_title="Sporta Bot", layout="wide")
with st.sidebar :
    st.write("Created with  ❤  by Team Sportans")
    u_choice = st.radio("""Choose the Interactivity Level : 
             If you Want to Gain Knowledge about Sports and Skills , Choose Sporta Bot
             If you want to learn Specific skill only Choose our Sporta Coach""" , ["Sporta Coach","Sporta Bot"])

# Configure Google Generative AI API
genai.configure(api_key="AIzaSyAz2-s0Ti5Qf6G7wcKgg9iaqJ4-_b9vjbE")

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

st.header("Welcome to Sporta Bot: Your Personalized Sports Coach and Caretaker!")

if u_choice == "Sporta Bot" :

        def start_chat():
            return model.start_chat(history=[])

        def get_response(question, chat):
            response = chat.send_message(question, stream=True)
            return response

        def get_conversational_chain(username, chat):
            prompt_template = f"""
            You are now Sporta Coach, an empathetic and insightful coach who not only provides training advice but also cares deeply about the well-being of the athletes and coaches you assist. Your approach should be interactive, encouraging the user to share more about their background, goals, and any concerns they may have. The user's name will be enclosed in {{}}.

            When a user asks a question, follow these steps:

            1. **Greet the user by name warmly and show genuine interest in their journey.**
            2. **Ask open-ended questions to understand the user's background, goals, and current situation.**
            3. **Based on their responses, provide tailored advice, blending technical guidance with motivational support.**
            4. **Encourage further dialogue, inviting the user to ask more questions or share more details.**
            5. **Reiterate important points, ensuring the user feels heard and supported.**

            Example Interaction:

            **User's Question:** 
            "Can you help me plan a training schedule for running a 5k?"

            **Sporta Bot:**
            "Hello {{username}}! It's great to see your enthusiasm for running a 5k. Before we dive into the schedule, could you share a bit about your running experience and what inspired you to take on this challenge?"

            **User's Input:**
            "I've been running casually, about 2-3 times a week, but nothing structured. I wanted to set a goal to stay motivated."

            **Sporta Bot:**
            "That's a fantastic goal, {{username}}! Setting structured goals is a great way to stay motivated and make progress. It sounds like you have a good base. Let's start by establishing a steady routine. How do you feel about running three times a week, gradually increasing your distance? Also, how do you currently feel during your runs? Any areas you'd like to focus on or improve?"

            **User's Input:**
            "I sometimes feel tired quickly, especially on longer runs."

            **Sporta Bot:**
            "I understand, {{username}}. It's important to pace yourself and listen to your body, especially as you're building endurance. Starting with shorter, manageable distances and then gradually increasing will help. We can also incorporate rest days and lighter activities to keep your energy up. Do you also focus on nutrition and hydration? These can make a big difference in how you feel during your runs."

            **Encouragement:**
            "You're doing amazing, {{username}}! Taking on a 5k is a wonderful journey, and with each step, you're building not just physical strength but mental resilience too. Remember, every runner started where you are now. Let's keep this dialogue open—if you ever have questions or just need some encouragement, I'm here for you. Let's achieve this together!"
            
            Let's start with a greeting.
            User: {username}
            """

            response = chat.send_message(prompt_template)
            return response.text

        # Streamlit app logic
        if "Login" not in st.session_state or not st.session_state["Login"]:
            st.error("Please Login to Continue")
        else:

            if 'chat_history' not in st.session_state:
                st.session_state['chat_history'] = []
                st.session_state['chat'] = start_chat()

            user = st.session_state["Name"]

            if not st.session_state['chat_history']:
                greeting_response = get_conversational_chain(user, st.session_state['chat'])
                st.session_state['chat_history'].append(("Coach", greeting_response))
            
            input_text = st.text_input("Input:", key="input")
            submit = st.button("GO!!")

            if input_text and submit:
                response = get_response(input_text, st.session_state['chat'])
                st.session_state['chat_history'].append(("You", input_text))
                st.subheader("Output")
                for chunk in response:
                    st.write(chunk.text)
                    st.session_state['chat_history'].append(("Coach", chunk.text))

            
            st.write("---")
            
            st.subheader("Chat History")
            for role, text in st.session_state['chat_history']:
                st.write(f"{role}: {text}")

else :
        # Function to collect user responses
        def collect_user_responses():
            st.write("Answer a few questions to help us tailor your training and coaching experience.")

            # Predefined questions with creative interaction
            sports_options = ["Football", "Basketball", "Tennis", "Cricket", "Running", "Swimming", "Other"]
            sport = st.selectbox("Which sport do you want to focus on?", sports_options)
            
            skill = st.text_input(f"What specific skill in {sport} are you aiming to develop or improve?")
            
            level_options = ["Beginner", "Intermediate", "Advanced"]
            level = st.selectbox(f"What's your current proficiency level in {skill}?", level_options)
            
            training_frequency = st.slider("How many days a week are you training or practicing?", 0, 7, 3)
            
            goal = st.text_input("What's your primary goal with this sport? (e.g., improve stamina, master techniques, compete professionally)")
            
            challenges = st.text_area("What challenges are you currently facing in reaching your goals?")
            
            specific_request = st.text_area("Do you have any specific requests or areas you'd like to focus on? (Optional)")

            if st.button("Get Personalized Plan"):
                chat = start_chat()
                response = get_conversational_chain("User", sport, skill, level, training_frequency, goal, challenges, specific_request, chat)
                generate_output(response)

        def start_chat():
            return model.start_chat(history=[])

        def get_response(question, chat):
            response = chat.send_message(question, stream=True)
            return response

        def get_conversational_chain(username, sport, skill, level, training_frequency, goal, challenges, specific_request, chat):
            prompt_template = f"""
    You are a friendly and helpful assistant dedicated to helping athletes and coaches. You should act as a coach and caretaker, providing guidance and support. Ask the user for their input and understand their background before providing tailored advice. Here are the user's details:

    - Sport: {sport}
    - Skill: {skill}
    - Level: {level}
    - Training Frequency: {training_frequency} times per week
    - Goal: {goal}
    - Challenges: {challenges}
    - Specific Request: {specific_request}

    Please respond with a motivational and personalized coaching plan for {username} based on these details.
    """

            response = chat.send_message(prompt_template)
            return response
        def generate_output(response):

            st.subheader("Your Personalized Coaching Plan")
            for chunk in response:
                st.write(chunk.text)

        # Streamlit app logic
        if "Login" not in st.session_state or not st.session_state["Login"]:
            st.error("Please Login to Continue")
        else:
            collect_user_responses()

