def palindrome(string, index):

    if len(string) == 1 or index == round(len(string) / 2):
        return f"{string} is a palindrome"
    if string[index] != string[len(string) - index - 1] :
        return f"{string} is not a palindrome"
    else:
        return palindrome(string, index + 1)


print(palindrome('abcba', 0))