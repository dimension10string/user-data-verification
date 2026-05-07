import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Internal Data Portal", page_icon="🔒", layout="wide")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 1. THE BORING LOGIN (PRE-AUTH) ---
if not st.session_state.authenticated:
    st.markdown("""
        <style>
        .stApp { background-color: #ffffff !important; }
        #MainMenu, footer, header, .stDeployButton {visibility: hidden; display:none;}
        .stForm {
            border: 1px solid #e0e0e0 !important;
            background: #fafafa;
            padding: 30px;
            border-radius: 5px;
            max-width: 450px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; color: #222; padding-top: 80px;'>Family Cloud: Archive Sync</h2>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token")
        
        # When she clicks this button, the browser "unlocks" the ability to play audio
        if st.form_submit_button("Verify Identity & Sync"):
            if u_name.strip() != "" and "cayman" in u_token.lower():
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid Token.")

# --- 2. THE LUXURY REVEAL (POST-AUTH) ---
else:
    # SETTINGS
    bg_filename = "beach_bg.jpg" 
    hero_filename = "us.jpg" 
    wife_name = "Her Name"
    your_name = "Your Name"
    
    # Direct high-quality link to Life in Technicolor II (Instrumental-style)
    # This works better than YouTube for background autoplay
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # Placeholder - replace with your direct mp3 link if you have one

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;300;400&display=swap');

        .stApp {{ 
            background-image: url("app/static/{bg_filename}"); 
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
        }}
        
        #MainMenu, footer, header, .stDeployButton {{visibility: hidden; display:none;}}
        .block-container {{ padding-top: 0rem !important; }}

        .img-container {{ 
            display: flex; justify-content: center; width: 100vw; 
            margin-left: calc(-50vw + 50%); overflow: hidden; 
        }}
        .hero-image {{ width: 100%; height: auto; border-radius: 0px !important; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); }}
        
        .birthday-text {{
            font-family: 'Pinyon Script', cursive !important;
            color: #ffffff !important; text-align: center !important;
            font-size: clamp(55px, 13vw, 110px) !important; 
            line-height: 1.1 !important; margin: 35px 10px !important;
            text-shadow: 2px 4px 15px rgba(0,0,0,0.6);
        }}
        
        .glass-card {{
            background: rgba(255, 255, 255, 0.12); 
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            border-top: 1px solid rgba(255,255,255,0.3);
            padding: 50px 20px 100px 20px; 
            width: 100vw; margin-left: calc(-50vw + 50%);
            color: white; text-align: center; font-family: 'Montserrat', sans-serif;
        }}
        </style>
    """, unsafe_allow_html=True)

    # THE AUDIO TRICK
    # This iframe uses a standard autoplay attribute that modern browsers allow 
    # AFTER a user clicks a button (which she did to login).
    st.markdown(f"""
        <iframe src="https://www.youtube.com/embed/fXsovfOKUPM?autoplay=1&mute=0" 
            allow="autoplay" style="display:none;"></iframe>
    """, unsafe_allow_html=True)

    st.snow()
    st.balloons()

    # The Visual Reveal
    st.markdown(f'<div class="img-container"><img src="app/static/{hero_filename}" class="hero-image"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="birthday-text">Happy Birthday, {wife_name}</div>', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="glass-card">
            <p style="letter-spacing: 5px; font-size: 11px; text-transform: uppercase; margin-bottom: 25px; opacity: 0.9;">A Dedicated Message</p>
            <i style="font-size: 24px;">My Dearest {wife_name},</i><br><br>
            <span style="font-size: 18px; line-height: 1.9;">
                I built this corner of the internet to remind you how deeply you are loved. <br>
                You make every ordinary day feel extraordinary.<br><br>
                May your day be as serene as a Cayman sunrise.<br><br>
                <b style="color: #e0f7fa;">Your surprise is waiting for you in the kitchen.</b>
            </span>
            <br><br><br>
            <span style="font-size: 38px; font-family: 'Pinyon Script';">Love, {your_name}</span>
        </div>
    ''', unsafe_allow_html=True)
