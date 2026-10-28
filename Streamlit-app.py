import streamlit as st
from PIL import Image


col1, col2 = st.columns((4, 5))


with col1:
    st.title("Edwin Arias Tellez")
    st.header("John Brown University Freshman")
    st.markdown("About Me")
    st.text("A Cybersecurity and Computer Science student in John Brown University")
    st.divider()
with col2:
    image = Image.open('moto.png')

st.balloons()



st.markdown("Qualifications")
st.text("High School Diploma")
st.text("Middle Tech Title in Networking")
st.divider()
st.markdown("Certifications")
st.text("Cisco CCNA 1")
st.text("Cisco CCNA 2")
st.text("Cisco CCNA 3")
st.divider()

st.markdown("Work Experience")
st.text("Kuanta Bridge [feb 2026 - jul 2026]")
st.text("A networking experience and cybersecurity usage of Acronis and Sophos")
st.divider()

st.markdown("Projects")
st.text("Fitness App - Axis")
st.divider()


st.markdown("**Contact Me**")
st.text("Number: (479) 599 9087")
st.text("Email: Ariastellee@jbu.edu")
st.text("GitHub: https://github.com/Ariastellee")


username = st.text_input("Username")
userEmail = st.text_input("Email")
userMessage= st.text_input("Message")
st.button("Send Message")
st.divider()





