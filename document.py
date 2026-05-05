# document.py
class Document:
    def __init__(self, filename: str, content: str):
        self.filename = filename
        self.content = content

    def display_info(self):
        print(f"Filename: {self.filename}")
        print(f"Length: {len(self.content)} chars")