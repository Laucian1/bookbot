def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        words = get_word_count(text)
        character_count = get_character_count(text)
        print(f"Word count: {words}")
        print(character_count)
   

def get_book_text(path):
        with open(path) as f:
                return f.read()
        
def get_word_count(text):
        words = text.split()
        return len(words)

def get_character_count(text):
        char_dict = {}
        lower_text = text.lower()
        for char in lower_text:
            if char in char_dict:
                char_dict[char] +=1
            else:
                char_dict[char] = 1
        return char_dict
                
                
main()