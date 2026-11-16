import streamlit as st

# ဖုန်းမျက်နှာပြင်နဲ့ လိုက်ဖက်ညီစေရန် Page Config သတ်မှတ်ခြင်း
st.set_page_config(page_title="မြန်မာကျောင်းသုံး သင်ခန်းစာနှင့် ဗီဒီယိုများ", page_icon="📚", layout="centered")

# App ခေါင်းစဉ်
st.title("📚 ကျောင်းသုံး သင်ခန်းစာနှင့် ဗီဒီယို အက်ပ်")

# Session State များ သတ်မှတ်ခြင်း
if 'users' not in st.session_state:
    st.session_state.users = {"admin": "1234"}  # Admin အကောင့် မူလ (Username: admin, Password: 1234)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""
if 'textbooks' not in st.session_state:
    # နမူနာ ကျောင်းသုံးသင်ခန်းစာများနှင့် ဗီဒီယိုများ
    st.session_state.textbooks = [
        {
            "grade": "Grade 5",
            "subject": "မြန်မာစာ",
            "title": "အခန်း (၁) - ကျောင်းချိန်ရောက်ပြီ",
            "content": "ကျောင်းသားကျောင်းသူများအားလုံး ကျောင်းသို့ ပျော်ရွှင်စွာ လာရောက်ကြပါစို့။ မနက်ခင်း လေညင်းလေးက အလွန်အေးမြသည်။",
            "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # ဥပမာ ဗီဒီယိုလင့်ခ်
        },
        {
            "grade": "Grade 5",
            "subject": "အင်္ဂလိပ်စာ",
            "title": "Unit 1 - Welcome Back to School",
            "content": "Good morning teacher and friends! Welcome back to our classroom. Let's learn English together.",
            "video": ""
        }
    ]

# ဘေးဘောင် (Sidebar) မီနူး
menu = ["ပင်မစာမျက်နှာ", "အကောင့်ဝင်ရန် (Login)", "အကောင့်အသစ်ဖွင့်ရန် (Register)"]
if st.session_state.logged_in:
    if st.session_state.current_user == "admin":
        menu = ["ပင်မစာမျက်နှာ", "သင်ခန်းစာများ ကြည့်ရန်", "သင်ခန်းစာနှင့် ဗီဒီယို တင်ရန် (Admin)", "ထွက်ရန် (Logout)"]
    else:
        menu = ["ပင်မစာမျက်နှာ", "ကျောင်းသုံးသင်ခန်းစာများ ဖတ်ရန်", "ထွက်ရန် (Logout)"]

choice = st.sidebar.selectbox("မီနူး", menu)

# ၁။ ပင်မစာမျက်နှာ
if choice == "ပင်မစာမျက်နှာ":
    st.subheader("ကြိုဆိုပါတယ် ကျောင်းသား/ကျောင်းသူများ 👋")
    st.write("ဤ အက်ပ်မှနေ၍ မြန်မာနိုင်ငံ ကျောင်းသုံးသင်ခန်းစာများနှင့် ဗီဒီယိုများကို အတန်းအလိုက်၊ ဘာသာရပ်အလိုက် ဖုန်းဖြင့် လွယ်ကူစွာ လေ့လာနိုင်ပါသည်။")
    if st.session_state.logged_in:
        st.success(f"လက်ရှိဝင်ထားသော အကောင့် - **{st.session_state.current_user}**")

# ၂။ အကောင့်အသစ်ဖွင့်ရန် (Register - ကျောင်းသားများအတွက်)
elif choice == "အကောင့်အသစ်ဖွင့်ရန် (Register)":
    st.subheader("📝 ကျောင်းသား အကောင့်အသစ်ဖွင့်ခြင်း")
    new_user = st.text_input("အသုံးပြုမည့် နာမည် (Username)")
    new_pass = st.text_input("စကားဝှက် (Password)", type="password")
    
    if st.button("အကောင့်ဖွင့်မည်"):
        if new_user in st.session_state.users:
            st.warning("ဒီနာမည် ရှိနှင့်ပြီးသားပါ။")
        elif new_user == "" or new_pass == "":
            st.error("အချက်အလက်များကို ဖြည့်သွင်းပါ။")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("အကောင့်အောင်မြင်စွာ ဖွင့်ပြီးပါပြီ။ 'အကောင့်ဝင်ရန်' သို့ သွားပါ။")

# ၃။ အကောင့်ဝင်ရန် (Login)
elif choice == "အကောင့်ဝင်ရန် (Login)":
    st.subheader("🔐 အကောင့်ဝင်ခြင်း")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("ဝင်မည်"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success(f"မင်္ဂလာပါ {username}!")
            st.rerun()
        else:
            st.error("Username သို့မဟုတ် Password မှားယွင်းနေပါသည်။")

# ၄။ ကျောင်းသားများအတွက် - ကျောင်းသုံး သင်ခန်းစာများနှင့် ဗီဒီယိုများ ကြည့်ရှုခြင်း
elif choice in ["ကျောင်းသုံးသင်ခန်းစာများ ဖတ်ရန်", "သင်ခန်းစာများ ကြည့်ရန်"]:
    st.subheader("📖 ကျောင်းသုံး သင်ခန်းစာများနှင့် ဗီဒီယိုများ")
    
    # အတန်း ရွေးချယ်ခွင့်
    all_grades = list(set([item['grade'] for item in st.session_state.textbooks]))
    selected_grade = st.selectbox("အတန်း ရွေးပါ", sorted(all_grades) if all_grades else ["Grade 5"])
    
    # ရွေးထားတဲ့ အတန်းအလိုက် သင်ခန်းစာများကို စစ်ထုတ်ပြသခြင်း
    filtered_lessons = [item for item in st.session_state.textbooks if item['grade'] == selected_grade]
    
    if filtered_lessons:
        for lesson in filtered_lessons:
            st.markdown(f"### 📚 [{lesson['subject']}] {lesson['title']}")
            st.write(lesson['content'])
            
            # ဗီဒီယိုပါရှိလျှင် ပြသရန်
            if lesson['video']:
                try:
                    st.video(lesson['video'])
                except:
                    st.warning("ဗီဒီယို လင့်ခ် မမှန်ကန်ပါ။")
                    
            st.divider()
    else:
        st.info("ဤအတန်းအတွက် သင်ခန်းစာ မရှိသေးပါ။")

# ၅။ ဆရာ/ဆရာမများအတွက် - သင်ခန်းစာနှင့် ဗီဒီယိုအသစ် တင်ရန် (Admin Only)
elif choice == "သင်ခန်းစာနှင့် ဗီဒီယို တင်ရန် (Admin)":
    st.subheader("➕ ကျောင်းသုံး သင်ခန်းစာနှင့် ဗီဒီယို အသစ်တင်ခြင်း (Admin)")
    
    with st.form("textbook_video_form"):
        t_grade = st.selectbox("အတန်း ရွေးပါ", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
        t_subject = st.selectbox("ဘာသာရပ် ရွေးပါ", ["မြန်မာစာ", "အင်္ဂလိပ်စာ", "গণিত (Math)", "သိပ္ပံ (Science)", "လူမှုရေး (Social Studies)"])
        t_title = st.text_input("သင်ခန်းစာ ခေါင်းစဉ် (ဥပမာ - အခန်း ၂: ရာသီဥတု)")
        t_content = st.text_area("သင်ခန်းစာ အကြောင်းအရာ အပြည့်အစုံ ရေးသားရန်")
        t_video = st.text_input("YouTube ဗီဒီယို လင့်ခ် (Link ထည့်ရန် - ဥပမာ: https://www.youtube.com/watch?v=...)")
        
        submit_btn = st.form_submit_button("သင်ခန်းစာနှင့် ဗီဒီယို တင်မည်")
        
        if submit_btn:
            if t_title and t_content:
                st.session_state.textbooks.append({
                    "grade": t_grade,
                    "subject": t_subject,
                    "title": t_title,
                    "content": t_content,
                    "video": t_video
                })
                st.success("🎉 ကျောင်းသုံးသင်ခန်းစာနှင့် ဗီဒီယိုကို အောင်မြင်စွာ တင်ပြီးပါပြီ။")
            else:
                st.error("ကျေးဇူးပြု၍ ခေါင်းစဉ်နှင့် အကြောင်းအရာကို ဖြည့်သွင်းပါ။")

# ၆။ ထွက်ရန် (Logout)
elif choice == "ထွက်ရန် (Logout)":
    st.session_state.logged_in = False
    st.session_state.current_user = ""
    st.success("အကောင့်မှ ထွက်လိုက်ပါပြီ။")
    st.rerun()