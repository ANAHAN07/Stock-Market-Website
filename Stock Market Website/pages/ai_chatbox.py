import streamlit as st
import openai


openai.api_key = "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"         # May chatgpt API Key

# Making the chatbox
def ai_chatbox():
    st.title("AI Chatbox - Stock Market Assistant")
    
    # Chat History
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Displaying previous chat history
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.write(f"**You:** {message['content']}")
        else:
            st.write(f"**AI:** {message['content']}")
    
    # User input
    user_input = st.text_input("Ask a question about the stock market:")
    
    if st.button("Send") and user_input:
        # Add the users message to the chat history
        st.session_state['messages'].append({"role": "user", "content": user_input})
        
        with st.spinner('AI is thinking...'):
            # Send the chat history to the OpenAI API
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # or gpt-4, depending on availability (can't working because i have to buy the api)
                prompt="\n".join([message["content"] for message in st.session_state['messages']]),  # Use a simple prompt
                max_tokens=200,  # Adjust token limit based on requirements
                temperature=0.7
            )
            
            # Get the AI response
            ai_message = response['choices'][0]['text'].strip()  # Adjust to match API response format
            
            # Add AI message to the chat history
            st.session_state['messages'].append({"role": "assistant", "content": ai_message})
            
            # Display the AI response
            st.write(f"**AI:** {ai_message}")

if __name__ == "__main__":
    ai_chatbox()
