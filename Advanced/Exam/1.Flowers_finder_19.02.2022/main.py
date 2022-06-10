words = ("rose", "tulip", "lotus", "daffodil")

# words_info = []
#
# for word in words:
#     curr_word = []
#     for char in word:
#         char_couple = [char, False]
#         curr_word.append(char_couple)
#
#     words_info.append(curr_word)
words_info = []

for word in words:
    curr_word = [word, 0]
    words_info.append(curr_word)


vowels = input().split(" ")
consonants = input().split(" ")
word_found = ""

while vowels and consonants and not word_found:
    for i in range(len(words_info)):
        curr_word, word_found_chars = words_info[i]

        vowel = vowels[0]
        consonant = consonants[-1]

        for char in curr_word:
            if vowel == char or consonant == char:
                words_info[i][1] += 1

        del vowels[0]
        del consonants[-1]

        if len(curr_word) == word_found_chars:
            word_found = curr_word
            break

print(f"Word found: {word_found}" if word_found else "Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(vowels)}")




