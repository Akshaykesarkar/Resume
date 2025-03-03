from streamlit_lottie import st_lottie
import streamlit as st 
import requests
import json
import os
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

def send_email(name, sender_email, message):
    your_email = "akshaykesarkar268@gmail.com"  
    your_password = "iptt tnvz ktrb bclf"  

    subject = f"New Contact Form Submission from {name}"
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = your_email  
    msg["Subject"] = subject
    msg.attach(MIMEText(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}", "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(your_email, your_password)
        server.sendmail(your_email, your_email, msg.as_string())
        server.quit()
        return "✅ Message sent successfully!"
    except Exception as e:
        return f"❌ Error sending email: {e}"

def get_image_path(filename):
    return os.path.join("images", filename)

with open("animation.json", "r", encoding="utf-8") as f:
    lottie_animation = json.load(f)
    
with open("animation3.json", "r", encoding="utf-8") as f:
    lottie_animation3 = json.load(f)
st.set_page_config(layout="wide")

col1,col2 = st.columns([2,2])

with col1:
    st.write("##")
    st.subheader("Hey Guys :wave:")
    st.title("I am Akshay Kesarkar")
    st.subheader("My Portfolio Website")
    st.write("""
            I am a data enthusiast skilled in **Python, SQL, Data Analysis, Visualization, Big Data Handling, Machine Learning and Deep Learning**.
            I enjoy transforming data into insights and building AI-driven solutions.
            Currently seeking opportunities to apply my skills and grow in the field of data science and machine learning engineer. 🚀 
            """)     
with col2:
    st_lottie(lottie_animation)
    
st.write("---")
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About","Projects","Contact"],
        icons=["person","code-slash","chat-left-text-fill"],
        orientation="horizontal"
    )

if selected == "About":
    st.title("Education")
    education =[
        {"degree": "Bachelor of technology in Artificial Intelligence and Data Science", "image": get_image_path("kjsit.jpg"), "university": "**K.J. Somaiya Institute of Technology, Mumbai**", "date": "2021 - 2025", "score": "CGPA: 8.6/10.0"}
    ]
    
    for edu in education:
        with st.container():
            col1,col2 = st.columns([0.4,2])
            
            with col1:
                st.image(edu["image"],use_container_width=True)
                
            with col2:
                st.subheader(edu["degree"])
                st.write(f"at {edu['university']}")
                st.write(f"{edu['date']} | {edu['score']}")
    
    st.title("Experience")
    
    experience = [
        {"role": "Research Intern","image": get_image_path("sirac_svu_logo.jpg"), "company": "**Geofencing Centre for Achieving Sustainability, Climate Action, Development, and Engagement (CASCADE) Somaiya Institute for Research and Consultancy**", "date": "Jun 2023 - Jun 2023", "description": "Worked on a geofencing project where we successfully mapped and analyzed over 900+ agricultural plots."},
        {"role": "Data Science Intern","image": get_image_path("oenneo_logo.jpg"), "company": "**KJSIT, Computer Engineering Department (in association with Claidroid Technologies Pvt. Ltd.)**", "date": "Dec 2023 - Jan 2024", "description": "Engaged in AI/ML project development, focusing on deep learning and advanced models."}
    ]
    
    for exp in experience:
        with st.container():
            col3,col4 = st.columns([0.4,2])
            
            with col3:
                st.image(exp["image"],use_container_width=True)
                
            with col4:
                st.subheader(exp["role"])
                st.write(f"at {exp['company']} | {exp['date']}")
                st.write(exp["description"])
    
    st.write("---")
    
    st.title("My Certificates")
    certificates = [
        {"title": "Machine Learning Specialization", "image": get_image_path("image.png"), "link": "https://coursera.org/share/75c1c44aaf9f4aac25ed0e9ffaa171e8"},
        {"title": "Applied Data Science with Python", "image": get_image_path("ibm_logo.jpg"), "link": "https://skills.yourlearning.ibm.com/certificate/PLAN-B6CBEFCA2BFD"}
    ]
    for cert in certificates:
        with st.container():
            col7,col8 = st.columns([1,2])
            
            with col7:
                st.image(cert["image"],width = 130)
                
            with col8:
                st.subheader(cert["title"])
                st.markdown(f"[🔗 View Certificate]({cert['link']})", unsafe_allow_html=True)

st.write("---")
st.markdown(" Made by **Akshay Kesarkar** 🖤")
