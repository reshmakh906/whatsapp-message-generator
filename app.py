import streamlit as st

st.title("WhatsApp Business Message Generator")

business_name = st.text_input("Enter your business name:")
offer = st.text_area("Enter your offer:")
deadline = st.text_input("Enter deadline (e.g., Sept 25):")

if st.button("Generate Message"):
    message = f"""
    🔥 SPECIAL OFFER from {business_name}!

    {offer}

    ⏰ Valid until: {deadline}
    📱 Reply to this message to claim!
    🎁 Limited time only!

    Thanks for being our valued customer!
    """
    st.success("Your WhatsApp Business Message:")
    st.code(message)
