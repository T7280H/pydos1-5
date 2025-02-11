import subprocess
import os

def edit_command():
    # مسیر فایل editor.py در فولدر apps
    editor_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'apps', 'editor.py'))
    
    if os.path.exists(editor_path):
        # اجرای فایل editor.py
        subprocess.run(['python', editor_path])
    else:
        print(f"File not found: {editor_path}")

if __name__ == "__main__":
    edit_command()