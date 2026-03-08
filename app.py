import streamlit as st
import ollama

st.set_page_config(page_title="Women Safety Chatbot", page_icon="🛡", layout="wide")

st.title("🛡 Women Safety Awareness Chatbot")

st.markdown("Ask questions about **women safety, emergency help, travel safety, and online safety.**")

# Sidebar
st.sidebar.title("🚨 Emergency Help")

st.sidebar.write("### India Women Helpline Numbers")

st.sidebar.info("""
📞 Emergency: 112  
📞 Women Helpline: 1091  
📞 Women Helpline (All India): 181  
📞 Police: 100  
""")

st.sidebar.write("Stay aware. Stay safe. 💜")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask about women safety...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # System prompt
    system_prompt = """
You are a helpful assistant that provides women safety awareness.

Your job is to:
- Provide safety tips for women
- Give emergency helpline numbers (especially India)
- Help with travel safety advice
- Provide online harassment safety guidance
- Suggest self defense awareness

Always answer clearly and supportively.
"""

    # Generate response using Ollama
    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    bot_reply = response["message"]["content"]

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)