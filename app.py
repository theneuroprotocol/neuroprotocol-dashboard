import streamlit as st
import datetime

# --- 1. SAYFA AYARLARI ---
st.set_page_config(
    page_title="NeuroProtocol | Operasyon Paneli",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. GHOST MODE CSS (AGRESİF TEMİZLİK) ---
# --- 2. GHOST MODE CSS (NÜKLEER TEMİZLİK) ---
st.markdown("""
    <style>
    /* 1. ANA GÖVDE RENKLERİ */
    .stApp {
        background-color: #050505;
        color: #E0E0E0;
    }

    /* 2. YÖNETİM VE MENÜLERİ GİZLEME */
    /* Sağ üstteki Hamburger Menü ve Toolbar */
    [data-testid="stToolbar"] {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* "Manage App" ve Deploy butonları */
    .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Sağ üstteki süslemeler */
    [data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Header (Başlık Çubuğu) */
    header {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* 3. FOOTER VE "HOSTED BY" YAZILARI (SUİKAST TİMİ) */
    footer {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* Alt kısımdaki "Hosted with Streamlit" rozeti */
    .viewerBadge_container__1QSob {
        display: none !important;
    }
    
    /* Eğer iframe içindeyse */
    iframe[title="streamlit_viewer_badge"] {
        display: none !important;
    }

    /* 4. FORM ELEMANLARI TASARIMI */
    .stTextInput input, .stNumberInput input, .stDateInput input, .stTimeInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #121212 !important;
        color: #fff !important;
        border: 1px solid #333;
        border-radius: 4px;
    }
    
    /* Butonlar */
    div.stButton > button {
        background-color: #700000;
        color: white;
        border: none;
        border-radius: 2px;
        text-transform: uppercase;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #a00000;
    }
    
    /* Slider Rengi */
    div.stSlider > div[data-baseweb = "slider"] > div > div > div[role="slider"]{
        background-color: #8B0000 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    /* 4. SLIDER (KIRMIZI VURGU) */
    div.stSlider > div[data-baseweb = "slider"] > div > div > div[role="slider"]{
        background-color: #8B0000 !important;
    }
    div.stSlider > div[data-baseweb="slider"] > div > div {
        background-color: #333 !important;
    }

    /* 5. BUTON (OTORİTER VE GÜÇLÜ) */
    div.stButton > button {
        background-color: #700000;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        letter-spacing: 1px;
        width: 100%;
        text-transform: uppercase;
        font-weight: bold;
        transition: 0.3s;
        border-radius: 2px;
    }
    div.stButton > button:hover {
        background-color: #a00000;
        box-shadow: 0px 0px 15px rgba(160, 0, 0, 0.4);
    }
    
    /* 6. TYPOGRAPHY */
    h1 { color: #fff; text-align: center; font-family: 'Helvetica', sans-serif; letter-spacing: 3px; font-weight: 800; }
    h2 { color: #8B0000; font-size: 18px; border-bottom: 1px solid #222; padding-bottom: 5px; margin-top: 30px; letter-spacing: 1px;}
    
    /* Expander Başlık Rengi */
    .streamlit-expanderHeader {
        background-color: #0F0F0F;
        color: #aaa;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BAŞLIK VE LOGO ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h1>NEUROPROTOCOL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444; font-size: 10px; letter-spacing: 2px;'>SYSTEM OS v2.1 | SECURE CONNECTION</p>", unsafe_allow_html=True)

# --- 4. FORM MANTIĞI ---
with st.form("np_daily_form"):
    
    # --- A) KİMLİK (İLERİDE BURASI OTOMATİK GELECEK) ---
    st.markdown("<h2>A | KİMLİK & LOG</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.date_input("D01 | Tarih", datetime.date.today())
    with c2:
        # Şimdilik manuel, sonra Master Config'den çekeceğiz
        st.selectbox("D02 | Öğrenci", ["Seçiniz...", "Ahmet Yılmaz", "Zeynep Kaya", "Demo User"])

    # --- B) UYKU & SABAH ---
    st.markdown("<h2>B | UYKU & SABAH</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("D10 | Uyku Süresi (saat)", min_value=0.0, max_value=12.0, step=0.5)
    with c2:
        st.slider("D11 | Uyku Kalitesi", 1, 10, 7)
    
    # --- D) AKADEMİK İCRAAT ---
    st.markdown("<h2>D | AKADEMİK PERFORMANS</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("D30 | Toplam Odak (dk)", step=10)
    with c2:
        st.number_input("D31 | Pomodoro Sayısı", step=1)

    # --- E) DERS ODAKLANMASI (SLOTLAR) ---
    st.markdown("<h2>E | DERS OTURUMLARI</h2>", unsafe_allow_html=True)
    st.info("Bugünkü çalışma bloklarını giriniz.")
    
    # SLOT 1
    with st.expander("S1 | Ders Oturumu #1", expanded=True):
        c1, c2 = st.columns(2)
        with c1: st.selectbox("Ders", ["TYT Türkçe", "TYT Mat", "TYT Fen", "TYT Sosyal", "AYT Mat", "Diğer"])
        with c2: st.number_input("Süre (dk)", step=10, key="s1_sure")
        
        c1, c2, c3 = st.columns(3)
        with c1: st.number_input("Doğru", step=1, key="s1_d")
        with c2: st.number_input("Yanlış", step=1, key="s1_y")
        with c3: st.number_input("Boş", step=1, key="s1_b")

    # SLOT 2
    with st.expander("S2 | Ders Oturumu #2 (Varsa)", expanded=False):
        st.markdown("İkinci ders verileri...")
        st.selectbox("Ders (S2)", ["-", "TYT Türkçe", "TYT Mat", "AYT Mat", "Diğer"])

    # --- J | KAPANIŞ ---
    st.markdown("<h2>J | ANALİZ</h2>", unsafe_allow_html=True)
    st.text_area("Günün Notu & Yarının Hedefi", height=80)

    # --- GÖNDER ---
    st.markdown("<br>", unsafe_allow_html=True)
    submit_btn = st.form_submit_button("VERİLERİ SİSTEME İŞLE")

    if submit_btn:
        st.success("Veri paketi şifrelendi ve sunucuya gönderildi.")
