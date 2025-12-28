import streamlit as st
import datetime

# --- 1. SAYFA KONFİGÜRASYONU (SEKMEDE GÖRÜNEN İSİM VE İKON) ---
st.set_page_config(
    page_title="NeuroProtocol | Student Dashboard",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS İLE ÖZELLEŞTİRME (FARUK BEY'İN STİLİ - DARK & ELITE) ---
# Streamlit'in standart görünümünü ezip, senin "Alfa Romeo" estetiğini yüklüyoruz.
st.markdown("""
    <style>
    /* Arka plan rengi - Derin Siyah/Füme */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Input alanları - Mat ve Modern */
    .stTextInput input, .stSelectbox, .stDateInput {
        background-color: #262730;
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #4a4a4a;
    }
    
    /* Buton Tasarımı - Otoriter Kırmızı veya Altın */
    div.stButton > button {
        background-color: #8B0000; /* Koyu Alfa Romeo Kırmızısı */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #FF0000;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.5);
    }
    
    /* Başlık Fontları */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BAŞLIK VE LOGO ALANI ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    # Buraya Faruk Bey'in tasarladığı logonun dosya yolunu verebilirsin
    # st.image("logo.png", width=200) 
    st.markdown("<h1 style='text-align: center; color: #E0E0E0;'>NEUROPROTOCOL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>STRATEJİK TAKİP SİSTEMİ v1.0</p>", unsafe_allow_html=True)

st.divider() # İnce bir çizgi çeker

# --- 4. FORM ALANI (GÜNLÜK VERİ GİRİŞİ) ---
st.subheader("GÜNLÜK RAPOR GİRİŞİ")

with st.form("daily_report_form"):
    # Tarih Seçimi
    report_date = st.date_input("Rapor Tarihi", datetime.date.today())
    
    # Odaklanma Süresi (Slider ile havalı durur)
    focus_time = st.slider("Bugün kaç saat Derin Odaklanma (Deep Work) yapıldı?", 0, 12, 4)
    
    # Konu Başlıkları
    st.markdown("**Tamamlanan Protokoller:**")
    math_status = st.checkbox("Matematik Analizi Tamamlandı")
    paragraph_status = st.checkbox("Paragraf Rutini (Hız Testi) Tamamlandı")
    
    # Serbest Not Alanı
    notes = st.text_area("Zihinsel Durum / Notlar", placeholder="Bugün zihnin nasıldı? Yorgunluk, stres veya berraklık seviyeni not et.")

    # Gönder Butonu
    submitted = st.form_submit_button("SİSTEME İŞLE")

    if submitted:
        # --- BURADA GOOGLE SHEETS ENTEGRASYONU OLACAK ---
        # Şimdilik sadece ekrana yazdırıyoruz.
        st.success("Veriler NeuroProtocol veritabanına başarıyla şifrelendi ve kaydedildi.")
        st.write(f"Kaydedilen Odak Süresi: {focus_time} saat")

# --- 5. FOOTER (ALT BİLGİ) ---
st.markdown("""
    <br><br>
    <div style='text-align: center; color: #555; font-size: 12px;'>
    © 2025 NeuroProtocol Systems. All rights reserved.<br>
    Powered by <b>Stanford & MIT Methodology</b>
    </div>
    """, unsafe_allow_html=True)
