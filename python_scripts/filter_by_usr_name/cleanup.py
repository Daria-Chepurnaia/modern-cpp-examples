import os 
import glob 
import argparse

parser = argparse.ArgumentParser(description="Delete *_lines.txt files")
parser.add_argument("--dry-run", action="store_true", help="Show files to be deleted without actually deleting them")
args = parser.parse_args()

pattern = "*_lines.txt"
#glob.glob("*_lines.txt") find all the files with a specified name in current dir
files = glob.glob(pattern)

if not files:
    print("No matching files found")
else:
    for file in files:
        if args.dry_run:
            print(f"[DRY-RUN] Would remove: {file}")
        else:
            try:
                os.remove(file)
                print(f"Removed {file}")
            except Exception as e:
                print(f"Error removing {file}: {e}")

