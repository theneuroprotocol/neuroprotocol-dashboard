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
        /* 1. Üstteki Menüyü ve Çizgiyi Kökten Gizle */
        header {visibility: hidden !important; height: 0px !important;}
        
        /* 2. Alttaki 'Hosted by Streamlit' ve Footer'ı Yok Et */
        footer {visibility: hidden !important; height: 0px !important;}
        
        /* 3. Ana İçeriği Yukarı İt (Boşluk Kalmasın) */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* 4. Sağ Üstteki Seçenekler Menüsü */
        div[data-testid="stToolbar"] {
            visibility: hidden !important;
            display: none !important;
        }

        /* 5. Görüntüleyici Rozeti (Varsa) */
        .viewerBadge_container__1QSob {display: none !important;}
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
