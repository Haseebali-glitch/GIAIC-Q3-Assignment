import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title=" Secure Data Encryption", layout="centered")
st.title(" Secure Data Encryption System")

@st.cache_data
def generate_key():
    return Fernet.generate_key()

if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = generate_key()

fernet = Fernet(st.session_state.fernet_key)

with st.expander(" Encryption Key (Keep this secret!)"):
    st.code(st.session_state.fernet_key.decode(), language='text')

tab1, tab2 = st.tabs([" Encrypt", " Decrypt"])

with tab1:
    st.subheader(" Encrypt a Message")
    user_input = st.text_area("Enter message to encrypt")
    if st.button("Encrypt"):
        if user_input:
            encrypted = fernet.encrypt(user_input.encode()).decode()
            st.success(" Encrypted Message:")
            st.code(encrypted, language='text')
        else:
            st.warning("Please enter a message to encrypt.")

with tab2:
    st.subheader("🔓 Decrypt a Message")
    enc_input = st.text_area("Enter encrypted message")
    if st.button("Decrypt"):
        try:
            decrypted = fernet.decrypt(enc_input.encode()).decode()
            st.success("🔓 Decrypted Message:")
            st.code(decrypted, language='text')
        except Exception as e:
            st.error(" Invalid encrypted message or wrong key!")

with st.expander(" Save Your Encryption Key"):
    st.download_button("Download Key as TXT", data=st.session_state.fernet_key, file_name="encryption_key.txt")

with st.expander(" Upload Encrypted Text File to Decrypt"):
    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])
    if uploaded_file is not None:
        enc_data = uploaded_file.read().decode()
        try:
            decrypted = fernet.decrypt(enc_data.encode()).decode()
            st.success(" Decrypted Content from File:")
            st.code(decrypted)
        except Exception as e:
            st.error(" Decryption failed. Possibly invalid key or message.")
