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
            margin: 100px auto;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; font-family: Arial; color: #222; padding-top: 50px;'>Family Cloud: Archive Sync</h2>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        st.markdown("<p style='text-align: center; color: #666;'>Verification Required</p>", unsafe_allow_html=True)
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token")
        
        if st.form_submit_button("Verify Identity & Unlock"):
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
    
    # This is a direct link to the audio file. No YouTube player, no ads, no blocking.
    # Note: If this specific link ever expires, you'd just need a new direct .mp3 URL.
    audio_url = "https://raw.githubusercontent.com/AnandSaminathan/Streamlit-Audio-Test/main/LifeInTechnicolor.mp3"

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
        .block-container {{ padding: 0rem !important; }}

        /* Image centering and sizing */
        .img-container {{ 
            display: flex; justify-content: center; width: 100vw; 
            margin-left: calc(-50vw + 50%); overflow: hidden; 
        }}
        .hero-image {{ width: 100%; height: auto; border: none; border-radius: 0px !important; }}
        
        .birthday-text {{
            font-family: 'Pinyon Script', cursive !important;
            color: #ffffff !important; text-align: center !important;
            font-size: clamp(60px, 14vw, 110px) !important; 
            line-height: 1.1 !important; margin: 30px 10px !important;
            text-shadow: 2px 4px 15px rgba(0,0,0,0.6);
        }}
        
        .glass-card {{
            background: rgba(255, 255, 255, 0.15); 
            backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
            border-top: 1px solid rgba(255,255,255,0.3);
            padding: 50px 20px 120px 20px; 
            width: 100vw; margin-left: calc(-50vw + 50%);
            color: white; text-align: center; font-family: 'Montserrat', sans-serif;
        }}
        </style>
    """, unsafe_allow_html=True)

    # THE AUDIO ENGINE
    # This uses the HTML5 audio tag. Browsers allow this after the "Verify" click.
    st.markdown(f"""
        <audio autoplay loop>
            <source src="{audio_url}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

    st.snow()
    st.balloons()

    # Visual Layout
    st.markdown(f'<div class="img-container"><img src="app/static/{hero_filename}" class="hero-image"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="birthday-text">Happy Birthday, {wife_name}</div>', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="glass-card">
            <p style="letter-spacing: 5px; font-size: 11px; text-transform: uppercase; margin-bottom: 25px; opacity: 0.9;">A Birthday Gift</p>
            <i style="font-size: 26px; font-weight: 200;">My Dearest {wife_name},</i><br><br>
            <span style="font-size: 19px; line-height: 1.9; font-weight: 300;">
                I built this corner of the internet to remind you how deeply you are loved. <br>
                You make every ordinary day feel extraordinary.<br><br>
                May your day be as serene as a Cayman sunrise.<br><br>
                <b style="color: #e0f7fa;">Your surprise is waiting for you in the kitchen.</b>
            </span>
            <br><br><br>
            <span style="font-size: 40px; font-family: 'Pinyon Script';">Love, {your_name}</span>
        </div>
    ''', unsafe_allow_html=True)
