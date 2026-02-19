import streamlit as st
try:
    import google.generativeai as genai
except Exception:
    genai = None
    st.error("Missing 'google-generative-ai' package. Install it with: pip install google-generative-ai")
    st.stop()

# Configure API key
api_key = "AIzaSyCeNBO8aKrt2QVsFhFYG-7ctBUxZyJ5LQA"
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

# Translation function
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI-Powered Language Translator", page_icon="🌍")
st.header("🌍 AI-Powered Language Translator")

text = st.text_area("📝 Enter text to translate:")
source_language = st.selectbox(
    "🌐 Select source language:",
    ["English", "Telugu", "Hindi", "Spanish", "French", "German", "Chinese"]
)

target_language = st.selectbox(
    "🎯 Select target language:",
    ["English", "Telugu", "Hindi", "Spanish", "French", "German", "Chinese"]
)

if st.button("🔁 Translate"):
    if text:
        translated_text = translate_text(text, source_language, target_language)
        st.subheader("📘 Translated Text:")
        st.write(translated_text)
    else:
        st.warning("⚠️ Please enter text to translate")