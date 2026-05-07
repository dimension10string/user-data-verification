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
        /* Force a plain white, clinical background */
        .stApp { background-color: #ffffff !important; }
        
        /* Hide all Streamlit branding */
        #MainMenu, footer, header, .stDeployButton {visibility: hidden; display:none;}
        
        /* Boring Form Styling */
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
    
    st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; color: #222; padding-top: 80px; letter-spacing: -1px;'>Family Cloud: Archive Sync</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-family: Arial, sans-serif;'>Authorized personnel only. Please input credentials to sync.</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User ID")
        u_token = st.text_input("Access Token (Memory Identifier)")
        
        if st.form_submit_button("Verify Identity"):
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Decrypting Archive..."):
                    time.sleep(2) # Adds a bit of suspense
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Authentication Failed. Invalid Token.")

# --- 2. THE LUXURY REVEAL (POST-AUTH) ---
else:
    # ⚠️ YOUR LOCAL FILE NAMES GO HERE
    bg_filename = "beach_bg.jpg" 
    hero_filename = "us.jpg" 
    
    # Text Variables
    wife_name = "Her Name"  # Replace with her actual name
    your_name = "Your Name" # Replace with your actual name

    st.markdown(f"""
        <style>
        /* Import Elegant Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;300;400&display=swap');

        /* The Full-Page Background (Only active here) */
        .stApp {{ 
            background-image: url("app/static/{bg_filename}"); 
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
        }}
        
        /* Hide Streamlit Clutter */
        #MainMenu, footer, header, .stDeployButton {{visibility: hidden; display:none;}}
        .block-container {{ padding-top: 0rem !important; padding-bottom: 0rem !important; }}

        /* Fade-in Animation */
        @keyframes elegantFade {{
            from {{ opacity: 0; transform: translateY(15px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Full-Bleed Sharp Hero Image (Centered via Flexbox) */
        .img-container {{ 
            display: flex; 
            justify-content: center; 
            align-items: center;
            width: 100vw; 
            margin-left: calc(-50vw + 50%); /* Bypasses Streamlit padding */
            overflow: hidden; 
            animation: elegantFade 1.5s ease-out forwards;
        }}
        .hero-image {{ 
            width: 100%; 
            height: auto; 
            border: none; 
            border-radius: 0px !important; /* Strictly NO rounding */
            box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        }}
        
        /* Perfectly Scaled Calligraphy Text */
        .birthday-text {{
            font-family: 'Pinyon Script', cursive !important;
            color: #ffffff !important; 
            text-align: center !important;
            /* The Clamp: Minimum 50px, fluid 12vw, Maximum 100px */
            font-size: clamp(50px, 12vw, 100px) !important; 
            line-height: 1.1 !important; 
            margin: 30px 10px !important;
            text-shadow: 2px 4px 15px rgba(0,0,0,0.6);
            animation: elegantFade 2s ease-out forwards;
        }}
        
        /* Frosted Glass Letter Box */
        .glass-card {{
            background: rgba(255, 255, 255, 0.12); 
            backdrop-filter: blur(16px); 
            -webkit-backdrop-filter: blur(16px);
            border-top: 1px solid rgba(255,255,255,0.3);
            border-bottom: 1px solid rgba(255,255,255,0.3);
            padding: 50px 20px 80px 20px; 
            margin: 0 auto; 
            width: 100vw;
            margin-left: calc(-50vw + 50%);
            color: white; 
            text-align: center; 
            font-family: 'Montserrat', sans-serif;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.4);
            animation: elegantFade 2.5s ease-out forwards;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Celebratory Effects
    st.snow()
    st.balloons()

    # The UI Layout
    st.markdown(f'<div class="img-container"><img src="app/static/{hero_filename}" class="hero-image"></div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="birthday-text">Happy Birthday, {wife_name}</div>', unsafe_allow_html=True)
    
    st.markdown(f'''
        <div class="glass-card">
            <p style="letter-spacing: 5px; font-size: 11px; text-transform: uppercase; font-weight: 300; margin-bottom: 25px; opacity: 0.9;">A Dedicated Message</p>
            <i style="font-size: 24px; font-weight: 200;">My Dearest {wife_name},</i><br><br>
            <span style="font-size: 18px; line-height: 1.9; font-weight: 300;">
                I built this corner of the internet to remind you how deeply you are loved. <br>
                You make every ordinary day feel extraordinary.<br><br>
                May your day be as serene as a Cayman sunrise.<br><br>
                <b style="font-size: 20px; font-weight: 400; color: #e0f7fa;">Your surprise is waiting for you in the kitchen.</b>
            </span>
            <br><br><br>
            <span style="font-size: 38px; font-family: 'Pinyon Script'; opacity: 0.9;">Love, {your_name}</span>
        </div>
    ''', unsafe_allow_html=True)
