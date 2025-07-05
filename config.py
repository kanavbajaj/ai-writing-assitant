"""
Configuration file for AI Writing Assistant
Contains all application settings, constants, and configuration options
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is required")

# AI Model Configuration
GEMINI_MODEL = "models/gemini-2.5-pro"
EMBEDDING_MODEL = "models/embedding-001"

# Vector Database Configuration
CHROMA_PERSIST_DIRECTORY = "chroma_db"
CHROMA_COLLECTION_NAME = "ai-writing-assistant"

# Text Processing Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Writing Styles
WRITING_STYLES = {
    "general": "Continue the text naturally and engagingly",
    "formal": "Continue in a professional, formal tone",
    "creative": "Continue with creative and imaginative language",
    "technical": "Continue with technical, precise language",
    "casual": "Continue in a friendly, conversational tone"
}

# Improvement Types
IMPROVEMENT_TYPES = {
    "general": "Provide general writing improvements for clarity, flow, and engagement",
    "grammar": "Focus on grammar, punctuation, and sentence structure improvements",
    "style": "Suggest style improvements for better tone and voice",
    "vocabulary": "Suggest vocabulary enhancements and word choice improvements",
    "structure": "Provide structural improvements for better organization and flow"
}

# Streamlit Configuration
STREAMLIT_CONFIG = {
    "page_title": "AI Writing Assistant",
    "page_icon": "📝",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# File Upload Configuration
ALLOWED_FILE_TYPES = ["txt", "pdf"]
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# UI Configuration
TEXT_AREA_HEIGHT = 200
MAX_SUGGESTIONS = 5
DEFAULT_SUGGESTIONS = 3

# Error Messages
ERROR_MESSAGES = {
    "api_key_missing": "Google API key is required. Please set GOOGLE_API_KEY in your .env file.",
    "file_upload_failed": "Failed to upload file. Please try again.",
    "file_parse_failed": "Failed to parse the uploaded file.",
    "suggestion_generation_failed": "Failed to generate suggestions. Please try again.",
    "improvement_generation_failed": "Failed to generate improvements. Please try again."
}

# Success Messages
SUCCESS_MESSAGES = {
    "file_uploaded": "File uploaded successfully!",
    "document_processed": "Document processed and indexed successfully!",
    "suggestions_generated": "Suggestions generated successfully!",
    "improvements_generated": "Improvements generated successfully!"
}

# Development Configuration
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Performance Configuration
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
CACHE_TTL = 3600  # 1 hour

# Security Configuration
ALLOWED_ORIGINS = ["*"]  # Configure for production
MAX_REQUEST_SIZE = 50 * 1024 * 1024  # 50MB 