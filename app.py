import streamlit as st
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

# Try importing OpenAI
try:
    from openai import OpenAI
    client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))
except:
    client = None

st.set_page_config(page_title="AI Career Assistant Pro", layout="centered")

# ---------------- UI DESIGN ----------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Career Assistant Pro")
st.caption("Resume • Interview • AI Chat 🚀")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["AI Chat", "Resume Builder", "Interview Trainer"]
)

# ---------------- AI CHAT ----------------
if menu == "AI Chat":
    st.header("💬 Chat with AI")

    user_input = st.text_input("Ask your career question")

    if st.button("Ask"):
        if user_input:
            if client:
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": user_input}]
                    )
                    reply = response.choices[0].message.content
                except:
                    reply = "API error. Check your key."
            else:
                reply = "AI not connected. Add API key."

            st.success(reply)

# ---------------- RESUME BUILDER ----------------
elif menu == "Resume Builder":
    st.header("📄 Resume Generator")

    name = st.text_input("Full Name")
    role = st.text_input("Target Role")
    skills = st.text_area("Skills")
    project = st.text_area("Project")

    def create_pdf(name, role, skills, project):
        file_path = "resume.pdf"
        doc = SimpleDocTemplate(file_path)
        styles = getSampleStyleSheet()

        content = []
        content.append(Paragraph(f"<b>{name}</b>", styles["Title"]))
        content.append(Spacer(1, 10))
        content.append(Paragraph(f"Aspiring {role}", styles["Normal"]))
        content.append(Spacer(1, 10))
        content.append(Paragraph(f"<b>Skills:</b> {skills}", styles["Normal"]))
        content.append(Spacer(1, 10))
        content.append(Paragraph(f"<b>Project:</b> {project}", styles["Normal"]))

        doc.build(content)
        return file_path

    if st.button("Generate Resume"):
        st.success("Resume Generated!")

        st.write(f"**{name}** - {role}")
        st.write("Skills:", skills)
        st.write("Project:", project)

        pdf_file = create_pdf(name, role, skills, project)

        with open(pdf_file, "rb") as f:
            st.download_button("📥 Download Resume PDF", f, file_name="resume.pdf")

# ---------------- INTERVIEW TRAINER ----------------
elif menu == "Interview Trainer":
    st.header("🎤 Interview Trainer")

    role = st.text_input("Enter Role")

    if st.button("Start"):
        question = f"Tell me about yourself for a {role} role."
        st.write("### Question")
        st.info(question)

        answer = st.text_area("Your Answer")

        if st.button("Get Feedback"):
            if client:
                try:
                    feedback = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "Give interview feedback"},
                            {"role": "user", "content": answer}
                        ]
                    )
                    result = feedback.choices[0].message.content
                except:
                    result = "API error."
            else:
                if len(answer) < 50:
                    result = "Answer too short. Add details."
                else:
                    result = "Good answer. Improve confidence and clarity."

            st.success(result)
