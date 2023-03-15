from pathlib import Path
import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import webbrowser



#--- path settings
curr_dir= Path(__file__).parent if"__file__" in locals() else Path.cwd()
css_file = "styles/main.css"
resume_file = "assets/cv.pdf"
warehouse_file="assets/Warehouse_management_report.docx"
dp_file = "assets/dp1.jpg"
certificate_file="assets/certificate.pdf"


# For inseritng animation we use Lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()






#----Page Variables----
TITLE= " WELCOME TO MY PORTFOLIO"
ICON=":wave:"
name = "I'm JOYAL KENUS"
description =""" Mechatronics Engineer and Data analyst   """
email="joyalkenus2711@gmail.com"
social_media={
    "Linkedin": "https://www.linkedin.com/in/joyal-kenus-7aa6b21b9/",
    "Github" :"https://github.com/joyalkenus"
}


st.set_page_config(page_title=TITLE, page_icon=ICON,layout="wide")





#---------lOAD CSS , PDF & PROFILE PI
with open('styles/main.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(certificate_file,"rb") as c:
    certificate=c.read()
profile_pic = Image.open(dp_file)
project_img1= Image.open("assets/face_project.jpg")
project2_img = Image.open('assets/Bionic_project.jpg')
project3_img = Image.open('assets/warehouse_project.jpg')
project4_img = Image.open('assets/quadro.jpg')
git_repo_url = "https://github.com/joyalkenus/Semi-autonomous-driving-system"

#load assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1LhsaB.json")
lottie_qual = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_stozcwgt.json")
lottie_hi = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_m9fz64i8.json")

# ----- -------------------------------------------------------------LOAD SIDE BAR
with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options=["Home","Qualifications","Projects"],
        icons=["house","award","person-workspace"],
        menu_icon="cast",
        default_index=0
    )




if selected == "Home":
    #------------------------------------------------------------------Main Section -----
    col1, col2 = st.columns((1, 2), gap="medium")
    with col1:
        st.image(dp_file)
    with col2:
        
        st.title("Hi :wave:,")
        st.title(name)
        st.subheader("Roboticist and Data Analyst")
        st.write("As a professional with expertise in robotics and data analysis, I am deeply committed to leveraging my skill set towards the creation of robust robotic systems and sophisticated machine learning models. My passion lies in identifying innovative avenues to apply these skills in pursuit of these goals. ")
        st.download_button(
            label="Take a look at my CV",
            data=PDFbyte,
            file_name=resume_file,
            mime="application/octet-stream",

        )
        st.write("📧:", email)
        #--- social links
        st.write("##")
        cols = st.columns(len(social_media))
        for index, (platform, link) in enumerate(social_media.items()):
            cols[index].write(f"[{platform}]({link})")




    #-------------------------------------------------------------Website section -----

    with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)
        with left_col:
            st.header("Welcome to My Website 🌐")
            st.write("###")
            st.write("My goal in creating this website was to compile all of my skill sets and projects into a single, easy-to-navigate location that anyone can access. I hope you find it informative and inspiring. This way i can make everything about me accesible to anyone who wants to take a look with the click of a button. ")
            st.write(
                "This was made my using streamlit and Python and deployed through Render.")
        with right_col:
            st_lottie(lottie_coding, height=400, key="coding")



#------------------------------------------------------------- QUALIFICATIONS-------------------------------------
if selected=="Qualifications":
    #---Qualifications--
    st.write("---")
    with st.container():
        left_col, right_col = st.columns(2)
        with left_col:
            st.header("⭐️ Qualifications & Certifications")
            st.markdown("---")
            
            st_lottie(lottie_qual, height=400, key="qualification")
            
            
        with right_col:
            
            st.subheader("✔️ Google Data Analytics Professional Certification")
            st.write("Completed on March 2023")
            st.markdown("***")
            
            st.subheader("✔️Master's in Mechatronics and Intelligent Machines")
            st.write("University of Central Lancashire, preston")
            st.write("Graduated with Distinction") 
            st.write("JAN 2021 - JULY 2022")
            st.markdown("***")
            st.subheader("✔️Bachelor's in Mechatronics Engineering")
            st.write("Nehru Institute of Engineering and Technology, Coimbatore, India")
            st.write("Graduated with First class degree")
            st.write("JUN 2016 - JUN 2020")
            st.markdown("***")
            st.subheader("✔️Deep Learning A-Z Hands-on Artificial Neural Network Completion Certificate from Udemy")
            st.write("Completed the certification on Mar 2 2023.")
            st.download_button(
                label="Download Certificate ",
                data=certificate,
                file_name=resume_file,
                mime="application/octet-stream",

            )
        
#---------------------------------------------------------------- projects------------------------
if selected =="Projects":
    #-- Projects
    


    with st.container():
        st.header("🤖 My Projects On Robotics ")
        st.markdown("___")
        st.subheader("1)")
        st.write("##")
        img_column, text_column = st.columns((1, 2))

        with img_column:
            # Add your image here.
            st.image(project_img1)

            with text_column:
                st.subheader("🏆 Face Orientation Based Wheelchair Driving System")
            # Add your text and other content here.
                st.markdown("- This project utilizes Arduino robotic systems that are integrated with a computer vision model to perform facial orientation checks. The arduino robotic car is provided with various facial orientation commands to move accordingly.The purpose of this model is to showcase a system that was proposed in my master's project, which could potentially be used in electric wheelchairs for individuals with disabilities.Additionally, the original project proposed an obstacle avoidance system using ultrasonic sensors, which is demonstrated on a small scale in this model.A 3D simulation was also made inorder to test the facial orientation system further in various environments and tested on diffrent faces. This simulation was done by using WeBots software. ")

                st.video("https://www.youtube.com/watch?v=sPwev6zheQM&t=17s")
                if st.button("GITHUB REPOSITORY FOR THIS PROJECT"):
                    webbrowser.open_new_tab(git_repo_url)
        st.markdown("___")
        st.subheader("2)")
        st.write("##")
        img_column, text_column = st.columns((1, 2))

        with img_column:
            # Add your image here.
            st.image(project2_img)

            with text_column:
                st.subheader("🏆 Bionic Hand For Handicapped To Ride a Motorbike")
                st.markdown("- During my undergraduate studies in Mechatronics Engineering, I undertook a mini-project to design a Bionic arm that could be securely attached to the hand using straps. Our team successfully developed a design that could be mounted onto the original accelerator handle of a motorbike, with the exoskeleton's motion powered by a servo motor that was controlled by an Arduino system. To enable intuitive acceleration control, we incorporated an accelerometer sensor to detect the degree of twist of the bicep, which was then translated into acceleration commands and sent to the Arduino microcontroller for processing.")
                st.video("https://www.youtube.com/watch?v=qooHR-YLo5c")
        st.markdown("___")
        st.subheader("3)")
        st.write("##")
        img_column, text_column = st.columns((1, 2))

        with img_column:
            # Add your image here.
            st.image(project3_img)

            with text_column:
                st.subheader(
                    "🏆 WareHouse Management System Using 4DOF Robotic Arm")
                st.markdown(""" - This project was a collaborative effort among myself and fellow students during my undergraduate studies in Mechatronics. We recognized a challenge within the warehousing and ecommerce industries in regard to the time required to sort and store various products. Our solution to this problem was the implementation of a warehouse management system composed of 4-degree-of-freedom (4DOF) robotic arms that could handle the picking and placing of a wide range of products. Each product was equipped with a unique Radio Frequency Identification (RFID) tag for identification purposes. The sorting process began as products were placed onto a conveyor belt, where they were then scanned by an RFID scanner. The resulting signal was sent to an ARDUINO board for processing, which allocated space for the product in the warehouse. This was achieved by using infrared sensors placed in the storage areas to identify available space. The system then sent signals to the robotic arm to pick up and place the product in the correct location. To improve the efficiency of the system, we integrated a record and play system into the robot's hands, allowing operators to train the system according to their specific needs. The proposed system offers flexibility for use in various warehouses and storage spaces. """)
                st.download_button(
                    label="Download the report for this project here",
                    data=PDFbyte,
                    file_name=warehouse_file,
                    mime="application/octet-stream",

                )
        st.markdown("___")
        st.subheader("4)")
        st.write("##")
        img_column, text_column = st.columns((1, 2))

        with img_column:
            # Add your image here.
            st.image(project4_img)

            with text_column:
                st.subheader("🏆 Workshop project on a Quadroped robot")
                st.markdown(" - During my early years, I had the opportunity to participate in a project facilitated by SP Robotics Maker Lab, Edapally, Kerala. The primary objective of this workshop was to learn how to program and operate a quadruped robot. In order to receive a certificate, participants were required to complete a project utilizing the robot. I decided to attach a rotating brush to the front of the robot, effectively creating a mini-robotic cleaner. The key advantage of using a quadruped as a cleaning robot is the relatively small surface area it covers on the ground, compared to other types of cleaning robots. This design feature eliminates the need for a sweeper on the rear of the robot, which is often present in other types of cleaning robots. The robot kit used in this project included an Arduino controller, 3D printed robotic parts, 8 servo motors, and an ultrasonic sensor.")
                st.markdown(
                    "- It was really fun to play around with this quadroped robot :smile:.")
                st.video("https://www.youtube.com/watch?v=Cn-CBeOi3Cc")














