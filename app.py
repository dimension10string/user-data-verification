import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Authorized Access Only", page_icon="🔒", layout="wide")

# --- Custom Styling ---
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        .stApp {
            background: radial-gradient(circle, #ffffff 0%, #e0f7fa 100%);
        }

        /* Hide Streamlit Clutter */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}

        /* Image Styling */
        .styled-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 40% !important; 
            border-radius: 150px 150px 20px 20px; 
            box-shadow: 0px 15px 35px rgba(0,0,0,0.1);
            border: 8px solid white;
            margin-top: 30px;
        }

        /* The Birthday Header: Balanced with 'Clamp' */
        .birthday-text {
            font-family: 'Pinyon Script', cursive !important;
            color: #00768e !important;
            text-align: center !important;
            /* Clamp(Minimum, Preferred, Maximum) */
            font-size: clamp(60px, 8vw, 100px) !important; 
            line-height: 1.1 !important;
            margin-top: -10px !important;
            margin-bottom: 10px !important;
            text-shadow: 1px 1px 5px rgba(0,118,142,0.1);
        }

        /* The Letter Box */
        .personal-wish {
            font-family: 'Montserrat', sans-serif !important;
            font-size: clamp(18px, 2vw, 22px) !important;
            text-align: center !important;
            color: #2c3e50 !important;
            line-height: 1.6 !important;
            margin: 0 auto !important;
            max-width: 700px !important;
            padding: 10px 40px 80px 40px !important;
        }

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

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    local_css()
    st.markdown("<h2 style='text-align: center; font-family: Montserrat; color: #333;'>Internal Data Verification</h2>", unsafe_allow_html=True)
    
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
                st.error("Authentication Error.")

else:
    local_css()
    st.snow()
    st.balloons()

    # Image
    st.markdown('<img src="https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop" class="styled-image">', unsafe_allow_html=True)
    
    # Title
    st.markdown(f'<div class="birthday-text">Happy Birthday, [Wife\'s Name]</div>', unsafe_allow_html=True)
    
    # Message
    st.markdown(
        f"""
        <div class="personal-wish">
            <p style="letter-spacing: 5px; font-size: 12px; text-transform: uppercase; color: #00768e; margin-bottom: 15px;">For My Incredible Wife</p>
            <i style="font-size: 24px;">My Dearest [Wife's Name],</i> <br><br>
            I built this corner of the internet to remind you how deeply you are loved. 
            You make every ordinary day feel extraordinary. <br><br>
            May your day be as serene as a Cayman sunrise. <br><br>
            <b style="color: #00768e;">Your surprise is waiting for you in the kitchen.</b><br><br>
            <span style="font-size: 24px; font-family: 'Pinyon Script';">Love, [Your Name]</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
