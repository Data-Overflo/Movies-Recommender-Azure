import streamlit as st

def about():
    #about page title
    st.title("M. Makhambi")


    about_RecoX, movieMatch_logo, = st.columns([2, 3])
    
    with about_RecoX:

        st.write("Software Developer | Application Developer | Web Developer | Data Scientist | Machine Learning Engineer")

        st.write("I'm a Full Stack Data Scientist from South Africa, driven by a passion for crafting innovative high-quality software solutions and using technology to solve real-world problems, from Data Engineering, Data Analysis and Machine Learning, DevOps to Web Development")
        
    st.markdown("")
    with movieMatch_logo:
        st.image('resources/imgs/profile.jpeg', width=150)