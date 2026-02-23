import os

def load_project_files(directory_path):
    code_data = []
    # Only these extensions will be read
    supported_extensions = ['.py', '.js', '.ts', '.java', '.cpp']
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.endswith(ext) for ext in supported_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        code_data.append({"file_name": file, "content": content})
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return code_data