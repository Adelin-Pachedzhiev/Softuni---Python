# Write a program that reads a text file and prints on the console its even lines. 
# Line numbers start from 0. Before you print the result replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
signs = ["-", ",", ".", "!", "?"]


with open("1.Even_lines.txt") as f:
    lines =  [line.strip() for line in f.readlines()]

for i in range(len(lines)):
    if i % 2 == 0:
        line = lines[i]
        line.strip(r"\n")
        for j in range(len(line)):
            if line[j] in signs:
                line = line.replace(line[j], "@")
    
        print(" ".join(reversed(line.split(" "))))
        
        

