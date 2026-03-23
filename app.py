import streamlit as st

st.set_page_config(page_title="AI Career Assistant Pro", layout="centered")

# 1. CREATE THE MENU FIRST (This fixes the NameError)
menu = st.sidebar.selectbox(
    "Choose Feature",
    ["AI Chat", "Resume Builder", "Interview Trainer"]
)

# 2. NOW USE THE IF STATEMENTS
if menu == "AI Chat":
    st.header("💬 Career Chatbot (Offline AI)")

    user_input = st.text_input("Ask your career question")

    if st.button("Ask"):
        if user_input:
            text = user_input.lower()
            
            # --- Your keyword logic starts here ---
            if any(word in text for word in ["resume", "cv"]):
                reply = "..." # (Your resume text)
            # ... (Rest of your elif statements)
            else:
                reply = "I can help you with..."
            
            st.success(reply)

# 3. ADD PLACEHOLDERS FOR OTHER TABS (To prevent errors when switching)
elif menu == "Resume Builder":
    st.header("📄 Resume Generator")
    st.info("Coming soon!")

elif menu == "Interview Trainer":
    st.header("🎤 Interview Trainer")
    st.info("Coming soon!")
  
