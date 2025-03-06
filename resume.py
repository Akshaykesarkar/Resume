from streamlit_lottie import st_lottie
import streamlit as st 
import requests
import json
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
    # your_password = "ogem jxxm ffop tojf"  

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
    st.link_button("🔗 Connect with me on LinkedIn", "https://www.linkedin.com/in/akshay-kesarkar-40060b285/")     
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
        {"degree": "Bachelor of technologyin Artificial Intelligence and Data Science", "image":"kjsit.jpg", "university": "**K.J. Somaiya Institute of Technology, Mumbai**", "date": "2021 - 2025", "score": "CGPA: 8.6/10.0"}
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
    
    description1 = {
        "description 1":"""
        Worked on a geofencing project where we successfully mapped and analyzed over 900+ agricultural plots.
        Acquired and processed large datasets through data acquisition techniques, ensuring accuracy and relevance for geospatial analysis.
        """,
        "description 2":"""
        Engaged in project development focused on AI/ML and deep learning, working on cutting-edge technologies.
        Applied artificial intelligence and machine learning techniques to real-world problems.
        Gained hands-on experience in deep learning models, including neural networks, and implemented solutions using frameworks like TensorFlow and Keras.
        """
    }

    experience = [
        {"role": "Research Intern","image":"sirac_svu_logo.jpg", "company": "**Geofencing Centre for Achieving Sustainability, Climate Action, Development, and Engagement (CASCADE) Somaiya Institute for Research and Consultancy** ", "date": "Jun 2023 - Jun 2023", "description": description1["description 1"]},
        {"role": "Data Science Intern","image":"oenneo_logo.jpg", "company": "**KJSIT, Computer Engineering Department (in association with Claidroid Technologies Pvt. Ltd.)** ", "date": "Dec 2023 - Jan 2024", "description": description1["description 2"]}
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
    
    col5,col6 = st.columns([2,2])

    with col5:
        st.title("My GitHub Activity")

        # GitHub Streak Stats Image (Replace 'your-username' with your actual GitHub username)
        github_username = "Akshaykesarkar"
        st.image(f"https://github-readme-streak-stats.herokuapp.com/?user={github_username}&theme=default",
                 caption="GitHub Streak Stats")
        st.image(f"https://ghchart.rshah.org/Light/{github_username}", caption="GitHub Contribution Graph")
        
        st.title("My LeetCode Streak")

        # Replace 'your-username' with your actual LeetCode username
        leetcode_username = "akshaykesarkar268" 

        st.image(f"https://leetcard.jacoblin.cool/{leetcode_username}?theme=default&ext=heatmap", 
                caption="LeetCode Streak & Activity")
        
    with col6:
        st.title("My Certificates")
        certificates = [
            {"title": "Machine Learning Specialization", "image":"image.png", "link": "https://coursera.org/share/75c1c44aaf9f4aac25ed0e9ffaa171e8"},
            {"title": "Applied Data Science with Python", "image":"ibm_logo.jpg", "link": "https://skills.yourlearning.ibm.com/certificate/PLAN-B6CBEFCA2BFD"},
            {"title": "Data Mining", "image":"NPTEL.jpg", "link": "https://archive.nptel.ac.in/noc/Ecertificate/?q=NPTEL24CS22S35030033830035499"}
        ]
        for cert in certificates:
            with st.container():
                col7,col8 = st.columns([1,2])
                
                with col7:
                    st.image(cert["image"],width = 130)
                    
                with col8:
                    st.subheader(cert["title"])
                    st.link_button("🔗 View Certificate", cert["link"])
                    
elif selected == "Projects":
    st.title("My Projects")
    
    description2 = {
        "description 1":"This project uses **LSTM networks** for real-time stock price prediction by analyzing historical and live market data. It fetches **real-time stock prices** using APIs like **Yahoo Finance or Alpha Vantage** and processes them with **Pandas and NumPy**. The **LSTM model**, built with **TensorFlow/Keras**, learns patterns from past trends to generate future price forecasts. 🚀📈"
    }

    projects = [
        {"title": "Stock Market Prediction using DL algorithms", "image":"project_image.png", "description": description2["description 1"], "link": "l"},
        {"title": "Stock Market Prediction using DL algorithms", "image":"project_image.png", "description": "Description 1", "link": "l"}
    ]

    for project in projects:
        with st.container():
            col9, col10 = st.columns([0.5, 2])
            
            with col9:
                st.image(project["image"], width=50, use_container_width=True)
            
            with col10:
                st.subheader(project["title"])
                st.write(project["description"])
                st.link_button("🔗 View Project", project["link"])  

elif selected == "Contact":
    st.title("Contact Me")
    with st.container():
        col11,col12 = st.columns([1,2])
        with col11:
            st.lottie(lottie_animation3)
        with col12:
            with st.form("contact_form"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Your Message")

                submitted = st.form_submit_button("Send Message")
                
                if submitted:
                    if name and email and message:
                        response = send_email(name, email, message)
                        st.success(response)
                    else:
                        st.error("⚠ Please fill in all fields before submitting.")
    
                
st.write("---")
st.markdown(" Made by **Akshay Kesarkar** 🖤")


