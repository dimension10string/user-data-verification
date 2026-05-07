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
            background-color: #ffffff;
        }

        /* Hide Streamlit UI */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stHeader"] {background: rgba(0,0,0,0); border-bottom: none;}

        /* Perfect Center Image Container */
        .img-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin-top: -80px; /* Pulls image to the top */
            overflow: hidden;
        }

        .styled-image {
            width: 100vw !important;
            max-width: 100vw !important;
            height: auto;
            border: none !important;
            border-radius: 0px !important;
            object-fit: cover;
        }

        /* The Birthday Header */
        .birthday-text {
            font-family: 'Pinyon Script', cursive !important;
            color: #00768e !important;
            text-align: center !important;
            font-size: clamp(55px, 14vw, 100px) !important; 
            line-height: 1.1 !important;
            margin: 25px 0 !important;
            padding: 0 15px;
        }

        /* The Letter Box */
        .personal-wish {
            font-family: 'Montserrat', sans-serif !important;
            font-size: clamp(16px, 4.5vw, 22px) !important;
            text-align: center !important;
            color: #2c3e50 !important;
            line-height: 1.7 !important;
            margin: 0 auto !important;
            max-width: 90% !important;
            padding: 10px 15px 120px 15px !important;
        }

        /* Login Form */
        .stForm {
            border: 1px solid #f0f0f0 !important;
            background: white;
            padding: 25px;
            border-radius: 12px;
            max-width: 400px;
            margin: 0 auto;
            box-shadow: 0 2px 10px rgba(0,0,0,0.02);
        }
        </style>
    """, unsafe_allow_html=True)

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    local_css()
    st.markdown("<h3 style='text-align: center; font-family: Montserrat; color: #333; padding-top: 120px;'>Internal Data Verification</h3>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        u_name = st.text_input("User Identification")
        u_token = st.text_input("Security Token")
        submitted = st.form_submit_button("Authenticate")
        
        if submitted:
            if u_name.strip() != "" and "cayman" in u_token.lower():
                with st.spinner("Authorizing..."):
                    time.sleep(1)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Authentication Error.")

else:
    local_css()
    st.snow()
    st.balloons()

    # 1. Image wrapped in a Flexbox container for perfect centering
    st.markdown('''
        <div class="img-container">
            <img src="https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop" class="styled-image">
        </div>
    ''', unsafe_allow_html=True)
    
    # 2. Name
    st.markdown(f'<div class="birthday-text">Happy Birthday, [Wife\'s Name]</div>', unsafe_allow_html=True)
    
    # 3. Letter
    st.markdown(
        f"""
        <div class="personal-wish">
            <p style="letter-spacing: 4px; font-size: 11px; text-transform: uppercase; color: #00768e; margin-bottom: 20px;">A Dedicated Message</p>
            <i style="font-size: 24px;">My Dearest [Wife's Name],</i> <br><br>
            I built this corner of the internet to remind you how deeply you are loved. 
            You make every ordinary day feel extraordinary. <br><br>
            May your day be as serene as a Cayman sunrise. <br><br>
            <b style="color: #00768e;">Your surprise is waiting for you in the kitchen.</b><br><br>
            <span style="font-size: 32px; font-family: 'Pinyon Script';">Love, [Your Name]</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
