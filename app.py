import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="System Access Portal", page_icon="💎", layout="wide")

# --- Custom Styling ---
def local_css():
    st.markdown("""
        <style>
        /* Import Pinyon Script & Montserrat */
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Montserrat:wght@200;400&display=swap');

        /* Background: Soft Tropical Morning */
        .stApp {
            background: linear-gradient(160deg, #f8f9fa 0%, #d1f2f7 50%, #b2ebf2 100%);
        }

        /* Fade-in Animation */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* The Handwriting Header */
        .birthday-text {
            font-family: 'Pinyon Script', cursive;
            color: #005f73;
            text-align: center;
            font-size: clamp(2000px, 50vw, 500px);
            font-weight: 400;
            margin-top: 10px;
            animation: fadeIn 2s ease-in-out;
        }

        /* The Letter Box: Frosted Glass Effect */
        .personal-wish {
            font-family: 'Pinyon Script', cursive;
            font-size: 50px;
            text-align: center;
            color: #264653;
            line-height: 2;
            margin: 0 auto;
            max-width: 800px;
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 60px;
            border-radius: 40px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
            animation: fadeIn 3s ease-in-out;
        }

        /* Styling Input Fields for the 'Boring' look */
        .stTextInput input {
            border-radius: 10px;
            background-color: rgba(255,255,255,0.5);
        }

        /* Elegant CTA Button */
        .stButton>button {
            border-radius: 30px;
            border: 1px solid #005f73;
            background-color: transparent;
            color: #005f73;
            padding: 10px 40px;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-size: 12px;
            transition: 0.5s;
        }
        .stButton>button:hover {
            background-color: #005f73;
            color: white;
            box-shadow: 0 5px 15px rgba(0,95,115,0.3);
        }
        </style>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Login Logic ---
if not st.session_state.authenticated:
    st.title("🛡️ Family Cloud: Secure Node")
    st.caption("Encryption Level: AES-256 | Status: Standby")
    
    with st.form("login_form"):
        name = st.text_input("Verified User Name")
        vacation = st.text_input("Access Token (Memory Location)")
        submit = st.form_submit_button("UNLOCk SYSTEM")
        
        if submit:
            if name.strip().lower() != "" and "cayman" in vacation.lower():
                with st.spinner("Authorizing..."):
                    time.sleep(2)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Invalid Token. Access Logged.")

else:
    # --- THE ELEGANT REVEAL ---
    local_css()
    
    # This creates 3 waves of balloons with a slight pause between them
    for i in range(3):
        st.balloons()
        time.sleep(0.5)
        
    # This adds a continuous shimmering effect that doesn't stop
    st.snow() 
    
    # Hero Image
    st.image("https://images.unsplash.com/photo-1544918877-460635b6d13e?q=80&w=2070&auto=format&fit=crop", 
             use_container_width=True)
    
    # The Pinyon Script Header
    st.markdown('<p class="birthday-text">Happy Birthday, [Name]</p>', unsafe_allow_html=True)
    
    # The Main Message
    st.markdown(
        """
        <div class="personal-wish">
            <span style="font-weight: 200; letter-spacing: 3px; font-size: 14px; text-transform: uppercase;">A Message from the Heart</span><br><br>
            <i>My Dearest [Name],</i> <br><br>
            There are some things that code cannot capture and words cannot fully describe. 
            You are my greatest adventure and my favorite destination. <br><br>
            Thank you for being the person who makes every ordinary day feel extraordinary. 
            I built this little corner of the internet just for you, to remind you how deeply you are loved. <br><br>
            <b>Today is all about you.</b>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Hint for the Kitchen Helper
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-family: Montserrat; font-weight: 200; letter-spacing: 4px; color: #005f73;'>SYSTEM NOTIFICATION: A GIFT AWAITS IN THE KITCHEN ARCHIVE</p>", unsafe_allow_html=True)
    
    # Subtle logout button at the very bottom
    if st.button("Close Secure Connection"):
        st.session_state.authenticated = False
        st.rerun()
