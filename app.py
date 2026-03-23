import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Career Assistant Pro", layout="centered", page_icon="🚀")

# ---------------- CUSTOM UI ----------------
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to:", ["💬 Offline AI Chat", "📄 Resume Generator", "🎤 Interview Trainer"])

# ---------------- 💬 OFFLINE AI CHAT ----------------
if menu == "💬 Offline AI Chat":
    st.header("💬 Career Chatbot (Offline AI)")
    st.caption("Smart career guidance without internet AI APIs.")

    user_input = st.text_input("Ask your career question")

    if st.button("Ask Assistant"):
        if user_input:
            text = user_input.lower()

            if "resume" in text or "cv" in text:
                reply = """**How to Build a Strong Resume:**
• Keep it short (1 page)
• Highlight skills and projects
• Use bullet points
• Add achievements with results
• Customize for each job"""

            elif "interview" in text:
                reply = """**Interview Tips:**
• Practice common questions
• Explain projects clearly
• Maintain confidence
• Research company
• Use STAR method"""

            elif "skills" in text or "learn" in text:
                reply = """**Important Skills:**
• Programming (Python/Java)
• Data Structures & Algorithms
• Communication skills
• Problem-solving
• Teamwork"""

            elif "internship" in text or "job" in text:
                reply = """**Getting Internships/Jobs:**
• Build strong projects
• Create a good resume
• Apply on LinkedIn
• Practice coding
• Network with professionals"""

            elif "project" in text:
                reply = """**Project Ideas:**
• AI Chatbot
• Resume Analyzer
• Data Dashboard
• Web App using Python
• Student Management System"""

            elif "confidence" in text:
                reply = """**Boost Confidence:**
• Practice daily
• Start small
• Learn from mistakes
• Stay consistent
• Believe in yourself"""

            else:
                reply = "I can help with Resume, Interview, Skills, and Projects. Try asking something specific."

            st.info(reply)

# ---------------- 📄 RESUME GENERATOR ----------------
elif menu == "📄 Resume Generator":
    st.header("📄 Professional Resume Builder")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")

    with col2:
        role = st.text_input("Target Role")
        skills = st.text_input("Skills (comma separated)")

    experience = st.text_area("Experience / Projects")

    if st.button("Generate Resume"):
        if name and email and role:
            file_path = "resume.pdf"
            doc = SimpleDocTemplate(file_path, pagesize=LETTER)
            styles = getSampleStyleSheet()

            header_style = ParagraphStyle(
                'Header',
                parent=styles['Heading1'],
                alignment=1,
                fontSize=18,
                textColor=colors.black
            )

            content = [
                Paragraph(f"<b>{name.upper()}</b>", header_style),
                Paragraph(f"{email} | Aspiring {role}", styles['Normal']),
                HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=10, spaceAfter=10),
                Spacer(1, 12),
                Paragraph("<b>SKILLS</b>", styles['Heading3']),
                Paragraph(skills, styles['Normal']),
                Spacer(1, 12),
                Paragraph("<b>PROJECTS / EXPERIENCE</b>", styles['Heading3']),
                Paragraph(experience.replace("\n", "<br />"), styles['Normal']),
            ]

            doc.build(content)

            with open(file_path, "rb") as f:
                st.download_button("📥 Download Resume", f, file_name="resume.pdf")

            st.success("Resume Generated Successfully!")
        else:
            st.error("Please fill required fields")

# ---------------- 🎤 INTERVIEW TRAINER ----------------
elif menu == "🎤 Interview Trainer":
    st.header("🎤 Mock Interview")

    questions = [
        "Tell me about yourself.",
        "Explain one project you worked on.",
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 3 years?",
        "Why should we hire you?"
    ]

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0

    progress = (st.session_state.q_index + 1) / len(questions)
    st.progress(progress)

    st.subheader(f"Question {st.session_state.q_index + 1}")
    st.write(questions[st.session_state.q_index])

    user_answer = st.text_area("Your Answer")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Next"):
            if st.session_state.q_index < len(questions) - 1:
                st.session_state.q_index += 1
                st.rerun()

    with col2:
        if st.button("Reset"):
            st.session_state.q_index = 0
            st.rerun()

    if user_answer:
        if len(user_answer) < 40:
            st.warning("Try to give a more detailed answer.")
        else:
            st.success("Good answer! Keep improving confidence and clarity.")
