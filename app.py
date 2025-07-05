"""
AI Writing Assistant (Streamlit + LangChain + Gemini + Chroma)

Setup:
1. Add your Gemini API key to a .env file or set as environment variable.
2. Install dependencies: pip install -r requirements.txt
3. Run: streamlit run app.py
"""

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import tempfile
from langchain_core.documents import Document

# For PDF parsing
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

# Load environment variables
load_dotenv()

# API Key (set this in your .env file or environment)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize LangChain components
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-pro", google_api_key=GOOGLE_API_KEY)

# Chroma vector store setup
persist_directory = "chroma_db"
vectorstore = Chroma(
    collection_name="ai-writing-assistant",
    embedding_function=embeddings,
    persist_directory=persist_directory
)

# Helper: Parse uploaded file
def parse_file(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf" and PyPDF2:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        return ""

# Helper: Chunk text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def chunk_text(text):
    return text_splitter.split_text(text)

# Helper: Upsert to Chroma
def upsert_to_chroma(chunks):
    docs = [Document(page_content=chunk) for chunk in chunks]
    vectorstore.add_documents(docs)
    vectorstore.persist()

# Helper: Get retriever
def get_retriever():
    return vectorstore.as_retriever()

# Helper: Generate phrase suggestions
def generate_phrase_suggestions(current_text, style="general", num_suggestions=3):
    """Generate next phrase suggestions based on current text"""
    
    style_prompts = {
        "general": "Continue the text naturally and engagingly",
        "formal": "Continue in a professional, formal tone",
        "creative": "Continue with creative and imaginative language",
        "technical": "Continue with technical, precise language",
        "casual": "Continue in a friendly, conversational tone"
    }
    
    prompt = f"""
    Based on the following text, suggest {num_suggestions} different ways to continue the next phrase or sentence.
    Current text: "{current_text}"
    
    Style: {style_prompts.get(style, style_prompts['general'])}
    
    Provide {num_suggestions} different suggestions, each as a complete phrase or sentence that naturally continues from the current text.
    Format your response as:
    1. [First suggestion]
    2. [Second suggestion] 
    3. [Third suggestion]
    
    Make sure each suggestion is contextually appropriate and flows naturally from the given text.
    """
    
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating suggestions: {str(e)}"

# Helper: Generate writing improvements
def improve_writing(text, improvement_type="general"):
    """Generate writing improvements and suggestions"""
    
    improvement_prompts = {
        "general": "Provide general writing improvements for clarity, flow, and engagement",
        "grammar": "Focus on grammar, punctuation, and sentence structure improvements",
        "style": "Suggest style improvements for better tone and voice",
        "vocabulary": "Suggest vocabulary enhancements and word choice improvements",
        "structure": "Provide structural improvements for better organization and flow"
    }
    
    prompt = f"""
    Analyze the following text and provide {improvement_prompts.get(improvement_type, improvement_prompts['general'])}.
    
    Text: "{text}"
    
    Provide specific, actionable suggestions for improvement. Include:
    1. Specific changes or alternatives
    2. Explanation of why the suggestion improves the text
    3. Overall assessment of the writing quality
    
    Format your response clearly with numbered suggestions.
    """
    
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating improvements: {str(e)}"

# Streamlit UI
st.title("📝 AI Writing Assistant")
st.write("Upload documents, chat with your AI assistant, and get writing suggestions!")

# Create tabs for different features
tab1, tab2, tab3 = st.tabs(["📚 Document Chat", "✍️ Writing Assistant", "💡 Writing Improvements"])

with tab1:
    st.header("Document Chat")
    st.write("Upload documents and chat with your AI assistant!")
    
    # Document upload
    uploaded_file = st.file_uploader("Upload a document (txt/pdf)", type=["txt", "pdf"], key="chat_uploader")
    
    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")
        text = parse_file(uploaded_file)
        if text:
            chunks = chunk_text(text)
            upsert_to_chroma(chunks)
            st.info(f"Document processed and indexed with {len(chunks)} chunks.")
        else:
            st.error("Failed to parse the uploaded file.")
    
    # Chat interface
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    user_input = st.text_input("Ask a question or request writing help:", key="chat_input")
    
    if st.button("Send", key="chat_send") and user_input:
        retriever = get_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        result = qa_chain({"query": user_input})
        answer = result["result"]
        st.session_state['chat_history'].append(("You", user_input))
        st.session_state['chat_history'].append(("AI", answer))
    
    # Display chat history
    for sender, message in st.session_state['chat_history']:
        st.markdown(f"**{sender}:** {message}")

with tab2:
    st.header("Writing Assistant")
    st.write("Write your text and get AI suggestions for the next phrases!")
    
    # Initialize session state for writing
    if 'current_text' not in st.session_state:
        st.session_state['current_text'] = ""
    
    # Text area for writing
    current_text = st.text_area(
        "Write your text here:",
        value=st.session_state['current_text'],
        height=200,
        placeholder="Start writing your text here...",
        key="writing_textarea"
    )
    
    # Update session state
    st.session_state['current_text'] = current_text
    
    # Writing style selection
    col1, col2 = st.columns(2)
    with col1:
        writing_style = st.selectbox(
            "Writing Style:",
            ["general", "formal", "creative", "technical", "casual"],
            key="writing_style"
        )
    
    with col2:
        num_suggestions = st.slider("Number of suggestions:", 1, 5, 3, key="num_suggestions")
    
    # Generate suggestions button
    if st.button("🎯 Get Phrase Suggestions", key="suggestions_btn") and current_text.strip():
        with st.spinner("Generating suggestions..."):
            suggestions = generate_phrase_suggestions(current_text, writing_style, num_suggestions)
            st.markdown("### 💡 Suggested Next Phrases:")
            st.markdown(suggestions)
    
    # Quick action buttons
    if current_text.strip():
        st.markdown("### Quick Actions:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📝 Continue Writing", key="continue_btn"):
                with st.spinner("Generating continuation..."):
                    continuation = generate_phrase_suggestions(current_text, writing_style, 1)
                    st.session_state['current_text'] = current_text + " " + continuation.split('\n')[0].replace('1. ', '').replace('2. ', '').replace('3. ', '')
                    st.rerun()
        
        with col2:
            if st.button("🔄 Rewrite", key="rewrite_btn"):
                with st.spinner("Generating rewrite..."):
                    rewrite_prompt = f"Rewrite the following text in a {writing_style} style while maintaining the same meaning: {current_text}"
                    response = llm.invoke(rewrite_prompt)
                    st.session_state['current_text'] = response.content
                    st.rerun()
        
        with col3:
            if st.button("✨ Enhance", key="enhance_btn"):
                with st.spinner("Enhancing text..."):
                    enhance_prompt = f"Enhance the following text to make it more engaging and polished: {current_text}"
                    response = llm.invoke(enhance_prompt)
                    st.session_state['current_text'] = response.content
                    st.rerun()

with tab3:
    st.header("Writing Improvements")
    st.write("Get detailed feedback and improvements for your writing!")
    
    # Text area for improvement analysis
    improvement_text = st.text_area(
        "Paste your text for improvement analysis:",
        height=200,
        placeholder="Paste your text here to get improvement suggestions...",
        key="improvement_textarea"
    )
    
    # Improvement type selection
    improvement_type = st.selectbox(
        "Focus on:",
        ["general", "grammar", "style", "vocabulary", "structure"],
        key="improvement_type"
    )
    
    # Generate improvements button
    if st.button("🔍 Analyze & Improve", key="improve_btn") and improvement_text.strip():
        with st.spinner("Analyzing your writing..."):
            improvements = improve_writing(improvement_text, improvement_type)
            st.markdown("### 📊 Writing Analysis & Suggestions:")
            st.markdown(improvements)
    
    # Word count and basic stats
    if improvement_text:
        word_count = len(improvement_text.split())
        char_count = len(improvement_text)
        st.markdown(f"**Text Statistics:** {word_count} words, {char_count} characters")

# Footer
st.markdown("---")
st.markdown("**Setup:** Add your API key to a .env file as follows:")
st.code("""
GOOGLE_API_KEY=your-google-api-key
""")

st.markdown("**Note:** PDF support requires PyPDF2. Install with: pip install PyPDF2") 