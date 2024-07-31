import streamlit as st

def about_us():
    st.title("About Us")

    st.header("Team  Sportans")
    
    st.write("In our first year of studies, we embarked on a remarkable journey to create this project, a journey that served as a testament to our collective ideas and boundless creativity. This endeavor, though undoubtedly challenging, proved to be an immensely rewarding experience that has left an indelible mark on each of us.")

    st.write("We wish to extend our deepest and most sincere gratitude to our mentor, Nandhini K. Her unwavering guidance and steadfast support were nothing short of invaluable. She not only steered us through the intricate and often convoluted path of this project but also instilled in us the wisdom and confidence necessary to navigate the complexities that arose.")

    st.write("Throughout this journey, there were countless late nights spent debugging code and endless iterations as we sought perfection. Despite the inevitable hurdles, our unwavering passion for our work, coupled with the steadfast support of our mentor, served as the bedrock upon which we persevered and thrived.")

    st.write("As we stand here today, presenting our project to the world, we are profoundly grateful for the privilege of having you visit and bear witness to the tangible result of our dedication and hard work. It is our hope that our project, the culmination of countless hours of labor and unwavering determination, proves to be not only inspiring but also informative to all those who engage with it.")


    st.write("---")
    col1,col2,col3=st.columns([2,0.5,2])

    with col1:
         st.header("Mentor:")
         
         st.image("images\mentor.jpg")
         st.write("Nandhini K")
    

    with col3:
         st.write("")
         st.write("")
         st.subheader("Team Members:")
         st.write("")
         st.image("images\members.jpg",caption="-Kartik  -Karan Rekhan       -Naman      -Aaditya      -Mallikarjun       -Karthik      -Karan Chauhan     -Utkarsh")



about_us()

