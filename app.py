import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Authorized Access Only", page_icon="🔒", layout="wide")

# --- Custom Styling (The "Luxury Boutique" CSS) ---
def local_css():
    st.markdown("""
        <style>
        /* Import Elegant Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        /* Background: Soft Tropical Gradient */
        .stApp {
            background: radial-gradient(circle, #ffffff 0%, #e0f7fa 100%);
        }

        /* Hide Streamlit Clutter */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}

        /* The Image: Rounded and Refined */
        .styled-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50% !important; 
            border-radius: 200px 200px 20px 20px; 
            box-shadow: 0px 20px 40px rgba(0,0,0,0.1);
            border: 10px solid white;
            margin-top: 40px;
        }

        /* The Birthday Header: MASSIVE and Radiant */
        .birthday-text {
            font-family: 'Pinyon Script', cursive !important;
            color: #00768e !important;
            text-align: center !important;
            /* Using vw (viewport width) so it stays huge on all screens */
            font-size: 12vw !important; 
            min-font-size: 80px !important;
            line-height: 0.8 !important;
            margin-top: -20px !important;
            margin-bottom: 20px !important;
            text-shadow: 2px 2px 15px rgba(0,118,142,0.2);
            display: block !important;
        }

        /* The Letter Box: Minimalist & Clean */
        .personal-wish {
            font-family: 'Montserrat', sans-serif !important;
            font-size: 24px !important;
            text-align: center !important;
            color: #2c3e50 !important;
            line-height: 1.8 !important;
            margin: 0 auto !important;
            max-width: 800px !important;
            padding: 20px 40px 100px 40px !important;
        }

        /* Styling the Login Form */
        .stForm {
            border: none !important;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            max-width: 500px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Logic Flow ---
if not st.session_state.authenticated:
    local_css()
    st.markdown("<h2 style='text-align: center; font-family: Montserrat; color: #333;'>Internal Data Verification</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-family: Montserrat; color: #666;'>Please authenticate to sync family records.</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User Identification")
        u_token = st.text_input("Access Token (Memory Location)")
        submitted = st.form_submit_button("Verify & Sync")
        
        if submitted:
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Decrypting Archive..."):
                    time.sleep(2)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Authentication Error: Token not recognized.")

else:
    # --- THE LUXURY REVEAL ---
    local_css()
    
    # Celebratory effects
    st.snow()
    for _ in range(2):
        st.balloons()

    # 1. Image
    st.markdown('<img src="https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop" class="styled-image">', unsafe_allow_html=True)
    
    # 2. The Big Text (Using !important in the HTML tag as well)
    st.markdown(f'<div class="birthday-text">Happy Birthday, [Wife\'s Name]</div>', unsafe_allow_html=True)
    
    # 3. The Letter
    st.markdown(
        f"""
        <div class="personal-wish">
            <p style="letter-spacing: 8px; font-size: 14px; text-transform: uppercase; color: #00768e; margin-bottom: 20px;">For My Incredible Wife</p>
            <i style="font-size: 28px;">My Dearest [Wife's Name],</i> <br><br>
            I built this tiny corner of the internet just to remind you how deeply you are loved. 
            You are the heart of our home and my favorite adventure. <br><br>
            May your day be as beautiful and serene as a Cayman sunrise. <br><br>
            <b style="color: #00768e;">Your surprise is waiting for you in the kitchen.</b><br><br>
            <span style="font-size: 20px; font-family: 'Pinyon Script';">Love, [Your Name]</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
