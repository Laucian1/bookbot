def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        words = get_word_count(text)
        character_count = get_character_count(text)
        report = prepare_report(character_count)
        print(f"--- Begin report of {book_path} ---")
        print(f"{words} words found in the document\n")
        print(report)
        print("--- End report ---")

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
                
def prepare_report(char_dict):
        dict_list = []
        for entry in char_dict:
            if entry.isalpha(): 
                temp_dict = {"Character": entry, "number": char_dict.get(entry)}                 
                dict_list.append(temp_dict)
        dict_list.sort(reverse=True, key=sort_on)
        meat = ""
        for i in dict_list:
              character = i.get("Character")
              number = i.get("number")
              meat += f"The '{character}' character was found {number} times\n"
        return meat

def sort_on(dict):
      return dict["number"]
          
main()