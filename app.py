import streamlit as st

st.title("WhatsApp Business Message Generator with Bulk Sending")

# Step 1: Bulk Customer Numbers Input
customer_numbers = st.text_area(
    "Paste your customers' phone numbers here (comma or newline separated):"
)

# Step 2: Business Info Input
business_name = st.text_input("Enter your business name:")
offer = st.text_area("Enter your offer:")
deadline = st.text_input("Enter deadline (e.g., Sept 25):")

# Step 3: Generate Messages Button
if st.button("Generate Bulk Messages"):

    # Clean customer numbers input
    numbers = [num.strip() for num in customer_numbers.replace("\n", ",").split(",") if num.strip()]
    
    # Generate the offer message
    message = f"""
🔥 SPECIAL OFFER from {business_name}!

{offer}

⏰ Valid until: {deadline}
📱 Reply to this message to claim!
🎁 Limited time only!

Thanks for being our valued customer!
"""

    # Show success message and full message for copying
    st.success("Messages ready to send:")

    # Display personalized messages per customer
    for num in numbers:
        st.code(f"To: {num}\n{message}")
    
    # Option to copy all messages (entire batch) at once
    all_messages = "\n\n".join([f"To: {num}\n{message}" for num in numbers])
    st.text_area("Copy all messages here:", all_messages, height=300)
