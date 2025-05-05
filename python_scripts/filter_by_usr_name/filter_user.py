#Usage: pass the username as the first command-line argument

import sys
username = sys.argv[1]

with open("users.txt", "r") as fin, open(f"{username}_lines.txt", "w") as fout:
    for line in fin:
        if username in line:
            fout.write(line)

print(f"All lines with username {username} were written to {username}_lines.txt")