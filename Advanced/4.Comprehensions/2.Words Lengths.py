li = [(word, len(word)) for word in input().split(", ")]
for word in li:
    print(f"{word[0]} -> {word[1]}")