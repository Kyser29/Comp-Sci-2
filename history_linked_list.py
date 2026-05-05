class HistoryNode:
    def __init__(self, search_term, search_type):
        self.search_term = search_term
        self.search_type = search_type
        self.next = None


class SearchHistory:
    def __init__(self):
        self.head = None

    def add_search(self, search_term, search_type):
        new_node = HistoryNode(search_term, search_type)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def display_history(self):
        if self.head is None:
            print("No search history yet.")
            return

        print("\nSearch History:")
        current = self.head
        count = 1

        while current is not None:
            print(f"{count}. [{current.search_type}] {current.search_term}")
            current = current.next
            count += 1

    def save_history(self, filename="search_history.txt"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                current = self.head

                while current is not None:
                    file.write(f"{current.search_type}: {current.search_term}\n")
                    current = current.next

            print("Search history saved successfully.")

        except Exception as e:
            print("Error saving search history:", e)