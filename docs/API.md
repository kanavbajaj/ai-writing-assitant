# AI Writing Assistant API Documentation

## Overview

The AI Writing Assistant provides a comprehensive API for document analysis, writing suggestions, and text improvements. This document outlines the available functions and their usage.

## Core Functions

### Document Processing

#### `parse_file(uploaded_file)`
Parses uploaded files and extracts text content.

**Parameters:**
- `uploaded_file`: Streamlit uploaded file object

**Returns:**
- `str`: Extracted text content

**Supported Formats:**
- Text files (.txt)
- PDF files (.pdf)

**Example:**
```python
text_content = parse_file(uploaded_file)
```

#### `chunk_text(text)`
Splits text into smaller chunks for processing.

**Parameters:**
- `text` (str): Input text to chunk

**Returns:**
- `list`: List of text chunks

**Example:**
```python
chunks = chunk_text("Long document text...")
```

### Writing Assistance

#### `generate_phrase_suggestions(current_text, style="general", num_suggestions=3)`
Generates AI-powered suggestions for continuing text.

**Parameters:**
- `current_text` (str): Current text to continue from
- `style` (str): Writing style ("general", "formal", "creative", "technical", "casual")
- `num_suggestions` (int): Number of suggestions to generate (1-5)

**Returns:**
- `str`: Formatted suggestions

**Example:**
```python
suggestions = generate_phrase_suggestions(
    "The sun was setting over the horizon",
    style="creative",
    num_suggestions=3
)
```

#### `improve_writing(text, improvement_type="general")`
Analyzes text and provides improvement suggestions.

**Parameters:**
- `text` (str): Text to improve
- `improvement_type` (str): Focus area ("general", "grammar", "style", "vocabulary", "structure")

**Returns:**
- `str`: Detailed improvement suggestions

**Example:**
```python
improvements = improve_writing(
    "This is a test sentence.",
    improvement_type="grammar"
)
```

### Vector Database Operations

#### `upsert_to_chroma(chunks)`
Adds document chunks to the vector database.

**Parameters:**
- `chunks` (list): List of text chunks to add

**Returns:**
- `None`

**Example:**
```python
upsert_to_chroma(document_chunks)
```

#### `get_retriever()`
Creates a retriever for document search.

**Returns:**
- `Retriever`: LangChain retriever object

**Example:**
```python
retriever = get_retriever()
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google AI API key | Yes |

### Model Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Language Model | `models/gemini-2.5-pro` | Primary AI model |
| Embedding Model | `models/embedding-001` | Text embedding model |
| Chunk Size | 1000 | Maximum chunk size |
| Chunk Overlap | 200 | Overlap between chunks |

## Error Handling

All functions include error handling and will return appropriate error messages when:

- API calls fail
- File parsing errors occur
- Invalid parameters are provided
- Network connectivity issues arise

## Rate Limits

The application respects Google AI API rate limits:
- Maximum 60 requests per minute
- Maximum 1500 requests per day

## Best Practices

### Text Processing
1. Keep individual chunks under 1000 characters
2. Use appropriate writing styles for your content
3. Provide context when requesting suggestions

### Document Upload
1. Ensure files are in supported formats
2. Keep file sizes reasonable (< 10MB)
3. Use clear, well-formatted documents

### API Usage
1. Implement proper error handling
2. Cache results when appropriate
3. Monitor API usage and costs

## Examples

### Complete Document Analysis
```python
# Upload and process document
text = parse_file(uploaded_file)
chunks = chunk_text(text)
upsert_to_chroma(chunks)

# Chat with document
retriever = get_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)
result = qa_chain({"query": "What is the main topic?"})
```

### Writing Assistance Workflow
```python
# Generate suggestions
suggestions = generate_phrase_suggestions(
    "The story begins with",
    style="creative",
    num_suggestions=3
)

# Improve existing text
improvements = improve_writing(
    "This sentence needs improvement.",
    improvement_type="grammar"
)
```

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure `GOOGLE_API_KEY` is set in environment
   - Verify API key is valid and has sufficient quota

2. **File Upload Issues**
   - Check file format is supported
   - Ensure file size is within limits
   - Verify file is not corrupted

3. **Performance Issues**
   - Reduce chunk size for large documents
   - Implement caching for repeated requests
   - Monitor API response times

### Debug Mode

Enable debug mode by setting:
```bash
export DEBUG=True
```

This will provide additional logging information for troubleshooting.

## Support

For additional support:
1. Check the [README.md](README.md) for setup instructions
2. Review the [test files](tests/) for usage examples
3. Create an issue with detailed error information 