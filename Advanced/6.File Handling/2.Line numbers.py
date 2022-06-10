# Write a program that reads a text file and inserts line numbers in front of each of its lines and counts all the letters and punctuation marks.
#  The result should be written to another text file. 

signs = ["-", ",", ".", "!", "?", "'"]

with open("2.line_numbers.txt") as f:
    lines = f.readlines()

with open("2.line_numbers_result.txt", "w") as f:
    for line in lines:
        letters = 0
        punc = 0
        for chr in line:
            if chr.isalnum():
                letters +=1
            elif chr in signs:
                punc +=1
        line = f"Line{lines.index(line) + 1}" + line.strip() +f" ({letters})({punc})"
        print(line, file= f)
