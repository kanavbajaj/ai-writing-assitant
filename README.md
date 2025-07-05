# AI Writing Assistant

A comprehensive AI-powered writing assistant built with Streamlit, LangChain, and Google's Gemini AI. This application provides document analysis, writing suggestions, and real-time phrase recommendations.

## 🚀 Features

### 📚 Document Chat
- Upload and analyze documents (TXT, PDF)
- Chat with your documents using AI
- Retrieve specific information from uploaded content
- Context-aware responses based on document content

### ✍️ Writing Assistant
- **Real-time Phrase Suggestions**: Get AI-powered suggestions for continuing your text
- **Multiple Writing Styles**: Choose from general, formal, creative, technical, or casual styles
- **Quick Actions**: 
  - Continue writing with AI suggestions
  - Rewrite text in different styles
  - Enhance text for better engagement
- **Customizable Suggestions**: Generate 1-5 different phrase options

### 💡 Writing Improvements
- **Comprehensive Analysis**: Get detailed feedback on your writing
- **Focus Areas**: Grammar, style, vocabulary, structure, or general improvements
- **Text Statistics**: Word count and character analysis
- **Actionable Suggestions**: Specific improvements with explanations

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: LangChain (v0.3.26)
- **LangChain Community**: v0.3.27
- **LangChain Core**: v0.3.68
- **LangChain Text Splitters**: v0.3.8
- **LangChain Google GenAI**: v2.1.6
- **Language Model**: Google Gemini 2.5 Pro
- **Vector Database**: ChromaDB
- **Embeddings**: Google Generative AI Embeddings
- **Document Processing**: PyPDF2 (for PDF files)

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API key (Gemini)
- Internet connection for AI model access

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-writing-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your-google-api-key-here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🔑 Getting Your Google AI API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## 📖 Usage Guide

### Document Chat
1. Navigate to the "Document Chat" tab
2. Upload a document (TXT or PDF)
3. Wait for the document to be processed
4. Ask questions about the document content
5. Get AI-powered responses based on the uploaded content

### Writing Assistant
1. Go to the "Writing Assistant" tab
2. Start writing in the text area
3. Select your preferred writing style
4. Click "Get Phrase Suggestions" for AI recommendations
5. Use quick action buttons to enhance your writing

### Writing Improvements
1. Navigate to the "Writing Improvements" tab
2. Paste your text for analysis
3. Choose the focus area (grammar, style, etc.)
4. Click "Analyze & Improve" for detailed feedback

## 🎯 Use Cases

- **Academic Writing**: Improve essays, research papers, and reports
- **Creative Writing**: Get inspiration and suggestions for stories and poems
- **Business Writing**: Enhance emails, proposals, and documentation
- **Content Creation**: Generate blog posts, articles, and social media content
- **Document Analysis**: Extract insights from uploaded documents

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google AI API key (required)

### Optional Dependencies
- `PyPDF2`: For PDF file processing (install with `pip install PyPDF2`)

## 📁 Project Structure

```
ai-writing-assistant/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (create this)
├── chroma_db/           # Vector database storage
└── venv/                # Virtual environment
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [LangChain](https://langchain.com/) for AI orchestration
- [Google AI](https://ai.google/) for the Gemini language model
- [ChromaDB](https://www.trychroma.com/) for vector storage

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Include your environment details and error messages

## 🔄 Updates

Stay updated with the latest features and improvements by:
- Starring the repository
- Watching for updates
- Checking the releases page

---

**Happy Writing! ✍️✨** 