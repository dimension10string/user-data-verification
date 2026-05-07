import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="System Verification", page_icon="🔒", layout="wide")

# --- Custom Styling for the Reveal ---
def local_css():
    st.markdown("""
        <style>
        .birthday-text {
            font-family: 'Helvetica Neue', sans-serif;
            color: #FF4B4B;
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            padding-top: 50px;
        }
        .personal-wish {
            font-size: 24px;
            text-align: center;
            color: #31333F;
            line-height: 1.6;
            margin: 20px auto;
            max-width: 700px;
        }
        </style>
    """, unsafe_allow_html=True)

# --- State Management ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Logic ---
if not st.session_state.authenticated:
    st.title("User Profile Data Sync")
    st.write("Please input the required credentials to access the family dashboard.")
    
    with st.form("login_form"):
        name = st.text_input("Full Name")
        favorite_memory = st.text_input("Secret Access Code (Hint: Our favorite vacation spot?)")
        submit = st.form_submit_button("Verify Identity")
        
        if submit:
            if name.strip() != "" and favorite_memory.strip() != "":
                with st.spinner("Processing data..."):
                    time.sleep(1.5)
                    st.session_state.authenticated = True
                    st.rerun()
            else:
                st.error("Please fill in all fields to proceed.")

else:
    # THE REVEAL PAGE
    local_css()
    st.balloons() # This triggers the built-in Streamlit confetti/balloons
    
    st.markdown('<p class="birthday-text">Happy Birthday, [Name]! ❤️</p>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="personal-wish">
            Dearest [Name], <br><br>
            I wanted to create something as unique and wonderful as you are. 
            You make every day better just by being in it, and I'm so grateful 
            to be the one by your side. <br><br>
            <b>Here's to another year of us.</b>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Optional: Display an image of you two or her gift
    # st.image("your_photo.jpg", use_column_width=True)
    
    if st.button("Log Out"):
        st.session_state.authenticated = False
        st.rerun()