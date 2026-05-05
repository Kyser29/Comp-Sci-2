class SearchResult:
    def __init__(self, filename, score):
        self.filename = filename
        self.score = score

    def display(self):
        print(f"{self.filename} | Matches: {self.score}")