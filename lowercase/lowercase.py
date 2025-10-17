import sys

if len(sys.argv) != 2:
    print("usage: python3 lowercase.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        content = file.read()
    
    # change only uppercase letters to lowercase
    modified_content = content.lower()
    
    with open(filename, 'w') as file:
        file.write(modified_content)
    
    print(f"processed {filename}: all uppercase letters converted to lowercase")
except FileNotFoundError:
    print(f"error: file '{filename}' not found")
except Exception as e:
    print(f"error: {e}")

