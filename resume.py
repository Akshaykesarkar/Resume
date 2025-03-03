import streamlit as st 
from streamlit_lottie import st_lottie
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
    your_password = "your-app-password"  # Use an environment variable instead of hardcoding
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

# Set up paths for animation JSON files
script_dir = os.path.dirname(os.path.abspath(__file__))
json1_path = os.path.join(script_dir, "animation.json")
json2_path = os.path.join(script_dir, "animation3.json")

# Load animations if they exist
lottie_animation = json.load(open(json1_path, "r", encoding="utf-8")) if os.path.exists(json1_path) else None
lottie_animation3 = json.load(open(json2_path, "r", encoding="utf-8")) if os.path.exists(json2_path) else None

st.set_page_config(layout="wide")

col1, col2 = st.columns([2,2])

with col1:
    st.write("##")
    st.subheader("Hey Guys :wave:")
    st.title("I am Akshay Kesarkar")
    st.subheader("My Portfolio Website")
    st.write("""
            I am a data enthusiast skilled in **Python, SQL, Data Analysis, Visualization, Big Data Handling, Machine Learning and Deep Learning**.
            I enjoy transforming data into insights and building AI-driven solutions.
            Currently seeking opportunities to apply my skills and grow in the field of data science and machine learning engineering. 🚀 
            """)     
with col2:
    if lottie_animation:
        st_lottie(lottie_animation)
    
st.write("---")
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects", "Contact"],
        icons=["person", "code-slash", "chat-left-text-fill"],
        orientation="horizontal"
    )

if selected == "About":
    st.title("Education")
    education =[
        {"degree": "Bachelor of Technology in Artificial Intelligence and Data Science", "image": "images/kjsit.jpg", "university": "**K.J. Somaiya Institute of Technology, Mumbai**", "date": "2021 - 2025", "score": "CGPA: 8.6/10.0"}
    ]
    
    for edu in education:
        with st.container():
            col1, col2 = st.columns([0.4,2])
            image_path = os.path.join(script_dir, edu["image"])  # Ensure correct path
            with col1:
                if os.path.exists(image_path):
                    st.image(image_path, use_container_width=True)
            with col2:
                st.subheader(edu["degree"])
                st.write(f"at {edu['university']}")
                st.write(f"{edu['date']} | {edu['score']}")
    
    st.title("Experience")
    experience = [
        {"role": "Research Intern", "image": "images/sirac_svu_logo.jpg", "company": "**CASCADE Somaiya Institute for Research and Consultancy** ", "date": "Jun 2023 - Jun 2023", "description": "Worked on geofencing and AI projects."},
        {"role": "Data Science Intern", "image": "images/oenneo_logo.jpg", "company": "**KJSIT & Claidroid Technologies Pvt. Ltd.** ", "date": "Dec 2023 - Jan 2024", "description": "Worked on AI/ML projects."}
    ]
    
    for exp in experience:
        with st.container():
            col3, col4 = st.columns([0.4,2])
            image_path = os.path.join(script_dir, exp["image"])
            with col3:
                if os.path.exists(image_path):
                    st.image(image_path, use_container_width=True)
            with col4:
                st.subheader(exp["role"])
                st.write(f"at {exp['company']} | {exp['date']}")
                st.write(exp["description"])
    
elif selected == "Projects":
    st.title("My Projects")
    projects = [
        {"title": "Stock Market Prediction", "image": "images/project_image.png", "description": "LSTM-based stock price prediction.", "link": "#"}
    ]
    for project in projects:
        with st.container():
            col9, col10 = st.columns([0.5, 2])
            image_path = os.path.join(script_dir, project["image"])
            with col9:
                if os.path.exists(image_path):
                    st.image(image_path, use_container_width=True)
            with col10:
                st.subheader(project["title"])
                st.write(project["description"])
                st.markdown(f"[🔗 View Project]({project['link']})", unsafe_allow_html=True)  

elif selected == "Contact":
    st.title("Contact Me")
    with st.container():
        col11, col12 = st.columns([1,2])
        with col11:
            if lottie_animation3:
                st_lottie(lottie_animation3)
        with col12:
            with st.form("contact_form"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Your Message")
                submitted = st.form_submit_button("Send Message")
                if submitted and name and email and message:
                    response = send_email(name, email, message)
                    st.success(response)
                elif submitted:
                    st.error("⚠ Please fill in all fields before submitting.")
                    
st.write("---")
st.markdown(" Made by **Akshay Kesarkar** 🖤")
