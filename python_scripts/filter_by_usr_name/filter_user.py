#Usage: python script.py --name username

import argparse

parser = argparse.ArgumentParser(description="Filter lines by username")
parser.add_argument("--name", required=True, help="Username to search for")
args = parser.parse_args();

username = args.name

with open("users.txt", "r") as fin, open(f"{username}_lines.txt", "w") as fout:
    for line in fin:
        if username in line:
            fout.write(line)

print(f"All lines with username {username} were written to {username}_lines.txt")
