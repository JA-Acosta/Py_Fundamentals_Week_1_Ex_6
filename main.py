'''
>>> JAAR
>>> 07/14/2023
>>> Practicing Fundamentals Program 6
>>> Version 1
'''
'''
>>> Generates a program that will take a phrase and count the total words in the phrase, total consonants (always including y), and the vowels (always excluding y). The program will then use the word count total as a size for the base of a pyramid that the program will build. Afterwards, the program will ask for a second sentence to determine if both sentences are anagrams.
'''

def main() :

    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    vowels_in_phrase = 0
    consonants_in_phrase = 0

    # Assume the phrase the user enters is a valid phrase without punctuation.
    phrase_1 = input("Enter a phrase and I'll count the words, consonants, and vowels: ").lower()
    word_list = phrase_1.split()
    word_count = len(word_list)
    no_spaces_p1 = phrase_1.replace(' ','')
    sorted_phrase_1 = sorted(no_spaces_p1)

    for ch in phrase_1 :
        if ch in vowels :
            vowels_in_phrase += 1
        elif ch in consonants:
            consonants_in_phrase += 1

    print(f"""
        Calculated Values for your phrase:
        \tWord Count =      {word_count}
        \tConsonant Count = {consonants_in_phrase}
        \tVowel Count =     {vowels_in_phrase}

        """)
    print("Before our next venture, here's a gift: ")
    # print out a pyramid

    for n in range(word_count + 1) :
        space = ' ' * (word_count - n)
        asterisk = '*' * n
        print(f'{space}{asterisk}{asterisk[1::]}')

    print('Let carry on.')
    phrase_2 = input("Enter another phrase and I'll check if it's an anagram of your first phrase: ").lower()
    no_spaces_p2 = phrase_2.replace(' ', '')
    sorted_phrase_2 = sorted(no_spaces_p2)

    if sorted_phrase_1 == sorted_phrase_2 :
        print('The phrases are anagrams.')
    else :
        print("The phrases aren't anagrams.")

if __name__ == '__main__' :
    main()
