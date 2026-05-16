import streamlit as st
import google.generativeai as genai

# -------------------------------
# Configure Gemini API
# -------------------------------
genai.configure(api_key="AIzaSyDul12w9eJIngabk25r8gVc7_a7lvROhJE")

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📘",
    layout="centered"
)

st.title("📘 StudyMate AI")
st.subheader("AI + Python + Java Learning Assistant")

st.write("Ask any question related to Python, Java, AI, ML, Coding, or Programming.")

# User input
question = st.text_input("Enter your question:")

# Button
if st.button("Get Answer"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            # Generate response from Gemini
            response = model.generate_content(question)

            # Display answer
            st.success("Answer Generated Successfully ✅")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit + Gemini AI")