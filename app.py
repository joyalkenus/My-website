import streamlit as st
from pathlib import Path
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import webbrowser

# -- Path settings
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = "styles/main.css"

# -- Update these filenames with your new CV info
resume_file = "assets/JK_compact.pdf"
warehouse_file = "assets/Warehouse_management_report.docx"
dp_file = "assets/dp.png"
certificate_file = "assets/certificate.pdf"

# -- Additional Lottie animations (optional). 
#    Add or replace these with other fun animations from lottiefiles.com
LOTTIE_CODING_URL = "https://assets5.lottiefiles.com/packages/lf20_1LhsaB.json"
LOTTIE_QUAL_URL   = "https://assets9.lottiefiles.com/packages/lf20_stozcwgt.json"
LOTTIE_HI_URL     = "https://assets10.lottiefiles.com/packages/lf20_m9fz64i8.json"
LOTTIE_SPARKLES   = "https://assets9.lottiefiles.com/packages/lf20_w51pcehl.json"

# -- Social Media
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/joyal-kenus-7aa6b21b9/",
    "GitHub": "https://github.com/joyalkenus"
}

# -- Basic Portfolio Settings
TITLE = "WELCOME TO MY PORTFOLIO"
ICON = ":wave:"
NAME = "I'm JOYAL KENUS"
DESCRIPTION = """Machine Learning and Robotics Engineer"""
EMAIL = "joyalkenus2711@gmail.com"
PHONE = "+44 7859 798421"
ADDRESS = "1 Cedar Drive, Edenbridge, TN8 5JN, United Kingdom"

# -- Streamlit Page Config
st.set_page_config(page_title=TITLE, page_icon=ICON, layout="wide")

# -- Utility function: load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -- Load external resources
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(certificate_file, "rb") as c:
    certificate = c.read()

profile_pic = Image.open(dp_file)
project_img1 = Image.open("assets/face_project.jpg")
project2_img = Image.open("assets/Bionic_project.jpg")
project3_img = Image.open("assets/warehouse_project.jpg")
project4_img = Image.open("assets/quadro.jpg")
git_repo_url = "https://github.com/joyalkenus/Semi-autonomous-driving-system"

# -- Load Lottie animations
lottie_coding = load_lottieurl(LOTTIE_CODING_URL)
lottie_qual = load_lottieurl(LOTTIE_QUAL_URL)
lottie_hi = load_lottieurl(LOTTIE_HI_URL)
lottie_spark = load_lottieurl(LOTTIE_SPARKLES)

# -- Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Qualifications", "Projects", "Experience", "Contact"],
        icons=["house", "award", "person-workspace", "briefcase", "envelope-fill"],
        menu_icon="cast",
        default_index=0
    )

# --------------------- HOME ---------------------
if selected == "Home":
    col1, col2 = st.columns((1, 2), gap="medium")

    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title("Hi :wave:,")
        st.title(NAME)
        st.subheader("Machine learning and Robotics Engineer")
        st.write(
            "Welcome to my portfolio! "
            "I'm a Machine Learning and Robotics engineer, "
            "It’s a deep passion of mine. I like to create robust robotic "
            "systems and deploy sophisticated ML models in the real world."
        )

        st.download_button(
            label="Take a look at my CV",
            data=PDFbyte,
            file_name="JK_compact.pdf",
            mime="application/octet-stream",
        )

        st.write(f"**Phone**: {PHONE}")
        st.write(f"**Email**: {EMAIL}")
        st.write(f"**Address**: {ADDRESS}")
        st.write("##")
        st.write("Let’s stay connected on these platforms:")
        # Social links
        cols = st.columns(len(social_media))
        for index, (platform, link) in enumerate(social_media.items()):
            cols[index].write(f"[{platform}]({link})")

    # A mini “sparkles” or greeting animation
    st.write("---")
    st_lottie(lottie_spark, height=120, key="hi_there")

    # A quick “about the site” explanation
    with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)
        with left_col:
            st.header("Welcome to My Website 🌐")
            st.write(
                "I created this space to share my skill sets, creative projects, "
                "and overall journey with anyone curious. It’s all about easy access "
                "and a friendly “hey, let’s collaborate!” vibe."
            )
            st.write(
                "Built with :blue[Streamlit], :green[Python], and a dash of whimsy. "
                "Deployed on Render for seamless sharing."
            )
        with right_col:
            st_lottie(lottie_coding, height=300, key="coding")

# --------------------- QUALIFICATIONS ---------------------
if selected == "Qualifications":
    st.write("---")
    st.header("⭐️ Qualifications & Certifications")
    st.write(
        "Uh, here’s a snapshot of my educational journey and some certificates "
        "I’ve proudly earned along the way."
    )
    st.write("##")

    left_col, right_col = st.columns(2)
    with left_col:
        # Another lottie for the qualifications
        st_lottie(lottie_qual, height=400, key="qualification")

    with right_col:
        st.subheader("✔️ Google Data Analytics Professional Certification")
        st.write("Completed on March 2023")
        st.markdown("***")

        st.subheader("✔️Master's in Mechatronics and Intelligent Machines")
        st.write("University of Central Lancashire, Preston")
        st.write("Graduated with Distinction")
        st.write("JAN 2021 - JULY 2022")
        st.markdown("***")

        st.subheader("✔️Bachelor's in Mechatronics Engineering")
        st.write("Nehru Institute of Engineering and Technology, Coimbatore, India")
        st.write("Graduated with First class degree")
        st.write("JUN 2016 - JUN 2020")
        st.markdown("***")

        st.subheader("✔️ Deep Learning A-Z Hands-on Artificial Neural Network (Udemy)")
        st.write("Completed the certification on Mar 2 2023.")
        st.download_button(
            label="Download Certificate",
            data=certificate,
            file_name="certificate.pdf",
            mime="application/octet-stream",
        )

# --------------------- PROJECTS ---------------------
if selected == "Projects":
    st.header("🤖 My Projects On Robotics")
    st.write(
        "These are some highlights of the work I’m most proud of. "
        "I hope you find them as exciting as I do!"
    )
    st.markdown("---")

    # 1) Face Orientation Based Wheelchair
    st.subheader("1) Face Orientation Based Wheelchair Driving System")
    img_col, text_col = st.columns((1, 2))
    with img_col:
        st.image(project_img1, use_column_width=True)
    with text_col:
        st.markdown(
            "- This project utilizes Arduino robotic systems along with a "
            "computer vision model for facial orientation checks. "
            "The end goal was to help individuals with disabilities control "
            "a wheelchair through facial orientation commands."
        )
        st.video("https://www.youtube.com/watch?v=sPwev6zheQM&t=17s")
        if st.button("GitHub Repo for Face Orientation Project"):
            webbrowser.open_new_tab(git_repo_url)

    st.markdown("---")

    # 2) Bionic Hand
    st.subheader("2) Bionic Hand For Handicapped To Ride a Motorbike")
    img_col2, text_col2 = st.columns((1, 2))
    with img_col2:
        st.image(project2_img, use_column_width=True)
    with text_col2:
        st.markdown(
            "- As part of my undergrad in Mechatronics, we designed an exoskeleton "
            "arm that straps onto the user’s bicep and controls the motorbike "
            "accelerator using a servo motor. An accelerometer sensor helped "
            "measure the bicep’s twist to determine acceleration inputs."
        )
        st.video("https://www.youtube.com/watch?v=qooHR-YLo5c")

    st.markdown("---")

    # 3) Warehouse Management System
    st.subheader("3) Warehouse Management System Using 4DOF Robotic Arm")
    img_col3, text_col3 = st.columns((1, 2))
    with img_col3:
        st.image(project3_img, use_column_width=True)
    with text_col3:
        st.markdown(
            "- Collaborated during undergrad to create a 4DOF robotic arm "
            "system that could identify, sort, and store products in a warehouse. "
            "Each product had an RFID tag, and IR sensors helped locate free spaces. "
            "The arm would pick and place items accordingly."
        )


    st.markdown("---")

    # 4) Quadroped robot workshop
    st.subheader("4) Workshop Project on a Quadruped Robot")
    img_col4, text_col4 = st.columns((1, 2))
    with img_col4:
        st.image(project4_img, use_column_width=True)
    with text_col4:
        st.markdown(
            "- During my early years, I participated in a workshop by SP Robotics Maker Lab. "
            "I learned to build and program a quadruped robot, then attached a rotating brush "
            "to create a mini-robotic cleaner. Super fun experience!"
        )
        st.video("https://www.youtube.com/watch?v=Cn-CBeOi3Cc")

# --------------------- EXPERIENCE (New Page) ---------------------
if selected == "Experience":
    st.header("My Experience & Additional Details")

    st.write("---")

    # -- Summary
    st.subheader("SUMMARY")
    st.markdown(
        "Machine Learning Engineer with proven expertise in developing emotion "
        "recognition systems and deploying production-scale AI solutions. Demonstrated "
        "track record in architecting and optimizing transformer-based models, with "
        "a focus on synthetic data generation and scalable ML pipelines. Experienced "
        "in implementing deep learning frameworks including PyTorch for real-world "
        "applications in computer vision and human-AI interaction. Consistently delivers "
        "innovative solutions by combining technical expertise in model architecture "
        "design with practical implementation strategies. Notable achievements include "
        "developing real-time facial recognition systems and contributing to cutting-edge "
        "emotion AI research at Onairos. Strong foundation in both theoretical ML concepts "
        "and hands-on engineering, with experience in end-to-end ML workflow optimization "
        "and deployment."
    )

    # -- Work Experience
    st.write("---")
    st.subheader("WORK EXPERIENCE")

    # Onairos
    st.markdown("**Machine Learning Engineer, At Onairos, London, United Kingdom**")
    st.write("Oct 2024 - Present")
    st.markdown(
        """
        - **Research and Development**: Assisting with cutting-edge AI emotion model research.  
        - **Emotion Model Development**: Contributed to advanced emotion recognition models.  
        - **Model Training**: Prepared and trained new AI models with dataset filtering and manipulation.  
        - **Synthetic Data Generation**: Developed systems for synthetic data labeling to enhance dataset quality.  
        - **Implementation**: Utilized PyTorch, transformer models, MLPs, and neural networks.  
        - **Algorithm Optimization**: Improved model performance with effective tuning.  
        - **Data Preprocessing**: Cleaned, normalized, and augmented data for training.  
        - **Version Control**: Employed Git for seamless collaboration.
        """
    )

    # Freelance Upwork
    st.markdown("**AI Integration Specialist, Freelance in Upwork, London, United Kingdom**")
    st.write("May 2024 - Sep 2024")
    st.markdown(
        """
        - **GPT Integration**: Implemented custom GPT solutions for small/medium businesses.  
        - **API Development**: Created robust APIs to integrate GPT models with existing systems.  
        - **Software Development**: Built personalized software leveraging AI.  
        - **Scalability Planning**: Designed AI solutions for future business growth.  
        - **Client Education**: Guided businesses on leveraging GPT tech.  
        - **Communication**: Ensured clear deliverables and frequent updates.
        """
    )

    # -- Education
    st.write("---")
    st.subheader("EDUCATION")
    st.markdown(
        """
        **University of Central Lancashire, Preston, United Kingdom**  
        Master of Science, Mechatronics and Intelligent Machines — GPA: 4.0  
        *Jan 2021 - Jul 2022*

        **Nehru Institute of Engineering and Technology, Coimbatore, India**  
        Bachelor of Engineering, Mechatronics Engineering — GPA: 3.4  
        *Jun 2016 - Jul 2020*
        """
    )

    # -- Additional Projects
    st.write("---")
    st.subheader("ADDITIONAL PROJECTS")
    st.markdown(
        """
        - **Semi-Autonomous Face Orientation Controlled Wheelchair Driving System**  
          Developed a Facial orientation recognition system with OpenCV, tested on an Arduino robotic car.  
          Integrated powertrain calibration techniques for varying commands and an obstacle avoidance system.  
          Constructed a WeBots 3D simulation for precision confirmation.
        
        - **Eva – On-demand Personal Yoga Companion**  
          Developed a fully functional web app providing real-time feedback on yoga poses.  
          Used ElevenLabs for voice, a Custom Google Search Engine for poses, and Gemini 1.5 pro for vision.
        
        - **AI Skill Analyser for Reputy.io**  
          Designed a soft skill analyser from scraped social media data.  
          Implemented Retrieval Augmented Generation (RAG) with Multimodal GPT to extract talent.
        
        - **Bionic Hand for Handicapped to Ride a Motorbike**  
          Engineered a prototype bionic hand enabling disabled individuals to control motorbike acceleration.  
          Linked bicep rotations to the bike's accelerator for accessible control.
        """
    )

    # -- Skills
    st.write("---")
    st.subheader("SKILLS")
    st.markdown(
        """
        - **Programming**: Python, JavaScript, C++  
        - **Data Tools**: SQL, Tableau, Power BI  
        - **Machine Learning**: PyTorch, MLOps, Data Pipelines, TensorFlow, Keras, Scikit-Learn  
        - **Technologies**: Arduino, MATLAB, OpenCV  
        - **Robotics**: Microcontrollers, Embedded systems, PLC, Pneumatic systems, Path Planning  
        - **Cloud**: AWS, Azure, GCP
        """
    )

    st.write("---")
    st.success("That’s the full scoop on my background. Thanks for reading!")    

# --------------------- CONTACT ---------------------
if selected == "Contact":
    st.header("Get in Touch :handshake:")
    st.write(
        "Um, I'd be absolutely delighted to hear from you—whether it's about "
        "a new project idea, collaboration, or just a friendly hello!"
    )
    st.write("##")
    contact_col1, contact_col2 = st.columns((2, 1))

    with contact_col1:
        st.subheader("Send me an email")
        st.write(
            f":envelope: [Email me here](mailto:{EMAIL})\n\n"
            "I usually respond within 24-48 hours."
        )
        st.write("##")

        st.subheader("Connect with me on LinkedIn")
        st.write(
            f":arrow_right: [LinkedIn Profile]({social_media['LinkedIn']})"
        )
        st.write("##")

        st.subheader("Check out my GitHub")
        st.write(
            f":computer: [GitHub Profile]({social_media['GitHub']})"
        )

    with contact_col2:
        # A sweet finishing animation
        st_lottie(lottie_hi, height=250, key="say_hi")

    st.write("##")
    st.write(
        "Thank you so much for dropping by! "
        "Have a wonderful day."
    )
