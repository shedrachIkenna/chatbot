import streamlit as st
import replicate 
import os

st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")

# Sidebar
with st.sidebar:
    # Define web app frontend for accepting API token
    st.title('🦙💬 Llama 2 Chatbot')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate Api Token:', type='password')
        if not (replicate_api.startswith('r8_') and len (replicate_api) == 40):
            st.warning('Please enter your credentials',  icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api

    # Adjustments for model parameters 
    # Set subheader
    st.subheader('Models and Parameters')
    # Define select box for choosing models 
    selected_model = st.sidebar.selectbox('Choose a Llama model', ['Llama2-7B', 'Llama2-13B'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    # Define temperature slider 
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    # Define top-p slider
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    # Define max_length slider
    max_length = st.sidebar.slider('max_length', min_value=32, max_value=128, value=120, step=8)

# Store, display and clear chat messages

# Set initial message in the session_state
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Clear chat history 
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)



st.title('🎈 App Name')

st.write('Hello world!')
