
import streamlit as st
import pdfplumber

st.title("📑 عارض PDF بسيط")

# رفع ملف PDF
uploaded_file = st.file_uploader("ارفع ملف PDF", type="pdf")

if uploaded_file is not None:
    st.success("تم رفع الملف بنجاح ✅")

    # قراءة محتوى الـ PDF
    with pdfplumber.open(uploaded_file) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text() or ""

    if all_text:
        st.subheader("محتوى الملف:")
        st.text_area("النص المستخرج:", all_text, height=400)
    else:
        st.warning("لم يتم العثور على نص قابل للاستخراج من هذا الملف.")
else:
    st.info("من فضلك ارفع ملف PDF.")
