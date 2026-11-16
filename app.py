import streamlit as st

# Page Configuration (ဝဘ်ဆိုဒ်ခေါင်းစဉ်နှင့် ပုံစံသတ်မှတ်ခြင်း)
st.set_page_config(
    page_title="KG မှ Grade 12 သင်ခန်းစာများ",
    page_icon="🎒",
    layout="centered"
)

# App Header (ခေါင်းစဉ်ပိုင်း)
st.title("📚 KG မှ Grade 12 အထိ နေ့စဉ် သင်ခန်းစာများ")
st.markdown("ဘယ်ဘက်ခြမ်းမှ မိမိလေ့လာလိုသည့် **အတန်း** ကို ရွေးချယ်ပါ။")
st.markdown("---")

# -------------------------------------------------------------
# KG မှ Grade 12 အထိ အတန်းအလိုက် အချက်အလက်များ (ဤနေရာတွင် နေ့စဉ် အသစ်ထည့်နိုင်ပါသည်)
# -------------------------------------------------------------
grades_data = {
    "KG": {
        "title": "KG (Kindergarten) - မူလတန်းကြို သင်ခန်းစာ",
        "description": "ကလေးငယ်များအတွက် အခြေခံအက္ခရာ၊ နံပါတ်နှင့် ပုံဆွဲခြင်း လေ့ကျင့်ခန်းများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 1": {
        "title": "Grade 1 - ပထမတန်း သင်ခန်းစာ",
        "description": "ပထမတန်းအတွက် မြန်မာစာ၊ အင်္ဂလိပ်စာနှင့် သင်္ချာ အခြေခံသင်ခန်းစာများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 2": {
        "title": "Grade 2 - ဒုတိယတန်း သင်ခန်းစာ",
        "description": "ဒုတိယတန်းအတွက် နေ့စဉ်လေ့လာရန် သင်ခန်းစာများနှင့် ဗီဒီယိုများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 3": {
        "title": "Grade 3 - တတိယတန်း သင်ခန်းစာ",
        "description": "တတိယတန်းအတွက် သင်ခန်းစာ အချက်အလက်များနှင့် လေ့ကျင့်ခန်းများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 4": {
        "title": "Grade 4 - စတုတ္ထတန်း သင်ခန်းစာ",
        "description": "စတုတ္ထတန်းအတွက် နေ့စဉ် သင်ခန်းစာများနှင့် ဗီဒီယိုများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 5": {
        "title": "Grade 5 - ပဉ္စမတန်း သင်ခန်းစာ",
        "description": "ပဉ္စမတန်း မူလတန်းအဆင့် ပြီးမြောက်ရေး သင်ခန်းစာများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 6": {
        "title": "Grade 6 - ဆဋ္ဌမတန်း သင်ခန်းစာ",
        "description": "အလယ်တန်းအဆင့် ပထမနှစ်အတွက် အခြေခံ သင်ခန်းစာများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 7": {
        "title": "Grade 7 - သတ္တမတန်း သင်ခန်းစာ",
        "description": "သတ္တမတန်းအတွက် အသေးစိတ် သင်ခန်းစာများနှင့် ရှင်းလင်းချက်များ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 8": {
        "title": "Grade 8 - အဋ္ဌမတန်း သင်ခန်းစာ",
        "description": "အဋ္ဌမတန်းအတွက် နေ့စဉ်လေ့လာရန် သင်ခန်းစာများနှင့် ဗီဒီယိုများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 9": {
        "title": "Grade 9 - နဝမတန်း သင်ခန်းစာ",
        "description": "အလယ်တန်းနောက်ဆုံးနှစ်အတွက် အရေးကြီးသော သင်ခန်းစာများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 10": {
        "title": "Grade 10 - ဒသမတန်း သင်ခန်းစာ",
        "description": "အထက်တန်းအဆင့် ပထမနှစ်အတွက် သင်ခန်းစာများနှင့် ရှင်းလင်းချက်များ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 11": {
        "title": "Grade 11 - ဧကာဒသမတန်း သင်ခန်းစာ",
        "description": "အထက်တန်း အဆင့်မြင့် သင်ခန်းစာများနှင့် လေ့ကျင့်ခန်းများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Grade 12": {
        "title": "Grade 12 - ဒွါဒသမတန်း သင်ခန်းစာ",
        "description": "တက္ကသိုလ်ဝင်တန်း (Grade 12) အတွက် အထူးသင်ခန်းစာများနှင့် ဗီဒီယိုများ။",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
}

# Sidebar - အတန်းရွေးချယ်ရန်
st.sidebar.header("🎓 အတန်း ရွေးချယ်ရန်")
selected_grade = st.sidebar.selectbox("လေ့လာလိုသည့် အတန်းကို ရွေးပါ", list(grades_data.keys()))

# Main Content (ရွေးချယ်ထားသော အတန်း၏ အချက်အလက်များကို ပြသခြင်း)
if selected_grade:
    grade_info = grades_data[selected_grade]
    
    st.header(grade_info["title"])
    st.write(grade_info["description"])
    
    # ဗီဒီယိုပြသခြင်း
    if grade_info["video_url"]:
        st.video(grade_info["video_url"])
        
    st.info("💡 နေ့စဉ် သင်ခန်းစာအသစ်များနှင့် ဗီဒီယိုလင့်ခ်များကို ဤနေရာတွင် ဆက်လက်ထည့်သွင်းနိုင်ပါသည်။")

# Footer
st.markdown("---")
st.markdown("© 2026 - KG to Grade 12 ပညာရေးအက်ပ် (Powered by Streamlit)")