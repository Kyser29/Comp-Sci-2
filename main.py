from search_engine import SearchEngine
from history_linked_list import SearchHistory


def main():
    engine = SearchEngine()
    history = SearchHistory()

    print(" Kings Squire ")
    print(" Indexed Search & Sorting Engine")
   
    while True:
        print("\n1. Load documents")
        print("2. Display documents")
        print("3. Linear search")
        print("4. Indexed search")
        print("5. Show search history")
        print("6. Save search history")
        print("7. Compare speeds")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            engine.load_documents("Documents")

        elif choice == "2":
            engine.display_documents()

        elif choice == "3":
            word = input("Enter word to search: ")
            engine.linear_search(word)
            history.add_search(word, "Linear Search")

        elif choice == "4":
            word = input("Enter word to search: ")
            engine.indexed_search(word)
            history.add_search(word, "Indexed Search")

        elif choice == "5":
            history.display_history()

        elif choice == "6":
            history.save_history()

        elif choice == "0":
            print("Goodbye.")
            break

        elif choice == "7":
            word = input("Enter word to compare: ")
            engine.compare_search_speeds(word)

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()