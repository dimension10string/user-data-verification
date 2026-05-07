import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Internal Data Portal", page_icon="🔒", layout="wide")

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Logic Flow ---

if not st.session_state.authenticated:
    # 1. THE BORING LOGIN PAGE
    st.markdown("""
        <style>
        .stApp { background-color: white !important; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; font-family: Arial; color: #333; padding-top: 100px;'>Family Cloud: Archive Sync</h3>", unsafe_allow_html=True)

    with st.form("login_form"):
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token")
        submitted = st.form_submit_button("Verify Identity")
        
        if submitted:
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Authorizing..."):
                    time.sleep(1)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Invalid Credentials.")

else:
    # 2. THE REVEAL PAGE
    
    # These must match your uploaded GitHub filenames exactly!
    bg_filename = "beach_bg.jpg" 
    main_pic_filename = "us.jpg" 

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        .stApp {{
            background-image: url("app/static/{bg_filename}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        .stDeployButton {{display:none;}}

        .img-container {{
            display: flex;
            justify-content: center;
            width: 100%;
            margin-top: -80px;
        }}
        .hero-image {{
            width: 100vw !important;
            max-width: 100vw !important;
            height: auto;
            border: none;
        }}

        .birthday-text {{
            font-family: 'Pinyon Script', cursive !important;
            color: white !important;
            text-align: center !important;
            font-size: clamp(60px, 15vw, 120px) !important; 
            line-height: 1 !important;
            margin-top: 20px !important;
            text-shadow: 2px 4px 10px rgba(0,0,0,0.4);
        }}

        .glass-card {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            padding: 40px 20px;
            margin: 20px 0;
            color: white;
            text-align: center;
            font-family: 'Montserrat', sans-serif;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.snow()
    st.balloons()

    # Layout
    st.markdown(f'''
        <div class="img-container">
            <img src="app/static/{main_pic_filename}" class="hero-image">
        </div>
        <div class="birthday-text">Happy Birthday, [Wife's Name]</div>
        <div class="glass-card">
            <i style="font-size: 26px;">My Dearest [Wife's Name],</i><br><br>
            <span style="font-size: 18px; line-height: 1.8;">
                I built this corner of the internet to remind you how deeply you are loved. 
                You make every ordinary day feel extraordinary.<br><br>
                May your day be as serene as a Cayman sunrise.<br><br>
                <b style="font-size: 20px; color: #e0f7fa;">Your surprise is waiting for you in the kitchen.</b>
            </span>
            <br><br>
            <span style="font-size: 35px; font-family: 'Pinyon Script';">Love, [Your Name]</span>
        </div>
    ''', unsafe_allow_html=True)
