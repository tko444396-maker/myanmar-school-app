import streamlit as st

# Page Configuration (ဝဘ်ဆိုဒ်ခေါင်းစဉ်နှင့် ပုံစံသတ်မှတ်ခြင်း)
st.set_page_config(
    page_title="KG မှ Grade 12 ဘာသာရပ်စုံ သင်ခန်းစာများ",
    page_icon="📖",
    layout="centered"
)

# App Header (ခေါင်းစဉ်ပိုင်း)
st.title("📚 KG မှ Grade 12 အထိ ဘာသာရပ်အလိုက် နေ့စဉ် သင်ခန်းစာများ")
st.markdown("အတန်းနှင့် ဘာသာရပ်ကို ရွေးချယ်ပြီး နေ့စဉ်သင်ခန်းစာများနှင့် ဗီဒီယိုများကို လေ့လာပါ။")
st.markdown("---")

# -------------------------------------------------------------
# အတန်းနှင့် ဘာသာရပ်အလိုက် အချက်အလက်များ (ဤနေရာတွင် အသစ်ထည့်နိုင်ပါသည်)
# -------------------------------------------------------------
curriculum_data = {
    "KG": {
        "မြန်မာစာ": {
            "title": "KG - မြန်မာစာ သင်ခန်းစာ",
            "description": "ဗျည်းနှင့် သရများ အသံထွက်လေ့ကျင့်ခန်းနှင့် ရေးနည်းများ။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        "သင်္ချာ": {
            "title": "KG - သင်္ချာ သင်ခန်းစာ",
            "description": "နံပါတ် (၁) မှ (၁၀) အထိ ရေးနည်းနှင့် ရေတွက်ခြင်း လေ့ကျင့်ခန်း။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    },
    "Grade 1": {
        "မြန်မာစာ": {
            "title": "Grade 1 - မြန်မာစာ သင်ခန်းစာ",
            "description": "ပထမတန်း မြန်မာဖတ်စာ အခန်း (၁) ပါ အကြောင်းအရာများ။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        "သင်္ချာ": {
            "title": "Grade 1 - သင်္ချာ သင်ခန်းစာ",
            "description": "ကိန်းဂဏန်းများ ပေါင်းခြင်းနှင့် နှုတ်ခြင်း အခြေခံ။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        "အင်္ဂလိပ်စာ": {
            "title": "Grade 1 - အင်္ဂလိပ်စာ သင်ခန်းစာ",
            "description": "Basic English alphabets and vocabulary words.",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    },
    "Grade 12": {
        "မြန်မာစာ": {
            "title": "Grade 12 - မြန်မာစာ သင်ခန်းစာ",
            "description": "တက္ကသိုလ်ဝင်တန်း မြန်မာစာ ကဗျာနှင့် ဆောင်းပါး ရှင်းလင်းချက်များ။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        "သင်္ချာ": {
            "title": "Grade 12 - သင်္ချာ သင်ခန်းစာ",
            "description": "အထက်တန်းအဆင့် အဆင့်မြင့်သင်္ချာ ပုစ္ဆာများ တွက်ချက်နည်း။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        },
        "ရူပဗေဒ (Physics)": {
            "title": "Grade 12 - ရူပဗေဒ သင်ခန်းစာ",
            "description": "စွမ်းအင်နှင့် လျှပ်စစ်ဆိုင်ရာ အခန်းများ ရှင်းလင်းချက်။",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    }
}

# Sidebar - အတန်းရွေးချယ်ရန်
st.sidebar.header("🎓 အတန်း ရွေးချယ်ရန်")
available_grades = list(curriculum_data.keys())
selected_grade = st.sidebar.selectbox("လေ့လာလိုသည့် အတန်းကို ရွေးပါ", available_grades)

# Sidebar - ရွေးထားသော အတန်းပေါ်မူတည်၍ ဘာသာရပ်ရွေးချယ်ရန်
st.sidebar.header("📖 ဘာသာရပ် ရွေးချယ်ရန်")
available_subjects = list(curriculum_data[selected_grade].keys())
selected_subject = st.sidebar.selectbox("လေ့လာလိုသည့် ဘာသာရပ်ကို ရွေးပါ", available_subjects)

# Main Content (ရွေးချယ်ထားသော အတန်းနှင့် ဘာသာရပ်အချက်အလက်များကို ပြသခြင်း)
if selected_grade and selected_subject:
    lesson_info = curriculum_data[selected_grade][selected_subject]
    
    st.header(lesson_info["title"])
    st.write(lesson_info["description"])
    
    # ဗီဒီယိုပြသခြင်း
    if lesson_info["video_url"]:
        st.video(lesson_info["video_url"])
        
    st.info("💡 ဤနေရာတွင် နေ့စဉ် သင်ခန်းစာအသစ်များနှင့် ဗီဒီယိုလင့်ခ်များကို ဆက်လက်ထည့်သွင်းနိုင်ပါသည်။")

# Footer
st.markdown("---")
st.markdown("© 2026 - KG to Grade 12 ဘာသာရပ်စုံ ပညာရေးအက်ပ် (Powered by Streamlit)")