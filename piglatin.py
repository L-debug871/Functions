''' a program that changes languages from piglatin to english or the latter
 Moholo Lerato
 10/09/2024
test program for english/piglatin translator'''

import piglatin
# converting english sentence given by the user to piglatin
def to_pig_latin(s):
    vowels = ['a','e','i','o','u','y']
    s = s.split()
    result = []
    for word in s:
        if word[0] in vowels:
            result.append(word + "way")
        else:
            j = 0
            while j<len(word) and word[j] not in vowels:
                j += 1
            result.append(word[j:] + 'a' + word[:j] + 'ay')
    return ' '.join(result)

# converting piglatin sentence given by the user to english
def to_english(s):
    vowels = ['a','e','i','o','u','y']
    translated_words = []
    for word in s.split():
        if  word[-3:] == 'way':
            translated_words.append(word[:-3])
        elif word[0] in vowels:
            word = word[:len(word)-2]
            r_word = word[::-1]
            n_word = r_word[r_word.find('a'):]
            o_word = r_word[:r_word.find('a')][::-1] + n_word[::-1]
            c_word = o_word[:len(word)-1]
            translated_words.append(c_word)
        else:
            index_of_a = word.rfind('a')
            translated_words.append(word[index_of_a+1:-2] + word[:index_of_a])        

    return ' '.join(translated_words)

def main():
    choice = input ("(E)nglish or (P)ig Latin?\n")
    action = choice[:1]
    if action == 'E':
        s = input("Enter an English sentence:\n")
        new_s = piglatin.to_pig_latin(s)
        print("Pig-Latin:")
        print(new_s)
    elif action =='P':
        s = input("Enter a Pig Latin sentence:\n")
        new_s = piglatin.to_english(s)
        print("English:")
        print(new_s)
    
if __name__=='__main__':
    main()
