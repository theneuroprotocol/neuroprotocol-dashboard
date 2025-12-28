import streamlit as st
import datetime

# --- 1. SAYFA AYARLARI ---
st.set_page_config(
    page_title="NeuroProtocol | Günlük Operasyon",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS İLE "ALFA ROMEO" TASARIMI (DARK & ELITE) ---
st.markdown("""
    <style>
    /* Genel Ayarlar */
    .stApp { background-color: #050505; color: #E0E0E0; }
    #MainMenu, footer, header { visibility: hidden; }
    
    /* Inputlar - Mat ve Keskin */
    .stTextInput input, .stNumberInput input, .stDateInput input, .stTimeInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #121212 !important;
        color: #fff !important;
        border: 1px solid #333;
        border-radius: 4px;
    }
    
    /* Slider (Skala) Rengi - Kırmızı */
    div.stSlider > div[data-baseweb = "slider"] > div > div > div[role="slider"]{
        background-color: #8B0000 !important;
    }
    div.stSlider > div[data-baseweb="slider"] > div > div {
        background-color: #333 !important;
    }

    /* Expander (Açılır Menü) Başlıkları */
    .streamlit-expanderHeader {
        background-color: #1a1a1a;
        color: #fff; 
        font-weight: bold;
        border-radius: 4px;
    }

    /* Buton - Otoriter Kırmızı */
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
    }
    div.stButton > button:hover {
        background-color: #a00000;
    }
    
    /* Başlıklar */
    h1 { color: #fff; text-align: center; font-family: 'Helvetica', sans-serif; letter-spacing: 2px; }
    h2 { color: #8B0000; font-size: 20px; border-bottom: 1px solid #333; padding-bottom: 5px; margin-top: 30px;}
    .section-code { color: #666; font-size: 12px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BAŞLIK ---
st.markdown("<h1>NEUROPROTOCOL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 14px;'>GÜNLÜK OPERASYON FORMU v1.2</p>", unsafe_allow_html=True)

# --- 4. FORM BAŞLANGICI ---
with st.form("np_daily_form"):
    
    # --- A) KİMLİK ---
    st.markdown("<h2>A | KİMLİK & LOG</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.date_input("D01 | Tarih", datetime.date.today())
    with c2:
        st.selectbox("D02 | Öğrenci", ["Seçiniz...", "Ahmet Yılmaz", "Zeynep Kaya", "Demo User"])
    with c3:
        st.selectbox("D03 | Gün Tipi", ["Okul Günü", "Kurs Günü", "Ev (Full Focus)", "Deneme Günü", "Diğer"])

    # --- B) UYKU & SABAH ---
    st.markdown("<h2>B | UYKU & SABAH RUTİNİ</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("D10 | Uyku Süresi (saat)", min_value=0.0, max_value=12.0, step=0.5)
        st.time_input("D12 | Yatış Saati", value=datetime.time(23, 0))
    with c2:
        st.slider("D11 | Uyku Kalitesi (1-10)", 1, 10, 7)
        st.time_input("D13 | Kalkış Saati", value=datetime.time(7, 0))
    
    st.selectbox("D14 | Sabah Enerji (Uyku Atâleti)", ["Fişek Gibi", "15 dk süper", "1 saatte açıldım", "Baş ağrısı/Yorgun"])
    
    c1, c2 = st.columns(2)
    with c1:
        st.radio("D15 | Sabah İlk 30 dk Telefonsuz", ["Evet", "Hayır"], horizontal=True)
    with c2:
        st.radio("D16 | Sabah Aktivasyon (Güneş+Su)", ["Evet", "Hayır"], horizontal=True)

    # --- C) ÇALIŞMA PENCERESİ ---
    st.markdown("<h2>C | GÜNÜN ÇALIŞMA PENCERESİ</h2>", unsafe_allow_html=True)
    st.selectbox("D20 | Ana Çalışma Penceresi", ["Sabah Bloğu", "Öğle Bloğu", "Akşam Bloğu", "Gece Bloğu"])

    # --- D) AKADEMİK İCRAAT ---
    st.markdown("<h2>D | AKADEMİK İCRAAT (METRİKLER)</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("D30 | Toplam Odaklı Çalışma (dk)", step=10)
        st.number_input("D32 | Ortalama Odak Süresi (dk)", step=5)
    with c2:
        st.number_input("D31 | Pomodoro/Blok Sayısı", step=1)
        st.slider("D33 | Odak Puanı (1-10)", 1, 10, 5)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.slider("D34 | Motivasyon", 1, 10, 5)
    with c2:
        st.slider("D35 | Stres Seviyesi", 1, 10, 5)
    with c3:
        st.selectbox("D36 | Dikkat Dağıtıcı", ["Yok (Clean)", "Telefon", "Çevre/Ses", "İç Ses/Kaygı"])

    # --- E) DERS SLOTLARI (Core Engine) ---
    st.markdown("<h2>E | DERS OTURUMLARI (SLOTLAR)</h2>", unsafe_allow_html=True)
    
    # Kullanıcıya kaç slot gireceğini soruyoruz (Form içinde UI kirliliği olmasın diye expander kullanacağız)
    st.info("💡 Her bir ders oturumu için aşağıdaki panelleri doldurun.")
    
    # SLOT 1
    with st.expander("S1 | Ders Oturumu #1", expanded=True):
        c1, c2 = st.columns(2)
        with c1: st.selectbox("D41_S1 | Ders", ["TYT Türkçe", "TYT Mat", "TYT Fen", "TYT Sosyal", "AYT Mat", "Fizik", "Kimya", "Biyoloji", "Geo", "Diğer"])
        with c2: st.text_input("D42_S1 | Konu", placeholder="Örn: Üslü Sayılar")
        
        c1, c2 = st.columns(2)
        with c1: st.number_input("D43_S1 | Süre (dk)", step=10, key="s1_sure")
        with c2: st.selectbox("D48_S1 | Teknik", ["Konu Çalışma", "Test Çözme", "Aktif Hatırlama", "Deneme Analizi", "Tekrar"], key="s1_tek")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.number_input("D44_S1 | Soru", step=5, key="s1_soru")
        with c2: st.number_input("D45_S1 | Doğru", step=1, key="s1_dogru")
        with c3: st.number_input("D46_S1 | Yanlış", step=1, key="s1_yanlis")
        with c4: st.number_input("D47_S1 | Boş", step=1, key="s1_bos")

    # SLOT 2 (Opsiyonel)
    with st.expander("S2 | Ders Oturumu #2 (Varsa)", expanded=False):
        c1, c2 = st.columns(2)
        with c1: st.selectbox("D41_S2 | Ders", ["-", "TYT Türkçe", "TYT Mat", "TYT Fen", "TYT Sosyal", "AYT Mat", "Fizik", "Kimya", "Biyoloji", "Geo", "Diğer"])
        with c2: st.text_input("D42_S2 | Konu")
        c1, c2 = st.columns(2)
        with c1: st.number_input("D43_S2 | Süre (dk)", step=10, key="s2_sure")
        with c2: st.selectbox("D48_S2 | Teknik", ["-", "Konu Çalışma", "Test Çözme", "Aktif Hatırlama", "Deneme Analizi"], key="s2_tek")
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.number_input("Soru", key="s2_soru")
        with c2: st.number_input("Doğru", key="s2_dogru")
        with c3: st.number_input("Yanlış", key="s2_yanlis")
        with c4: st.number_input("Boş", key="s2_bos")

    # SLOT 3 (Opsiyonel)
    with st.expander("S3 | Ders Oturumu #3 (Varsa)", expanded=False):
        st.markdown("*Bu slot için verileri giriniz (Opsiyonel)*")
        # (Kod tekrarını önlemek için sadeleştiriyorum, normalde burası da S2 gibi full set olur)
        c1, c2 = st.columns(2)
        with c1: st.selectbox("D41_S3 | Ders", ["-", "AYT Mat", "Fizik", "Kimya", "Biyoloji", "Geo"])
        with c2: st.number_input("D43_S3 | Süre (dk)", key="s3_sure")
    
    # --- F | ÖĞRENME TEKNİKLERİ ---
    st.markdown("<h2>F | NÖRO-TEKNİKLER</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.radio("D50 | Aktif Hatırlama?", ["E", "H"], horizontal=True)
    with c2: st.radio("D51 | Interleaving?", ["E", "H"], horizontal=True)
    with c3: st.radio("D52 | Feynman/Elaborasyon?", ["E", "H"], horizontal=True)
    st.number_input("D53 | Hata Defteri Giriş Sayısı", step=1)

    # --- G | DOPAMİN & TOPARLANMA ---
    st.markdown("<h2>G | DOPAMİN & RECOVERY</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.radio("D60 | Telefon İzolasyonu", ["E", "H"], horizontal=True)
    with c2: st.slider("D61 | Dopamin Detoks Başarısı (%)", 0, 100, 70)
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.checkbox("D62 | NSDR")
    with c2: st.checkbox("D63 | Nefes Egzersizi")
    with c3: st.checkbox("D64 | Gevşeme")

    # --- H & I | BESLENME & FİZİKSEL ---
    st.markdown("<h2>H-I | BİYOLOJİK DURUM</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        st.selectbox("D70 | Dengeli Öğün Sayısı", [0, 1, 2, 3])
        st.radio("D73 | Kahvaltı Yaptın mı?", ["E", "H"], horizontal=True)
    with c2:
        st.number_input("D80 | Egzersiz Süresi (dk)", step=10)
        st.radio("D81 | HIIT?", ["E", "H"], horizontal=True)

    # --- J | KAPANIŞ ---
    st.markdown("<h2>J | KAPANIŞ VİZYONU</h2>", unsafe_allow_html=True)
    st.text_input("D90 | Günün TEK Hatası (Analiz)", placeholder="Dikkatsizlik değil, bilgi eksikliğiydi...")
    st.text_input("D91 | Yarın TEK Hedef (Strateji)", placeholder="Türev fasikülü bitecek.")

    # --- GÖNDER BUTONU ---
    st.markdown("<br>", unsafe_allow_html=True)
    submit_btn = st.form_submit_button("SİSTEME İŞLE & ANALİZ ET")

    if submit_btn:
        st.success("Veriler NeuroProtocol Ana Veritabanına (Sheets) Şifrelendi ve Gönderildi. (Simülasyon)")
        st.balloons()

# --- FOOTER ---
st.markdown("<div style='text-align:center; color:#444; margin-top:50px; font-size:11px;'>NEUROPROTOCOL SYSTEMS OS v1.2</div>", unsafe_allow_html=True)
