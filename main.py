def main():
        file_path = "books/frankenstein.txt"
        file_contents = print_franken_book(file_path)
        
        #print(file_contents)
        print("book text here - long (remove this print)")
        print("\n")
        
        count = word_count(file_contents)
        print(f"Word count is {count} words.")
        print("\n")
        
        individual_letter_count = letter_count(file_contents)
        print(individual_letter_count)
        print("\n")
        
        letters = dictionary_to_dictionaries(individual_letter_count)
        report_gen(file_path, count, letters)
        print("\n")

def word_count(file_contents):
        words = file_contents.split()
        count = 0
        for word in words:
                count += 1
        return count

def print_franken_book(file_path):
        with open(file_path) as f:
                file_contents = f.read()
        return(file_contents)

def letter_count(file_contents):
        alphabet_dict = {}
        lowercased = file_contents.lower()
        letters = list(lowercased)

        for letter in letters:
                if letter not in alphabet_dict:
                        alphabet_dict[letter] = 1
                elif letter in alphabet_dict:
                        alphabet_dict[letter] += 1
        
        return alphabet_dict

def sort_on(dict):
        return dict["num"]

def dictionary_to_dictionaries(dictionary):
        letters = []
        dict_split = list(dictionary)
        for letter in dict_split:
                if letter.isalpha():
                        temp_dict = {}
                        temp_dict["name"] = letter
                        temp_dict["num"] = dictionary[letter]
                        letters.append(temp_dict)
        
        letters.sort(reverse=True, key=sort_on)
        return(letters)



def report_gen(path, word_num, lett_cnt_desc):
        print(f"--- Begin report of {path}")
        print(f"{word_num} words found in the document")
        print("\n")
        for i in range(0, len(lett_cnt_desc)):
                print(f"The '{lett_cnt_desc[i]['name']}' "
                        f"character was found '{lett_cnt_desc[i]['num']}' times")
        


main()

