import streamlit as st
import time

# --- INITIAL CONFIG ---
st.set_page_config(page_title="Internal Data Portal", page_icon="🔒", layout="wide")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- UI LOGIC ---
if not st.session_state.authenticated:
    # THE DECEPTION
    st.markdown("<style>.stApp { background-color: white !important; } #MainMenu, footer, header {visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-family: sans-serif; color: #333; padding-top: 100px;'>Family Cloud: Archive Sync</h3>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token")
        if st.form_submit_button("Verify Identity"):
            if u_name.strip() != "" and "cayman" in u_token.lower():
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid Credentials.")
else:
    # THE LUXURY REVEAL
    # REPLACE FILENAMES HERE
    bg = "beach_bg.jpg" 
    hero = "us.jpg" 
    wife_name = "Her Name"
    your_name = "Your Name"

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');
        .stApp {{ background-image: url("app/static/{bg}"); background-size: cover; background-position: center; background-attachment: fixed; }}
        #MainMenu, footer, header, .stDeployButton {{visibility: hidden; display:none;}}
        
        .img-container {{ display: flex; justify-content: center; width: 100%; margin-top: -80px; overflow: hidden; }}
        .hero-image {{ width: 100vw !important; height: auto; border: none; border-radius: 0; }}
        
        .birthday-text {{
            font-family: 'Pinyon Script', cursive !important;
            color: white !important; text-align: center !important;
            font-size: clamp(65px, 15vw, 120px) !important; 
            line-height: 1 !important; margin: 25px 0 !important;
            text-shadow: 2px 4px 10px rgba(0,0,0,0.4);
        }}
        
        .glass-card {{
            background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            padding: 40px 20px; margin: 20px 0; color: white; text-align: center; font-family: 'Montserrat', sans-serif;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.snow()
    st.balloons()

    st.markdown(f'<div class="img-container"><img src="app/static/{hero}" class="hero-image"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="birthday-text">Happy Birthday, {wife_name}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="glass-card"><i style="font-size: 24px;">My Dearest {wife_name},</i><br><br><span style="font-size: 18px; line-height: 1.8;">I built this corner of the internet to remind you how deeply you are loved.<br><br><b>Your surprise is waiting in the kitchen.</b></span><br><br><span style="font-size: 35px; font-family: \'Pinyon Script\';">Love, {your_name}</span></div>', unsafe_allow_html=True)
