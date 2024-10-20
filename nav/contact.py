# streamlit dependencies
import streamlit as st
# data dependencies
import pandas as pd
import numpy as np
import base64
from PIL import Image

def data_professionals():

    st.markdown("")

    st.image('resources/imgs/profile.jpeg', width=150)

     
    col1, col2, col3 = st.columns(3)
    with col1:
            
            st.write("Makhambi M")
            st.write('Email : dlamini.amk@gmail.com')
         
            st.write('LinkedIn: https://www.linkedin.com/in/kilo-dlamini-404b811a7/')   
    
    
    contact_form = """
    <form action="https://formsubmit.co/dlamini.amk@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send mail</button>
    </form>
    """
    
    
    
    team, members, contact, = st.columns([2, 1.5, 1.5])

    with contact:
        st.header("Contact us")
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("./utils/style.css")
    with team:
        st.write("")
    
    with members:
        st.markdown(f'',unsafe_allow_html=True)
        
    st.write("")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style >{f.read()}</style>", unsafe_allow_html=True)