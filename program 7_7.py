"""
COMP.CS.100 The 7.7 Python program.
Creator: Rahele Ahmadian
Student id number: 151200445
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    english_words = []
    print("Dictionary contents:")
    for word in sorted(english_spanish.keys()):
        english_words.append(word)
    english_words_str = ', '.join(english_words)
    print(english_words_str)
    while True:


        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish.get(word)}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            word_added_E = input("Give the word to be added in English: ")
            word_added_S = input("Give the word to be added in Spanish: ")
            english_spanish[word_added_E] = word_added_S
            english_words = []
            print("Dictionary contents:")
            for word in sorted(english_spanish.keys()):
                english_words.append(word)
            english_words_str = ', '.join(english_words)
            print(english_words_str)

        elif command == "R":
            word_removed = input("Give the word to be removed: ")
            if word_removed in english_spanish:
                del english_spanish[word_removed]
                english_words = list(english_spanish.keys())
            else:
                print("The word", word_removed, "could not be found from the dictionary.")


        elif command == "P":
            print()
            print("English-Spanish")
            for words in sorted(list(english_spanish.keys())):
                print(words, english_spanish[words])
            spanish_words = list(english_spanish.values())
            print()
            print("Spanish-English")
            spanish_english = {}
            for word in sorted(spanish_words):
                for key, value in english_spanish.items():
                    if value == word:
                        spanish_english[word] = key
                print(word, spanish_english[word])
            print()
        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            text_list = text.split(" ")
            for i , word in enumerate(text_list):
                if word in english_spanish:
                    translated_word = english_spanish.get(word)
                    text_list.remove(word)
                    text_list.insert(i, translated_word)
            translated_text = ' '.join(text_list)
            print("The text, translated by the dictionary:")
            print(translated_text)


        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")



# The commands we want the program to execute begin here.
# Python requires there to be at least one command here.

if __name__ == "__main__":
    main()
