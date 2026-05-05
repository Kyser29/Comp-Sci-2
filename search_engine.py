import os
from document import Document
from search_result import SearchResult
import time
from pypdf import PdfReader
class SearchEngine:
    def __init__(self):
        self.documents = []
        self.index = {}

    def load_documents(self, folder_path):
        try:
            self.documents = []
            self.index = {}

            files = os.listdir(folder_path)

            for file in files:
                full_path = os.path.join(folder_path, file)  # 👈 MOVE THIS HERE

                if file.endswith(".txt"):
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                
                    doc = Document(file, content)
                    self.documents.append(doc)

                elif file.endswith(".pdf"):
                     content = self.read_pdf(full_path)

                     doc = Document(file, content)
                     self.documents.append(doc)
                elif file.endswith(".pdf"):
                    content = self.read_pdf(full_path)

                    doc = Document(file, content)
                    self.documents.append(doc)

            print(f"{len(self.documents)} documents loaded successfully.")

            self.build_index()
            print("Index built successfully.")

        except Exception as e:
            print("Error loading documents:", e)

    def read_pdf(self, file_path):
        from pypdf import PdfReader

        text = ""
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text() 
            if page_text:
                text += page_text + "\n"

            return text

    def display_documents(self):
        if not self.documents:
            print("No documents loaded.")
            return

        for doc in self.documents:
            doc.display_info()

    def linear_search(self, word):
        results = []

        for doc in self.documents:
            content_lower = doc.content.lower()
            word_lower = word.lower()

            count = content_lower.count(word_lower)

            if count > 0:
                results.append(SearchResult(doc.filename, count))

        if not results:
            print("No matches found.")
            return

        results = self.merge_sort_results(results)

        print(f"\nLinear search results for '{word}':")
        for result in results:
            result.display()

    def build_index(self):
        self.index = {}

        for i, doc in enumerate(self.documents):
            words = doc.content.lower().split()

            for word in words:
                word = word.strip(".,!?;:\"()[]{}")

                if word not in self.index:
                    self.index[word] = []

                self.index[word].append(i)

    def indexed_search(self, word):
        word = word.lower().strip(".,!?;:\"()[]{}")

        if word not in self.index:
            print("No matches found.")
            return

        doc_counts = {}

        for doc_index in self.index[word]:
            if doc_index not in doc_counts:
                doc_counts[doc_index] = 0
            doc_counts[doc_index] += 1

        results = []

        for doc_index, count in doc_counts.items():
            filename = self.documents[doc_index].filename
            results.append(SearchResult(filename, count))

        results = self.merge_sort_results(results)

        print(f"\nIndexed search results for '{word}':")
        for result in results:
            result.display()

    # -----------------------------
    # MERGE SORT (RECURSIVE)
    # -----------------------------
    def merge_sort_results(self, results):
        if len(results) <= 1:
            return results

        mid = len(results) // 2
        left = self.merge_sort_results(results[:mid])
        right = self.merge_sort_results(results[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].score > right[j].score:  # descending order
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

    import time

    def compare_search_speeds(self, word):
        if not self.documents:
            print("No documents loaded.")
            return

        word = word.lower().strip(".,!?;:\"()[]{}")

    
        start = time.perf_counter()
        linear_count = 0

        for doc in self.documents:
            linear_count += doc.content.lower().count(word)

        linear_time = time.perf_counter() - start

    
        start = time.perf_counter()
        indexed_count = 0

        if word in self.index:
            indexed_count = len(self.index[word])

        indexed_time = time.perf_counter() - start

        print(f"speed comparison for '{word}':")
        
        print(f"Linear matches: {linear_count}")
        print(f"Linear time: {linear_time:.8f} seconds")
        print(f"Indexed matches: {indexed_count}")
        print(f"Indexed time: {indexed_time:.8f} seconds")

    def read_pdf(self, file_path):
        text = ""

        reader = PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text 
               

