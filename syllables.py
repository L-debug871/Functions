'''MOHOLO LERATO September 2024'''

# Given a word, calculate how many syllables it contains.

def is_vowel(letter):
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    letter_lower = letter.lower()  # Ensure we compare in lowercase
    return letter_lower in vowel


def count_syllables(word):
    count = 0
    k = 0
    length = len(word)

    # Handle words ending with 'e', reducing the length to ignore a silent 'e'
    if length > 1 and word[-1].lower() == 'e' and not is_vowel(word[-2]):
        length -= 1

    while k < length:
        if is_vowel(word[k]):
            count += 1

            # Skip consecutive vowels (e.g., "ae" or "ou" should count as one syllable)
            while k < length and is_vowel(word[k]):
                k += 1
        else:
            k += 1

    return max(count, 1)  # Ensure at least 1 syllable for very short words like "a"


def main():
    word = input("Enter a word (or 'q' to quit):\n")
    while word.lower() != 'q':
        syllable_count = count_syllables(word)
        print(f"The word {word} has {syllable_count} syllable", end="")
        if syllable_count != 1:
            print("s", end="")
        print(".")
        word = input("Enter a word (or 'q' to quit):\n")


if __name__ == '__main__':
    main()

