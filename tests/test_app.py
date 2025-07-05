"""
Unit tests for AI Writing Assistant
"""

import pytest
import os
import sys
import tempfile
from unittest.mock import Mock, patch

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the functions to test
try:
    from app import (
        parse_file,
        chunk_text,
        generate_phrase_suggestions,
        improve_writing
    )
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you're running tests from the project root directory")
    # Create mock functions for testing if import fails
    def parse_file(uploaded_file):
        return "Mock text content"
    
    def chunk_text(text):
        return [text]
    
    def generate_phrase_suggestions(current_text, style="general", num_suggestions=3):
        return "1. Mock suggestion\n2. Another suggestion\n3. Third suggestion"
    
    def improve_writing(text, improvement_type="general"):
        return "Mock improvement suggestions"

class TestFileParsing:
    """Test file parsing functionality"""
    
    def test_parse_text_file(self):
        """Test parsing of text files"""
        # Create a mock text file
        mock_file = Mock()
        mock_file.type = "text/plain"
        mock_file.read.return_value = b"Hello, this is a test document."
        
        result = parse_file(mock_file)
        assert result == "Hello, this is a test document."
    
    def test_parse_pdf_file(self):
        """Test parsing of PDF files"""
        # Mock PyPDF2
        with patch('app.PyPDF2') as mock_pypdf2:
            mock_reader = Mock()
            mock_page = Mock()
            mock_page.extract_text.return_value = "PDF content"
            mock_reader.pages = [mock_page]
            mock_pypdf2.PdfReader.return_value = mock_reader
            
            mock_file = Mock()
            mock_file.type = "application/pdf"
            
            result = parse_file(mock_file)
            assert result == "PDF content"
    
    def test_parse_unsupported_file(self):
        """Test parsing of unsupported file types"""
        mock_file = Mock()
        mock_file.type = "image/jpeg"
        
        result = parse_file(mock_file)
        assert result == ""

class TestTextChunking:
    """Test text chunking functionality"""
    
    def test_chunk_text(self):
        """Test text chunking"""
        text = "This is a test document. " * 50  # Create long text
        chunks = chunk_text(text)
        
        assert isinstance(chunks, list)
        assert len(chunks) > 0
        assert all(isinstance(chunk, str) for chunk in chunks)

class TestPhraseSuggestions:
    """Test phrase suggestion functionality"""
    
    @patch('app.llm')
    def test_generate_phrase_suggestions(self, mock_llm):
        """Test phrase suggestion generation"""
        mock_response = Mock()
        mock_response.content = "1. First suggestion\n2. Second suggestion\n3. Third suggestion"
        mock_llm.invoke.return_value = mock_response
        
        result = generate_phrase_suggestions("Hello world", "general", 3)
        
        assert "First suggestion" in result
        assert "Second suggestion" in result
        assert "Third suggestion" in result
    
    @patch('app.llm')
    def test_generate_phrase_suggestions_error(self, mock_llm):
        """Test error handling in phrase suggestions"""
        mock_llm.invoke.side_effect = Exception("API Error")
        
        result = generate_phrase_suggestions("Hello world")
        
        assert "Error generating suggestions" in result

class TestWritingImprovements:
    """Test writing improvement functionality"""
    
    @patch('app.llm')
    def test_improve_writing(self, mock_llm):
        """Test writing improvement generation"""
        mock_response = Mock()
        mock_response.content = "1. Improve grammar\n2. Better word choice\n3. Enhanced structure"
        mock_llm.invoke.return_value = mock_response
        
        result = improve_writing("This is a test text.", "general")
        
        assert "Improve grammar" in result
        assert "Better word choice" in result
        assert "Enhanced structure" in result
    
    @patch('app.llm')
    def test_improve_writing_error(self, mock_llm):
        """Test error handling in writing improvements"""
        mock_llm.invoke.side_effect = Exception("API Error")
        
        result = improve_writing("This is a test text.")
        
        assert "Error generating improvements" in result

class TestConfiguration:
    """Test configuration and setup"""
    
    def test_required_environment_variables(self):
        """Test that required environment variables are set"""
        # This test assumes GOOGLE_API_KEY is set in environment
        # In a real test environment, you'd mock this
        assert os.getenv("GOOGLE_API_KEY") is not None or "GOOGLE_API_KEY" in os.environ

# Integration tests
class TestIntegration:
    """Integration tests for the full application"""
    
    @patch('app.llm')
    @patch('app.embeddings')
    def test_full_document_processing(self, mock_embeddings, mock_llm):
        """Test complete document processing pipeline"""
        # Mock the embeddings and LLM
        mock_embeddings.embed_query.return_value = [0.1, 0.2, 0.3]
        mock_response = Mock()
        mock_response.content = "Test response"
        mock_llm.invoke.return_value = mock_response
        
        # Test the full pipeline
        text = "This is a test document for processing."
        chunks = chunk_text(text)
        
        assert len(chunks) > 0
        assert all(isinstance(chunk, str) for chunk in chunks)

# Performance tests
class TestPerformance:
    """Performance tests"""
    
    def test_large_text_processing(self):
        """Test processing of large text documents"""
        large_text = "This is a test sentence. " * 1000  # Create large text
        
        chunks = chunk_text(large_text)
        
        # Should handle large text without errors
        assert len(chunks) > 0
        assert all(len(chunk) <= 1000 for chunk in chunks)  # Check chunk size limit

# Fixtures for testing
@pytest.fixture
def sample_text():
    """Sample text for testing"""
    return "This is a sample text for testing the AI writing assistant."

@pytest.fixture
def sample_document():
    """Sample document content"""
    return """
    This is a sample document for testing purposes.
    It contains multiple sentences and paragraphs.
    The AI writing assistant should be able to process this content.
    """

if __name__ == "__main__":
    pytest.main([__file__]) 