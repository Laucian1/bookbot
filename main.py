def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        words = get_word_count(text)
        print(text)
        print(f"Word count: {words}")
   

def get_book_text(path):
        with open(path) as f:
                return f.read()
        
def get_word_count(text):
        words = text.split()
        return len(words)

main()