# Create a program that will receive commands until the command "End". The commands can be:
# "Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)
# "Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it and add the content
# "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
# "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"



import os


while True:

    raw_command = input("enter command\n")

    if raw_command == "End":
        break

    if "-" not in raw_command:
        continue

    raw_command = raw_command.split("-")
    command = raw_command[0]
    file_name = raw_command[1]

    if command == "Create":
        with open(f"{file_name}" , "w") as f:
            f.write("")

    elif command == "Add":

        add_content = raw_command[2]
        with open(f"{file_name}", "a") as f:
            f.write(f"{add_content}")
            f.write(f"\n")

    elif command == "Replace":

        if (os.path.exists(f"{file_name}")):
            if raw_command[2] != raw_command[3]:

                with open(f"{file_name}", "r+") as f:
                    lines = []
                    lines_read = f.readlines()
                    for line in lines_read:
                        print(f"line givven is {line}")
                        while raw_command[2] in line:
                            line = line.replace(raw_command[2], raw_command[3])
                        lines.append(line)

                with open(f"{file_name}", "w") as f:
                    f.writelines(lines)                    

        else:
            print("An error occurred")

        
    elif raw_command[0] == "Delete":
        if (os.path.exists(f"{file_name}")):
            os.remove(f"{file_name}")
        else:
            print("An error occurred")

