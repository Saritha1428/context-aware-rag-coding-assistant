def chunk_code(code_data):
    chunks = []
    chunk_size = 500  # Enni characters okko chunk lo undali
    
    for item in code_data:
        content = item['content']
        file_name = item['file_name']
        
        # Simple character-based chunking
        for i in range(0, len(content), chunk_size):
            snippet = content[i : i + chunk_size]
            chunks.append({
                "file_name": file_name,
                "text": snippet
            })
    return chunks