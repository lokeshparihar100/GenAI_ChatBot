import streamlit as st
from htmlTemplates import css, bot_template, user_template

#st.set_page_config(page_title="Question and Answering on Web Page", page_icon=":image:")

st.set_page_config(page_title="Chat with Image", page_icon=":camera:")
st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None
    
st.header("Chat with Image :camera:")
user_question = st.text_input("Ask a question about your Image:")
if user_question:
    handle_userinput(user_question)
    
with st.sidebar:
        
    st.subheader("Your Images")
    pdf_docs = st.file_uploader("Upload your Images here and click on 'Process'", accept_multiple_files=True)
    
    if st.button("Process"):
        with st.spinner("Processing"):
            # get pdf text
            raw_text = get_pdf_text(pdf_docs)

            # get the text chunks
            text_chunks = get_text_chunks(raw_text)

            # create vector store
            vectorstore = get_vectorstore(text_chunks)

            # create conversation chain
            st.session_state.conversation = get_conversation_chain(vectorstore) 