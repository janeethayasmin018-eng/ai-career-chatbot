if menu == "AI Chat":
    st.header("💬 Career Chatbot (Offline AI)")

    user_input = st.text_input("Ask your career question")

    if st.button("Ask"):
        if user_input:
            text = user_input.lower()

            # Smart keyword detection
            if any(word in text for word in ["resume", "cv"]):
                reply = """To build a strong resume:
• Keep it clear and concise (1 page)
• Highlight skills and projects
• Use bullet points
• Mention achievements with results
• Customize for each job role"""

            elif any(word in text for word in ["interview", "hr", "questions"]):
                reply = """Interview Tips:
• Practice common questions
• Be confident and clear
• Explain your projects well
• Maintain good body language
• Research the company before interview"""

            elif any(word in text for word in ["skills", "learn", "technology"]):
                reply = """Important Skills for Students:
• Programming (Python/Java)
• Data Structures & Algorithms
• Communication skills
• Problem-solving ability
• Teamwork & adaptability"""

            elif any(word in text for word in ["internship", "job", "placement"]):
                reply = """To get internships/jobs:
• Build strong projects
• Create a good resume
• Apply on LinkedIn & job portals
• Practice coding regularly
• Network with professionals"""

            elif any(word in text for word in ["project", "ideas"]):
                reply = """Project Ideas:
• AI Chatbot
• Resume Analyzer
• Student Management System
• Data Analysis Dashboard
• Web applications using Python"""

            elif any(word in text for word in ["motivation", "confidence"]):
                reply = """Stay Motivated:
• Set small goals
• Practice daily
• Learn from failures
• Stay consistent
• Believe in your growth"""

            else:
                reply = """I can help you with:
• Resume building
• Interview preparation
• Skills development
• Career guidance

Try asking something like:
'How to build a resume?' or 'How to prepare for interviews?'"""

            st.success(reply)
