import streamlit as st



st.session_state["Name"] = ""
st.session_state["Login"] = ""
st.session_state["Id"]= ""

# Set a title for your site
col1,col4,col2,col3=st.columns([1,0.3,5,2])
with col1:
     st.image(".\images\logo.png")

with col2:
     st.write(" ")
     st.write(" ")
     st.header("Meet the Sportans")

st.text(" ")
st.text("")

# Add an introduction
st.write(
    "Welcome to Sportans, where our passion is to simplify the complexities of "
    "sports management. We've designed a platform that caters to everyone involved in sports, "
    "be it a dedicated coach, an efficient team manager, or a determined athlete. Our mission is "
    "to make the management of sports teams and individual performance efficient, organized, and data-driven."
    " "
    "At Sportan, we're committed to enhancing the way you train, communicate, "
    "and analyze performance. We understand the unique challenges you face in the world of "
    "sports, and our platform is meticulously crafted to address these challenges. Our goal is to "
    "free up your time and energy, allowing you to focus on what truly matters: winning games and achieving your athletic ambitions."
)

st.write( '''In the realm of sports management, we're redefining how sports are managed and experienced. Sportan is here to make the lives of coaches, team managers, and athletes easier. We believe in simplifying the intricacies of sports management by providing tools that enhance training regimens, improve communication, and offer data-driven insights into performance. Inclusivity is at the core of our platform, making it accessible and welcoming for all sports enthusiasts. Our data-driven approach empowers you to make informed decisions, whether you're tracking performance metrics or managing player injuries. Your success is our utmost priority, and we're dedicated to being your partner on your journey toward athletic excellence. Join us today to experience the future of sports management with Sportans, where we're committed to streamlining your sports experience.''')

st.write("---")
# Explain why the website was built
col1,_,col2=st.columns([5,0.3,3])

with col1:
     st.header("Why Sportan ?")
     st.write(
    "In the fast-paced world of sports, effective management can make all the difference.  "
    "Whether you're a coach, a team manager, or an athlete, Sports Management Hub is here to "
    "revolutionize the way you experience and interact with sports. Here are the core reasons why "
    "we exist and why we believe Sports Management Hub is the future of sports management : "
     )

     st.markdown("1. Streamlined Efficiency")
     st.markdown("2. Inclusivity for All")
     st.markdown("3. Data-Driven Excellence")
     st.markdown("4. Simplifying Challenges")
     st.markdown("5. Your Success is Our Success")

     st.write("---")
     
with col2:
     st.write(" ")
     st.write(" ")
     st.image(".\images\choose.png",width=300)

st.header("Why we're Better")

# Column 3: Competitive Analysis
col3,col1=st.columns(2)
with col3:
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.image(".\images\compete.png")

with col1:
    st.header("Competitive Analysis")
    st.write(
        "To understand why we stand out, let's conduct a competitive analysis. We've compared Sportan with other sports management platforms, and here's what we found:"
    )
    st.subheader("Competitor A")
    st.write("Pros: Strong user base, established reputation.")
    st.write("Cons: Limited data analysis, complex interface.")
    st.subheader("Competitor B")
    st.write("Pros: Intuitive interface, good mobile app.")
    st.write("Cons: Limited inclusivity, lacks injury management features.")
    st.subheader("Sports Management Hub")
    st.write("Pros: Streamlined efficiency, inclusivity, data-driven insights, simplification of challenges, commitment to user success, and our custom sports chatbot.")
    st.write("Cons: None!")

st.write("---")
# Highlight key features
st.header("Key Features")
st.write("Our platform offers a range of features, including:")
st.write("- Team and Player Management")
st.write("- Athlete Training Reports")
st.write("- Performance Analytics")
st.write("- Communication Tools")
st.write("- Data Security and Privacy")

st.write(
    "We've also integrated a powerful AI bot to assist you with tasks, answer your questions, "
    "and provide insights. Our bot is here to make your sports management experience even better."
)

