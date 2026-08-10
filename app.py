import streamlit as st
import google.generativeai as genai

# --- 1. API KEY CONFIGURATION ---
GOOGLE_API_KEY = "AIzaSyBFkEvniPQ3UFEUMeI0r0SlqLqVxeoXK6E"
genai.configure(api_key=GOOGLE_API_KEY)

# --- 2. PAGE CONFIGURATION ---
# ఇక్కడ టైటిల్ మార్చాను
st.set_page_config(page_title="Fake News Detector", page_icon="🛡️", layout="wide")

# --- 3. SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 4. CSS లోడ్ చేయడం ---
# ఇందులో పాత హెడర్ కి సంబంధించిన స్టైల్స్ ఏవీ ఉండవు
with open("news.css", "r", encoding="utf-8") as f:
    custom_css = f.read()
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# --- 5. PAGE LOGIC ---

# --- హోమ్ పేజీ (HOME PAGE) ---
if st.session_state.page == 'home':
    with open("news.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # ఇక్కడ బటన్ కోసం HTML కోడ్‌ను యాడ్ చేస్తున్నాము
    # ఇది బ్లూ స్క్రీన్ లోపల అందంగా కనిపిస్తుంది
    button_html = """
    <div style="text-align: center; margin-top: 20px;">
        <form target="_self">
            <button name="verify_button" value="clicked" class="custom-button">
                Verify News Now 
            </button>
        </form>
    </div>
    """
    
    target_sentence = "Our platform helps you identify misinformation and verify the authenticity of news articles and information online."
    
    if target_sentence in html_content:
        # వాక్యం తర్వాత బటన్ వచ్చేలా చేస్తున్నాము
        parts = html_content.split(target_sentence)
        full_html = parts[0] + target_sentence + button_html + parts[1]
        
        # పూర్తి HTMLను ప్రదర్శిస్తుంది
        st.markdown(full_html, unsafe_allow_html=True)
        
        # బటన్ క్లిక్ చేసినట్లు గుర్తించడానికి (Streamlit Query Params ద్వారా)
        if st.query_params.get("verify_button") == "clicked":
            st.query_params.clear() # పారామీటర్స్ క్లియర్ చేస్తుంది
            st.session_state.page = 'verification'
            st.rerun()
    else:
        st.markdown(html_content, unsafe_allow_html=True)



# --- వెరిఫికేషన్ పేజీ (VERIFICATION PAGE) ---
elif st.session_state.page == 'verification':
    # వెనక్కి వెళ్లడానికి బటన్
    if st.button("⬅ Back to Home"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<div class="internal-tag">AI Powered Verification</div>', unsafe_allow_html=True)
    st.markdown("### 🕵️‍♂️ వార్తను ఇక్కడ నమోదు చేయండి:")

    news_input = st.text_area("", placeholder="వార్తను ఇక్కడ పేస్ట్ చేయండి...", height=200)

    # ఇక్కడ మోడల్ సెలెక్ట్ ఆప్షన్ తీసేసి, డైరెక్ట్ గా మోడల్ పేరు ఇస్తున్నాం
    if st.button("నిజమా? అబద్ధమా? సరిచూడు"):
        if news_input:
            with st.spinner("విశ్లేషిస్తోంది..."):
                try:
                    # 1. మొదట gemini-1.5-flash ప్రయత్నిస్తుంది
                    try:
                        model = genai.GenerativeModel('models/gemini-2.5-flash')
                        prompt = f"Analyze this news. Tell if it is Real or Fake. Provide reasoning in English script with clear bullet points. News: {news_input}"
                        response = model.generate_content(prompt)
                    except:
                        # 2. అది పని చేయకపోతే gemini-pro ప్రయత్నిస్తుంది
                        model = genai.GenerativeModel('models/gemini-2.5-pro')
                        prompt = f"Analyze this news. Tell if it is Real or Fake. Provide reasoning in English script with clear bullet points. News: {news_input}"
                        response = model.generate_content(prompt)
                    
                    st.markdown("---")
                    st.markdown("### విశ్లేషణ ఫలితం:")
                    st.success(response.text)
                except Exception as e:
                    # ఒకవేళ మళ్ళీ ఎర్రర్ వస్తే అది ఇక్కడ కనిపిస్తుంది
                    st.error(f"సమస్య ఏర్పడింది: {e}")
        else:
            st.warning("ముందుగా ఏదైనా వార్తను ఎంటర్ చేయండి!")
    st.markdown('</div>', unsafe_allow_html=True)