import os

files_dict = {}

for root, dirs, files in os.walk("."):
    
    for file in files:
        # if file.endswith(".txt"):
        filename , file_extension = os.path.splitext(file)
        

        if file_extension not in files_dict.keys():
            files_dict[file_extension] = []
        else:
            files_dict[file_extension].append(file)

with open("/Users/adelinpachedzhiev/Desktop/report.txt", "w") as f: 
    for key in sorted(files_dict.keys()):
        f.write(key)
        f.write("\n")
        for item in sorted(files_dict[key]):
            f.write(f"- - - {item}")
            f.write("\n")

